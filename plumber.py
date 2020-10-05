import re
import requests
import pdfplumber
import pandas as pd
from collections import namedtuple
import os
import csv

with open('data.csv', 'w') as csv_file:
	file = csv.writer(csv_file)
	file.writerow(["firstname", "lastname", "email", "adress","city", "state", "phone", "zip"])

l = 0

email = firstname=lastname = adress = zipp = city =  ""
state =  "Not married"
phone = None
with pdfplumber.open('data.pdf') as pdf:
	for page in pdf.pages:
		text = page.extract_text()
		previousline = None
		for n, line in enumerate(text.split('\n')):
			reg_zip = re.compile(r'(^([A-Z](\w+)\s?([A-Z]\w+)?\s?([A-Z]\w+)?),\s[A-Z]{2}\s)([\d-]*)')
			reg_city = re.compile(r'^([A-Z](\w+)\s?([A-Z]\w+)?\s?([A-Z]\w+)?),\s[A-Z]{2}\s')
			reg_phone = re.compile(r"^(Work Phone: )([\d\+\-\)\(\sA-Z]*)\s")
			reg_state = re.compile(r'(?<=Spouse: ).*')

			try:
				city = reg_city.search(line).group(1)
			except:
				pass	
				
			try:
				zipp = reg_zip.search(line).group(6) 
			except Exception as e:
				pass
			
			try:
				state = reg_state.search(line).group(0)
			except Exception as e:
				pass
			
			try:
				phone = reg_phone.search(line).group(2)
			except Exception as e:
				pass

			if '@' in line:
				l = n + 2
				email = line
				firstname = previousline.split()[0]
				lastname = ' '.join(previousline.split()[1:])
			
			if l == n:
				adress = line.split('Spouse:')[0]
			if phone:
				with open("data.csv", "a") as f:
					file = csv.writer(f)
					file.writerow([firstname, lastname, email, adress,city, state, phone, zipp])
				phone=None

			previousline = line