inp=int(input())
all=[]
lis=[]
for i in range(inp):
    lis.append(input().split(" "))

for i in range(len(lis[0])):
    temp=0
    for j in range(inp):
        temp=temp+int(lis[j][i])
    all.append(temp)
    
if(all[0]==0 and max(all)==0 and min(all)==0):
    print("YES")
else:
    print("NO")
