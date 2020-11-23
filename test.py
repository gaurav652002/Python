a=int(input("number here"))
list=[]
listr=[]
for i in range(1,a+1):
    list.append(i)
print(list)
for i in range(1,len(list)+1):
    listr.append(list.pop())
    print(list)
    print(listr)
print(list)
print(listr)
