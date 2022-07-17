tc = int(input())
for t in range(1, tc+1):
    CC = ""
    N = int(input())
    for i in range(N):
        Ci, Ki = input().split()
        Ki = int(Ki)
        CC += Ci * Ki
    print('#{}'.format(t))
    for i in range(len(CC)):
        if (i+1)%10 == 0:
            print(CC[i])
        else:
            print(CC[i], end="")
    print()