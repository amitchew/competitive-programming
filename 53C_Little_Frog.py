n=int(input())
j=1
k=n
for i in range(n):
    if i%2 ==0:
        print(j,end=" ")
        j +=1
    else:
        print(k,end=" ")
        k-=1
print("")
