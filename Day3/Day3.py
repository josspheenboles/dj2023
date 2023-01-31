
"""
f=open('asd.py','w')
#f.write('line1;ine')
if(f.writable()):
    f.write('tst')
    f.writelines(['line1', 'test'])
    if(f.readable()):
        print(f.read())
else:
    print('cannt write in file')
f.close()

f=open('test.txt','w')
#f.write('line1line2')
if(f.writable()):
    f.writelines(['line1\n','line2'])

f.close()

#files
f=open('asd.txt','r')
#content=f.read()
#content=f.readline()
content=f.readlines()
print(content,type(content))
#print(f.readline())
#print(f.readline())
f.close()

#logical ---> debug watch var data type scope
#runtime error-->
import sys
try:
    n1=float(input('enter num1'))#1
    n2=float(input('enter num2'))#2
    sum=(n1+n2)
    print(n1/n2)
except ValueError:
    print('n1 and n2 must be digit')
except ZeroDivisionError:
    print('cannt divid by zero')
except:#generl case
    print(sys.exc_info()[1])
else:
    print('result of sum',n1,'+',n2,'=',sum)
    print('else')
finally:
    print('thank you for using my app')

#handel runtime error using if statment
n1=(input('enter num1'))
if(n1.isdigit()):
    n1=float(n1)
else:
    print('n1 must be digit')
    n1=0
n2=(input('enter num2'))
if(n2.isdigit()):
    n2=float(n1)
else:
    print('n2 must be digit')
    n2=0
print(n1+n2)

#syntax error
print('dddd')
#range()

*x,y,z=2,4
print(x,y,z)

x,y,*z=2,3,4,5,6
print(x,y,z)


name='aya ali'
l=[]
for x in name:
    if(x!='a'):
        l.append(x)
print(l)

print([x for x in name if(x!='a')])
"""