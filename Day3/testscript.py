l=input('enter ')
'''
import sys
try:
    float('s')
except:
    print(sys.exc_info())


import re
email='asd@yahoo.com'#input('enter your email')
pattern='([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
print(re.match(pattern,email))
print(re.search(pattern,email))
print(re.fullmatch(pattern,email))

from math import *
print(pi)


from os import *
print(getcwd())
print(system('dir'))
#system('cd myexperiance')
chdir('myexperiance')

print(system('dir'))

from myexperiance.filemodule import path,readtofile
print(path)
print(readtofile('asd.py'))
from myexperiance.databases.postgresdb import select
select('s')


import myexperiance.filemodule
import myexperiance.databases.postgresdb 
print(myexperiance.databases.postgresdb.host)
myexperiance.databases.postgresdb.select('select * from user')



from myexperiance.filemodule import readtofile as seperatedfuncreadinmodule

def readtofile():
    print('test')

readtofile()

seperatedfuncreadinmodule('asd.py')

import filemodule
print(filemodule.path)
content=filemodule.readtofile('asd.py')
print(content)
'''