n = int(input())

for i in range(n + 1):
    power = 2 ** i
    if power > n:
        print(2 ** i)
        break
