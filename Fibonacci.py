myStudes = ["A","B","C","D"]
myLen = len(myStudes)
i=0
while(not(myLen==0)):
    print("Hi",myStudes[i])
    i+=1
    myLen-=1

lineNum=1
for name in myStudes:
    print(lineNum,name)
    lineNum+=1