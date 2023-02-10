nums=int(input())
for l in range(nums):
    
    n=int(input())
    t=0
    s=0
    for i in input().split():
        i=int(i)
        
        if t*i>0:
            t=max(t, i)
        else:
            s+=t
            t=i
        
    print(s+t)
