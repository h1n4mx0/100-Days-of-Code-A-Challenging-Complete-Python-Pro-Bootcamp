# Strings Basics
# str, string-module
string1 = 'Pruthviraja L'
print(string1)
#%%
string2 = "Pruthviraja L"
string3 = '''Pruthviraja L'''
string3 = """Pruthviraja L"""
string_ml = """Hi, Welcome to Python For Engineers:
From Beginner To Advanced Level"""
print(string_ml)
#%%
#help(str)
print(dir(str))
print(type(dir(str)))
print(len(dir(str)))
#%%
string_sob = str(object='Pruthviraja L')
print(string_sob)
#%%
print('Pruthvi'.__len__())
print('Pruthvi'.__add__('Raja L'))
#%%
methods = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
           'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
           'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
           'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
           'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
           'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
           'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
           'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
           'upper', 'zfill']
print(len(methods))
#%%
# 'capitalize'
string3 = 'hi, welcome to Python For Engineers'
print(string3.capitalize())
#%%
# 'casefold'
string4 = "PruThviRaja L, is my NAME"
print(string4.casefold())
#%%
# 'centre'
# syntax; string.center(length, fillchar)
# center without fillchar
string5 = 'Hi, welocme to Python For Engineers'
print(len(string5))
print(string5.center(100))
print(string5.center(100, '*'))
print(string5.center(20, '*'))
#%%
# 'count' method
# syntax: string.count(subsring, start, end)
string6 = 'Hi, welcome to Python For Engineers, Python is Popular'
print(len(string6))
print(string6.count('Python', 0, 60))
print(len('Hi, welcome to Pyt'))
print(string6.count('Python', 10, 54))
#%%
# 'endswith'
# syntax: string.endswith(suffix, start, end)
string7 = 'Hi, welcome to Python For Engineers, Python is Popular'
print(string7.endswith('Popular'))
print(string7.endswith('lar'))
print(string7.endswith('Python is Popular'))
print(string7.endswith('Hi, welcome to Python For Engineers, Python is Popular'))
print(string7.endswith('Popular', 0, 60))
print(string7.endswith('Popu', 0, 50))
#%%
# 'startswith'
# syntax: string.startswith(prefix, start, end)
string8 = 'Hi, welcome to Python For Engineers, Python is Popular'
print(string8.startswith('Hi'))
print(string8.startswith('Hi, welcome'))
print(string8.startswith('welcome'))
print(len('Hi, welcome to Python'))
print(string8.startswith('Python', 15, 45))
print(string8.startswith(('Hai', 'welcome', 'H', 'to')))
#%%
# 'expandtabs'
# Syntax: string.exanadtabs(space_size) # \t
string9 = 'Hi\twelcome\tto\tPython For Engineers'
print(string9.expandtabs())
print(string9.expandtabs(4))
print(string9.expandtabs(10.1))
#%%
# 'find'
# 'string.find(sub, start, end)
string10 = 'Hi, welcome to Python For Engineers, Python is Popular'
print(string10.find('to'))
print(string10.find('Python')) # end_index: len(string10)-1
print(string10.find('hai'))
print(string10.find('Python', 17, 60))
print(len('Hi, welcome to Python For Engineers, P'))
#%%
# 'index'
# 'string.index(sub, startp, endp)
string11 = 'Hi, welcome to Python For Engineers'
print(string11.index('For'))
print(string11.index('come'))
print(string11.index('Hi', 2, 30))
print(string11.index('to', 2, 30))
print(string11.index('to', 2, 14))
#%%
# 'isalnum'
# syntax: string.isalnum()
string12 = 'pruthvi34'
print(string12.isalnum())
print('34'.isalnum())
print('pruthvi'.isalnum())
#%%
# 'isdecimal'
# syntax: string.isdecimal()
string13 = '101'
print(string13.isdecimal())
print('pruthvi34'.isdecimal())
print('3-4'.isdecimal())
#%%
# 'isdigit'
# syntax: string.isdigit()
string14 = 'abc150'
print(string14.isdigit())
print('2 3'.isdigit())
#%%
# 'isidentifier'
# syntax: string.isidentifier()
string15 = '_Python3_10_For_Engineers'
print(string15.isidentifier())
#%%
# 'istitle'
# syntax: string.istitle()
string16 = 'Python3.10 For Engineers'
print(string16.istitle())
#%%
# 'join'
# syntax: string.join(iterable_object)
string17 = ['P', 'r', 'u', 't', 'h', 'v', 'i']
string17 = 'Pruthvi'
print('*'.join(string17))
string18 = '12345'
print('-'.join(string18))
#%%
# 'isalpha'
# syntax: string.isalpha()
string19 = 'Pruthvirajalageist34hirtyfour'
print(string19.isalpha())

#%%
# 'islower'
# syntax: string.islower()
string20 = "this is python!!"
print(string20.islower())
#%%
# 'rindex'
# syntax: string.rindex(sub, start, end)
string21 = "This is Python Tutorial and is best"
print(string21.rindex('is'))
print(string21.rindex('is', 0, 20))
print(string21.rindex('T', 15, 33))
print(string21.rindex('end', 15, 33))
#%%
# 'rfind'
# Syntax: string.rfind(sub, start, end) # len(string)-1
string22 = "This is Python Tutorial and is best"
print(string22.rfind('is'))
print(string22.rfind('is', 0, 20))
print(string22.rfind('t', 0, 28))
print(string22.rfind('as', 0, 34))
#%%
# 'split'
# syntax: string.split(separator, maxsplit)
string23 = "This,is,Python,Tutorial:and:is:best"
print(string23.split(','))
print(string23.split(' '))
print(string23.split(':'))
print(string23.split(',', 2))
print(string23.split('t'))
#%%
# 'splitlines'
# syntax: string.splitlines(keep_ends) # \n, \r, \t
string24 = "This\nis\nPython\rTutorial and\risbest"
print(string24.splitlines())
print(string24.splitlines(True))
print(string24.splitlines(0))
#%%
# 'lower'
# syntax: string.lower()
string25 = "This,is,Python34#@,Tutorial:and:is:Best"
print(string25.lower())
#%%
# 'partition'
# syntax: string.partition(separator)
string26 = "This is Python Tutorial and is best"
print(string26.partition('and'))
print(string26.partition('is'))
print(string26.partition('Python'))
print(string26.partition('as'))
#%%
# 'rpartition'
# syntax: string.rpartition(separator)
string27 = "This,is,Python34#@,Tutorial:and:is:Best"
print(string27.rpartition(':'))
print(string27.rpartition('as'))
#%%
# 'strip'
# syntax: string.strip([char's])
string28 = "this is Python Tutorial and is best this"
print(string28.strip())
print(string28.strip('best'))
print(string28.strip('this'))
#%%
# 'rstrip'
# syntax: string.strip([char's])
string29 = " this is Python Tutorial and is best this"
print(string29.rstrip('siht'))
#%%
# 'isspace'
# syntax: string.isspace()
string30 = '             '
print(string30.isspace())
#%%
# 'swapcase()
# syntax: string.swapcase()
string31 = "This is Python Tutorial and is best this"
print(string31.swapcase())
#%%
# 'max'
string32 = "This is PYython Tutorial and is best thiszZ"
print(max(string32))
# a-z
# A-Z
#%%
# 'min'
string32 = "thisispythontutorialandisbestthisz"
print(min(string32))
# A-YZ
# a-z
#%%
# 'upper'
string32 = "This is PYython34@#+ Tutorial and is best thiszZ"
print(string32.upper())
#%%
# 'replace'
string32 = "This is PYython Tutorial and is best thiszZ"
print(string32.replace('is', 'bound'))
#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%






