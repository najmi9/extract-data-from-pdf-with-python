import re

f = open('help.md', 'r')
city = zipp= phone=state=None
for line in f.read().split('\n'):
	reg_zip = re.compile(r'(^([A-Z](\w+)\s?([A-Z]\w+)?\s?([A-Z]\w+)?),\s[A-Z]{2}\s)([\d-]*)')
	reg_city = re.compile(r'^([A-Z](\w+)\s?([A-Z]\w+)?\s?([A-Z]\w+)?),\s[A-Z]{2}\s')
	reg_phone = re.compile(r"^(Work Phone: )([\d\+\-\)\(\sA-Z]*)\s")
	reg_state = re.compile(r'(?<=Spouse: ).*')
	try:
		city = reg_city.search(line).group(1)
		zipp = reg_zip.search(line).group(6) 
		phone = reg_phone.search(line).group(2)
		state = reg_state.search(line).group(0) 
	except Exception as e:
		pass
	if phone :
		print(state, '-------')
		state = None
		pass