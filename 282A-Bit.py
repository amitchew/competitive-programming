result = 0
x=int(input())

for i in range(1,x+1):
    if i == 'X++' or i == '++X':
        result = result + 1
    else:
        result = result - 1
        
print(result)
