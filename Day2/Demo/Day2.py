#'{name}'.format(name='asd')
print('test')
def sum(**kargs):
    print(kargs,type(kargs))
    sum=0
    for k in kargs:
        print(k)
        sum+=kargs[k]
    print(sum)
#calling
#sum(x=1,y=3)
#sum(x=1,y=3,z=10)
#sum(x=1)
'''
#min(1,2.......9)
def sum(*args):
    print(args,type(args))
    sum=0
    for x in args:
        sum+=x
    print(sum)
sum(1,2,3,4,6)
sum(1,2,3)

#range(0,12,1) range(0,12) range(12)
#default argument value
def sum(x,y=0,z=1):
    print(x+y+z)
sum(1,2,3)
sum(1,2)
sum(1)

#noinput output
def sum():
    return 2+1
    print('test')
x=sum()
print(x)

#input output
def sum(x,y):
    return x+y
var=sum(1,4)
print(var+3)
print(sum(1,4))


#input no output
def sum(x,y):
    print(x+y)
sum(1,3)
sum()

#defination function
def checkisfigitconverttoint(num):
    if (num.isdigit()):
        num = int(num)
        return  num

num1=(input('enter number1'))
#calling
num1=checkisfigitconverttoint(num1)
num2=int(input('enter number2'))
#calling
num2=checkisfigitconverttoint(num2)
operation=(input('enter operaiotn + - * /'))
if(operation=='+'):
    print(num2+num2)


name='aya ali'
for index,letter in enumerate(name):
    print(index,'has ',letter)
l=1,2,1.1,True,[3,5]
for index,v in enumerate(l):
    print(index,v)

count=0
for letter in name:
    print(letter,count)
    count+=1

#dictionary collection of values different datatypes
#key:value---> key unique
trainee={
    'id':1,
    'GPA':3.4,
    'name':'aya ali',
    'track':32829380932,
    'course':['python oop','postgres','js'],
    'grades':(100,90,80),
    'palpla':'plapsl'
}
trainees={
    '1':{
        'id':123457,
        'track':'web using python',
        'branch':'qena'
    },
    '2':{
        'id':329384093284,
        'track':'iot',
        'branch':'smart'
    },
}
print(trainees['1']['id'])

t=3,4
print(type(t))
x,y=t
print(x,y)
for key,value in trainee.items():
    print(key,value)

print(trainee.keys())
for item in trainee.items():
    print(item[0],item[1])

for value in trainee.values():
    print(value)

for key in trainee:
    print(key,trainee[key])


trainee2={
    'id':3,
    'GPA':3.4,
    'name':'aya ali',
    'track':32829380932,
    'course':['python oop','postgres','js'],
    'grades':(100,90,80),
    'certificate':['redhat1']
}
trainee2.update(trainee)
print(trainee)

trainee['id']=100
trainee['course']='oop using python'
trainee['plapla']='plapla'
print(trainee['course'],type(trainee['course']))

print(trainee,type(trainee))
opensourcelang='shell','python','java','php'
database=('postgres','mysql')
print(opensourcelang+database)
print(database*3)
print(database)
print(opensourcelang)


x=('one')
print(type(x))

x=1,1.1,True,'dsd',[],(),{}
#x[0]='wwkwk'
print(x[-1])

#tuple collection of values different datatypes
#tuple Immutable list
x='one',
print(type(x))

x=(1,1.1,1+2j,True,'asas',[],(),{})
print(x[-1])
print(type(x))

#x[0]='test'
print(x[0])
print(x,type(x))

#list collection of values different datatypes
opensourcelang=['shell','python','java','php']
database=['postgres','mysql']
print(database*2)
print(database)


print(opensourcelang+database)
database.extend(opensourcelang)
print(opensourcelang)
print(database)

x=[1,1.1,1+2j,True,'one',[2,4],(),{}]#empty list

print(x)
var=x.remove(1)
print(var)
#x.remove(1)
#x.remove('php')
print(x)
var=x.pop()
print(var)
var=x.pop()
print(var)
var=x.pop(3)
print(var)
print(x)

x.append('asd')
x.insert(0,'asd')
x.insert(4,False)
print(x)


x[0]='test'
#x[8]='asd'
print(x)
print(x[-1])
#print(x[20])
print(len(x))

for value in x:
    print(value,type(value))

print(x,type(x))

if(x):
    print('True')
else:
    print('false')

name='ahmed ali'
print('A' in name)

x=25
if(x==2):
    print('two')
y='two' if (x==2) else 'not two'
print(y)

#print(val1.....valm,sep=' ',end='\n')
print(1,'one',sep='&',end='===>')
print(3)
print('new line')

x=1
y=3
print(x,y)
x,y=y,x
print(x,y)


temp=x#1
x=y#3
y=temp
#unpacking squ.
var1,var2=1,'one'
print(var1)
print(var2)
w,x,y,z=1.1,2,3.6,3
print(w,x,y,z)
print(min(x,y,z,w,3,5,76,8,-1))
print(max(x,y,z,w,3,5,76,8,-1))
print(round(y))

c=complex(2,3)
print(c)

statment='trainee:{name} have grade={g} {name} passed'
print(statment)
print(statment.format(name='ahmed ali',g=1000))
print(statment.format(g=1000,name='aya ali'))

statment='trainee:{} have grade={}'
print(statment)
print(statment.format('ahmed ali',100))
print(statment.format(100,'aya ali'))
name='ahmed ali'
username=name.split(' ')[0]
password=name.replace('a','@',3)
print(username,password)

s='sasasa'
print(s[s.index('a')+1:])
print(s.index('a'),s[s.index('a')+1:])

num=(input('enter num'))
if(num.isdigit()):
    num=int(num)
else:
    print('number must be digit')

name='ahmed ali'#collection of letters
print(name.capitalize())
print(name.lower())
print(name.count('a'))
print(name.index('a'),name[name.index('a')+1:].index('a'))
print(name)

print(name[2])
print(name[1:3]) #[start[0]:end[len of str-1]:step[1]]
print(name[2:])
print(name[:2])
print(name[-2])
print(len(name))
print(name[9])


for x in name:
    print(x)

number=int(input('enter number'))
myrange=range(1,number+1)
for num in myrange:
    print(num*'*')
    
'''