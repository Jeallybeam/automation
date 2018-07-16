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
import re


def wildcard(message):
    wildcardRegex = re.compile(r'.at')
    mo = wildcardRegex.findall(message)
    print(mo)


wildcard('The cat in the hat sat on the flat mat.')


# Matching Everything with Dot-Star ###############################################################################
import re


def name(message):
    namedRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    mo = namedRegex.search(message).group(1)
    mo1 = namedRegex.search(message).group(2)
    print(mo)
    print(mo1)


name('First Name: Al Last Name: Sweigart.')
#
#
#Non Greedy
import re


def name(message):
    namedRegex = re.compile(r'<.*?>')
    mo = namedRegex.search(message).group()
    print(mo)


name('<To serve man> for dinner.>')
#
#
#Greedy
import re


def name(message):
    namedRegex = re.compile(r'<.*>')
    mo = namedRegex.search(message).group()
    print(mo)


name('<To serve man> for dinner.>')



# Matching Newlines with the Dot Character #############################################################################
import re


def newline(message):
    newlineRegex = re.compile(r'.*', re.DOTALL)
    mo = newlineRegex.search(message).group()
    print(mo)


newline('Serve the public trust.\nProtect the innocent.\nUphold the law.')



#Substituting Strings with the sub() Method#############################################################################
import re


def substituting(message):
    namesRegex = re.compile(r'Agent \w+')
    mo = namesRegex.sub('CENSORED', message)
    print(mo)


substituting('Agent Alice gave the secret documents to Agent Bob.')
#
#
#
import re


def substituting(message):
    namesRegex = re.compile(r'Agent (\w)\w*')
    mo = namesRegex.sub(r'\1****', message)
    print(mo)


substituting('Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')



#Managing Complex Regexes#############################################################################
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?)')
#
#
#
phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))?           # area code
 (\s|-|\.)?                   # separator
 \d{3}                        # first 3 digits
 (\s|-|\.)                    # separator
 \d{4}                        # last 4 digits
 (\s*(ext|x|ext.)\s*\d{2,5})? # extension
 )''', re.VERBOSE)
