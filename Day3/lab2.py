name='global'
def final():
    name='final'
    def outer():
        #name='outer'
        def innert():
            global name
            print(name)#outer
            name='test'
            print(name)  # outer
        innert()
        print(name)#global
    outer()
final()
print(name)#test
'''

def Area(shapename, dim1, dim2=0):
    if (shapename == 't'):
        return 0.5 * dim2 * dim1
    elif (shapename == 'r'):
        return dim1 * dim2
    elif (shapename == 'c'):
        return 3.14 * dim1 ** 2
    elif (shapename == 's'):
        return dim1 * dim1
    else:
        return 'invalid shape'

#calling Area
print(Area('c', 10))

shape = input("""enter Shape name:
t for triangle
c for circle
r for rectangle
s for squar""")
dim1 = float(input('enter dim1'))
if (shape == 't' or shape == 'r'):
    dim2 = float(input('enter dim2'))
    print(Area(shape, dim1, dim2))
else:
    print(Area(shape, dim1))

#global scope
x='aya ali'
i=1#var1 i
for i in x: #var2 i
    print(i)
'''
