import re
pattern = r"[aeiou]"
string = input()
if re.search(pattern,string):
    print("match")
else:
    print("not")