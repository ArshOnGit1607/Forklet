def swap_first_last(num):
    N=num
    l=N%10
    count=0
    while N>0:
        f=N%10
        count+=1
        N//=10
    middle_num=num%(10**(count-1))
    middle_num//=10
    result=l*(10**(count-1))+middle_num*10+f
    return(result)
