#!venv/bin python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

baseUrl = 'https://www.pio.gov.cy/coronavirus/categories/press'
html = urlopen(baseUrl).read()
html = html.decode('utf-8')

soup = BeautifulSoup(html, features='html.parser')
pdfs = soup.find_all("a", {"class": "flag pdf"})

with open('data.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
	for pdf in pdfs[:10]:
		href = pdf["href"]
		if "stay" in href or "rapid" in href:
			csvwriter.writerow(href, pdf.text)

with open('latest.html', 'w') as f:
	for pdf in pdfs[:10]:
		href = pdf["href"]
		if "stay" in href or "rapid" in href:
			f.writelines(str(pdf))
			f.writelines("<hr>")

