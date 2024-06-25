import re

def emailValidator(email):
    #this method uses the fullmatch() function of re module to validate given email address
    match = re.fullmatch(r'[a-zA-Z0-9]*@[a-z]*.com\b',email)
    if match != None:
        return True
    else:
        return False


email = input("Enter Email to check it's valid or not: ")
if emailValidator(email)==True:
    print('Email is Valid!')
else:
    print('Email Invalid!')
    