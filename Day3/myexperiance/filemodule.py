#defination functions or vars or class
#no calling ,print in global scope
path='c:\\asd.txt'

def writetofile(path,content):
    print('plppla')
    f=open(path,'w')
    if(f.writable()):
        f.write(content)
    f.close()

def readtofile(path):
    f = open(path, 'r')
    if (f.readable()):
        content=f.read()
    f.close()
    return content

