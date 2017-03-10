import keyword
import re
import string

"""
import string
alphas = string.letters + '_'
nums = string.digits
inPut = "Hello"
if inPut[0] in alphas and inPut[1:].replace("_","").isalnum():
    print "Valid identifier for python"
------------------------------------------------
"""


l = []
alphas = string.ascii_letters + '_'
while True:
    s = input()
    if s == '':
        break
    else:
        l.append(s)

for word in l:
    if word[0] in alphas and word[1:].replace("_", "").isalnum():
        print("True")
    else:
        print("False")