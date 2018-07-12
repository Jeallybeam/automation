# Finding Patterns of Text Without Regular Expressions##################################################################
import re
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdigit():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdigit():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdigit():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

########################################################################################################################
import re
def isPhoneNumber(message):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    print(phoneNumRegex.search(message).group())


isPhoneNumber('My number is 415-555-4242.')

def isPhoneNumber_1(message):
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    print(phoneNumRegex.search(message).group())
    print(phoneNumRegex.search(message).group(1))
    print(phoneNumRegex.search(message).group(2))
    print(phoneNumRegex.search(message).group(1, 2))

isPhoneNumber_1('My number is 415-555-4242.')


# Matching Multiple Groups with the Pipe################################################################################
import re
def isHero(message):
    heroRegex = re.compile(r'Batman|Tina Fey')
    print(heroRegex.search(message).group())

isHero('Batman and Tina Fey.')
isHero('Tina FeyX and Tina Fey.')

# Prefix #################################################################################################################
import re
def prefHero(message):
    prefRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    print(prefRegex.search(message).group())

prefHero('Batmobile lost a wheel')