n = int(input())

count = 0

while 1:
    if n == 0:
        print(count)
        break
    if n < 0:
        print(-1)
        break
    if n%5 == 0:
        count+=n//5
        print(count)
        break
    else:
        n -= 3
        count +=1