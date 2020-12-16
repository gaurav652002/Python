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
    n_tive=a/le
    p_tive=b/le
    z_r=c/le