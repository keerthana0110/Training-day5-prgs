import re
emailAddress = input("Enter email addresses: ")
 
pat2 = "(\w+)@((\w+\.)+(com))"
 
r2 = re.match(pat2,emailAddress)
 
print (r2.group(1))
