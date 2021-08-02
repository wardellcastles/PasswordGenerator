################################################################
##  This script creates passwords based on user requirements  ##
##    1) Length                                               ##
##    2) Number of passwords to be generated                  ##
##    3) Password must have Upper Case                        ##
##    4) Password must have Lower Case                        ##
##    5) Password must have Special Character                 ##
##    6) Password must have Number                            ##
##                                                            ##
##                                                            ##
##   Copyright(c) 2021 Wardell Castles  vvvvvv                ##
##                http://red7en.com                           ##
################################################################

import string
import random

allLetters = string.ascii_letters
upperLetters = string.ascii_uppercase
lowerLetters = string.ascii_lowercase
numberLetters = string.digits
specialLetters = string.punctuation

pwdLength = input("Password length ")
if int(pwdLength) < 4:
    print("Password Length must be greater than 4")
    exit()
nbrPasswords = input("Number of passwords to be generated ")
mustContainUpper = input("Must contain UPPER CASE (Y/n")
mustContainLower = input("Must contain lower case (Y/n")
mustContainSpecial = input("Must contain Special Character (Y/n")
mustContainNumber = input("Must contain a Number (Y/n")
mustHaveUpper = False
mustHaveLower = False
mustHaveSpecial = False
mustHaveNumber = False
if(mustContainNumber == "Y"):
    mustHaveNumber = True
if(mustContainSpecial == "Y"):
    mustHaveSpecial = True    
if(mustContainUpper == "Y"):
    mustHaveUpper = True
if(mustContainLower == "Y"):
    mustHaveLower = True

haveUppper = False
haveLower = False
haveSpecial = False
haveNumber = False


pwdCounter = 1
while pwdCounter <= int(nbrPasswords):
    passWord=''
    while len(passWord) < int(pwdLength):
        aLetter=random.choice(allLetters)
 #Test for Number       
        isNumber = aLetter.find(string.digits)
        if isNumber != -1 and mustHaveNumber:
               havenumber = True
               passWord += aLetter
 #Test for Special       
        isSpecial = aLetter.find(string.punctuation)
        if isSpecial != -1 and mustHaveSpecial:
            haveSpecial = True
            passWord += aLetter
 #Test for Upper       
        isUpper = aLetter.isupper()
        if isUpper and mustHaveUpper:
            haveUpper = True
            passWord += aLetter
#Test for lower       
        isLower = aLetter.islower()
        if isLower and mustHaveLower:
            haveLower = True
            passWord += aLetter            
    print(passWord)
    pwdCounter += 1