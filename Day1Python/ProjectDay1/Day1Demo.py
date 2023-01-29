for x in range(5):#[0,1,2,3,4]
    if(x==2):
        continue
    else:
        print(x)
x=input('enter x')
"""

for x in range(5):#[0,1,2,3,4]
    if(x==2):
        continue
    print(x)
else:
    #line interprted if for loop done
    print('database backup done')

for x in range(0,10,1):#loop 10 times
    if(x==5):
        continue#break loop5
        #break #loop till loop5
    print(x)

#while(conditio):
    #


#colection of numbers
#range([start=0],end,[step=1])-->range(0,11,1)
r=range(0,11,1)#[0,1,2,3....,10]
r=range(0,11)#step===>1 [0,1,2,3....,10]
r=range(11)#start==>0 ,step===>1 [0,1,2,3....,10]
print(r,type(r))
for number in r:
    print(number)

name='ahmed ali'#collection of letter
count=0
for varx in name:
    print(varx,count)
    count+=1

x=2
if(x==3):
    print('three')
elif(x==2):
    print('two')
else:
    print('another number')


if(x==3):
    print('three')
else:
    if(x==2):
        print('two')
    else:
        print('anothe number')
if(x==3):
    print('three')
elif(x==2):
    print('two')
else:
    print('another number')
#if(condition):
    #
#elif(condition):
    #
#elif(condition):
    #
#elif(condition):
    #
#else:
    #
# and first flase,---->last True
#or first true,====>last false
print(2 and 5)#val and val-->True and True -->5
print(0 and 2)#False--->0

print(2 or 5)#val or val-->True or True -->2
print(0 or 2)#False--->2
print('' or 0 or 5)#5


print(True and True and True)
print(True and False and True)
print(True or False or True)
print(False or True or False)



print(2<5)

age=10
age+=2#12
age-=2#10
age*=2#20
age/=2#10
age%=2#0
age=9
age//=2#4
age**=2
print(age)



print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(9%2)
print(9//2,9/2)
print(2**8)

age='ten'#str
print(type(int(age)))


age=10 #define datatype
print(type(age))
age='ten'
print(type(age))
age=10.5
print(type(age))
age=False
print(type(age))
age=1+2j
print(type(age))
x=input('enter num')
print(type(x))

#single line of string
name="ahmed ali"
name='ahmed ali'

#multi line string
bio='''my name is ahmed ali
my job is django developer'''
print(bio)

#python casesensetive
var1='1'
_Var1=2
#reserverd word
#if=1
#indentaion using tab
if(True):
    print('1')
    print('2')
"""