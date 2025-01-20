n , m = input().split()

list1 = []
count = 0

for i in range(int(n)):
    x = input()
    if len(x)==int(m):
        list1.append(x)
    else:
        break

for i in list1:
    for char in i:
        if char == '*':
            count += 1

print(count)