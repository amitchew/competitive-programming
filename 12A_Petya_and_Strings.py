first=input()
second=input()

if(first.upper()==second.upper()):
    print("0")
else:
    for i in range(len(first)):
        if(first[i].upper()>second[i].upper()):
            print('1')
        elif(first[i].upper()<second[i].upper()):
            print(-1)
        
