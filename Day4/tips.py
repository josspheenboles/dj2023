l=['php','python','ruby','r']
it=map(lambda x:x.capitalize(),l)
print(type(it))
print(type(next(it)))
'''
for x in l:
    print(x.capitalize())

def mygen():
    l=[]
    for i in range(5):  # i=0
        l.append(i)
    return l
x=mygen()
it=iter(x)
print(next(it))
print(next(it))





def mygen():
    for i in range(5):#i=0
        yield i
x=(mygen())
print(next(x))
print(next(x))
print(next(x))
print(next(x))

l=['php','python']
lit=iter(l)
print(lit,type(lit))
print(next(lit))
print(next(lit))
print(next(lit))

def summ(y):
    return lambda x:x+y
print(summ(5)(7))


var=lambda x:x+2
print(var)

def sum(x):
    return x+4
print(sum(1))
var=lambda x:x+3
print(var(3))
'''