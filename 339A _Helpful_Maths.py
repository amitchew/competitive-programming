num=input()
out=[]

intt=num.split("+")
intt.sort()


for i in range(len(intt)-1):
    out.append(f'{intt[i]}+')
    
out.append(f'{intt[-1]}')
print(*out,sep='')
