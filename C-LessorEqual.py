n,k = map(int,input().split())
 
s= list(map(int,input().split()))
 
s.sort()
 
if k==0:
    if s[0]>1:
        print(1)
    else:
        print(-1)
       
elif k==n:
    print(s[-1])
else:
    if s[k]==s[k-1]:
        print(-1)
    else:
        print(s[k-1])
