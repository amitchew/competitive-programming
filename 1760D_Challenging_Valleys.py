for _ in range(int(input())):
    n = int(input())
    liss = list(map(int, input().split()))
    result = "YES"
    vall = 0
    for i in range(1, n):
        if vall and liss[i] < liss[i-1]:
            result = "NO"
            break
        if vall == 0 and liss[i] > liss[i-1]:
            vall = 1
    print(result)
