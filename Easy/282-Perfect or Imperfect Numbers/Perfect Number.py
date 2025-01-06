number = int(input())
list1 = []
for i in range(1, number):
    if number % i == 0:
        list1.append(i)

if sum(list1) == number:
    print('YES')
else:
    print('NO')
