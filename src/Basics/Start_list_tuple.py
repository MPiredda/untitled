import os
import sys

sys.path.insert(0, os.path.abspath("./src/"))
html_theme = 'sphinx_rtd_theme'
extensions = ['sphinx.ext.autodoc']


x = 23-22
y = "Hello"
z = 3.43

if z == 3.43 or y == "Hello":
    x = x + 1
    y = y + " World"
    r = 7//2

print(x, y)
print(r)

tu = (2 , "ciao", 3.43, (3,6))   # tupla    sono immutabili, non possiamo t[2] = 3.14
li = ["ciao2", 3, 4.55, "cap"]   # lista    sono mutabili,       possimo li[1] = 45

list1 = ["ciao2", 3, 4.55, "cap"]

list2 = list1                        # 2 names refer to 1 ref
list2 = list1[:]                     # Two independent copies, two refs

d = {"user": "bat", "pswd":1234}     #DIZIONARI
print(d["user"])

d["id"] = 45
print(d)

del d["user"]
print(d)

d.clear()
print(d)


list1 = [1,2,3]
list2 = [4,5,6]
concatened = list1+list2
print(list1,list2,concatened)






