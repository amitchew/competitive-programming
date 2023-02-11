
num = int(input())
 
for _ in range(num):
    inp = int(input())
    inp2 = input()
    l = 0
    r = inp - 1
    while l < r:
        if (inp2[l] == "0" and inp2[r] == "1") or (inp2[l] == "1" and inp2[r] == "0"):
            l += 1
            r -= 1
            continue
 
        break
 
    print(r - l + 1)
