import re
text="hello world?1234"
pattern=re.compile(r"\D")
arr=re.finditer(pattern,text)
for row in arr:
    print(row)