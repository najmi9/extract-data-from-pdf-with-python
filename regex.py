import re



# words, AA '546-8587'
# 
# reg = re.compile(r'^[A-Z]\w+, [AZ]{2} (.*) ')

# every thing after max and before min
regex = re.compile(r'(?<=max)(.*)(?=min)')
#every thing after max
regex1 = re.compile(r'(?<=max).*')
#every character before the word min
regex2 = re.compile(r'.*(?=min)')

string = "max 22 min 33"
res = regex.search(string).group(0)
res1 = regex1.search(string).group(0)
res2 = regex2.search(string).group(0)

print(string)

print( '(?<=max)(.*)(?=min) ---------- ' + res)
print( '(?<=max).* ------------------- ' + res1)
print( '.*(?=min) -------------------- ' + res2)