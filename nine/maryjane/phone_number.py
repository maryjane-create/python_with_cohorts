def isPhoneNumber(string):
    if string[0]==0:
        return True
    if len(string)==11:
        return True
    if string[0]!=0:
        return False
    if len(string)!=11:
        return  False




print(isPhoneNumber('09061557705'))