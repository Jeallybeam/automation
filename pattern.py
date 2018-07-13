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
    chunk = message[i:i + 12]
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

# Prefix ###############################################################################################################
import re


def prefHero(message):
    prefRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    print(prefRegex.search(message).group())
    print(prefRegex.search(message).group(1))


prefHero('Batmobile lost a wheel')


# Optional Matching with the Question Mark #############################################################################
import re


def optionalHero(message):
    optionRegex = re.compile(r'Bat(wo)?man')
    print(optionRegex.search(message).group())


optionalHero('The Adventures of Batwoman')


# Optional are number #############################################################################
import re


def areaNumber(message):
    areaRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
    print(areaRegex.search(message).group())


areaNumber('My number is 415-555-4242')
areaNumber('My number is 555-4242')


# Matching Zero or More with the Star ##################################################################################
import re


def zeroormoreHero(message):
    optionRegex = re.compile(r'Bat(wo)*man')
    print(optionRegex.search(message).group())


zeroormoreHero('The Adventures of Batwoman')
zeroormoreHero('The Adventures of Batman')
zeroormoreHero('The Adventures of Batwowowowoman')


# Matching One or More with the Plus ##################################################################################
import re


def zeroormoreHero(message):
    optionRegex = re.compile(r'Bat(wo)+man')
    print(optionRegex.search(message).group())


zeroormoreHero('The Adventures of Batwoman')
'''zeroormoreHero('The Adventures of Batman')''' #Will cause Exception
zeroormoreHero('The Adventures of Batwowowowoman')


# Matching Specific Repetitions with Curly Brackets ####################################################################
import re


def curlyBrackets(message):
    curlyRegex = re.compile(r'(Ha){3}')
    mo = curlyRegex.search(message)
    if mo == None:
        print(mo)
    else:
        print(mo.group())


curlyBrackets('HaHaHa')
curlyBrackets('Ha')


# Greedy Matching ########################################################################################
import re


def greedy(message):
    greedyRegex = re.compile(r'(Ha){3,5}')
    print(greedyRegex.search(message).group())


greedy('HaHaHaHaHa')


# Nongreedy Matching ########################################################################################
import re



def nonGreedy(message):
    nonGreedyRegex = re.compile(r'(Ha){3,5}?')
    print(nonGreedyRegex.search(message).group())


nonGreedy('HaHaHaHaHa')


# The findall() Method ########################################################################################
import re


def findall(message):
    findallRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = findallRegex.findall(message)
    for i in mo:
        print('Number: ' + i)



findall('Cell: 415-555-9999 Work: 212-555-0000')


# Character Classes ########################################################################################
import re


def vowel(message):
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    mo = vowelRegex.findall(message)
    print(mo)


vowel('RoboCop eats baby food. BABY FOOD.')


# negative Character Classes ########################################################################################
import re


def vowel(message):
    vowelRegex = re.compile(r'[^aeiouAEIOU]')
    mo = vowelRegex.findall(message)
    print(mo)


vowel('RoboCop eats baby food. BABY FOOD.')


# The Caret and Dollar Sign Characters ###############################################################################
'''For example, the r'^Hello' regular expression string matches strings
that begin with 'Hello'''
import re


def caret(message):
    caretRegex = re.compile(r'^Hello') '''For example, the r'^Hello' regular expression string matches strings
                                        that begin with 'Hello'.'''
    mo = caretRegex.findall(message)
    print(mo)


caret('Hello world!')
caret('He said hello.')
#
#
#
'''The r'\d$' regular expression string matches strings that end with a
numeric character from 0 to 9.'''
import re


def caret(message):
    caretRegex = re.compile(r'\d$')
    mo = caretRegex.findall(message)
    print(mo)


caret('Your number is 42')
caret('Your number is forty two.')
#
#
#
'''The r'^\d+$' regular expression string matches strings that both begin
and end with one or more numeric characters.'''
import re


def caret(message):
    caretRegex = re.compile(r'^\d+$')
    mo = caretRegex.findall(message)
    print(mo)


caret('1234567890')
caret('12345xyz67890')
caret('12 34567890')



# The Wildcard Character ###############################################################################

