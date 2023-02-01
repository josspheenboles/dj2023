l=['ahmed',"fatam"]
inputlist=input('enter list of names')
print(inputlist,type(inputlist))
inputlist=(inputlist.replace('[','').replace(']','').replace('"','').replace("'",'').split(','))
dnames={}
for name in inputlist:
    dnames[name[0]]=[name]
print(dnames)