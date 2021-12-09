import re

str = "123?45yy7890"
pat = re.compile("[0-9]{1,3}")
m = re.findall(pat, str)
print(m)