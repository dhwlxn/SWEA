t = int(input())
for i in range(1, t+1):
    num = input().rstrip()
     
    if num == num[::-1]:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')