def plusminus(arr):
    le=len(arr)
    a=0
    b=0
    c=0
    le= len(arr)
    for i in arr:
        if i <0:
            a +=1
        if i>0:
            b +=1
        if i==0:
            c +=1
    ntive=a/le
    ptive=b/le
    zr=c/le
    print(ntive)
    print(ptive)
    print(zr)
    

arr = []
n=int(input('please enter the number of elements in the array:'))
for i in range(n):
    elemnt=int(input())

    arr.append(elemnt)

plusminus(arr)