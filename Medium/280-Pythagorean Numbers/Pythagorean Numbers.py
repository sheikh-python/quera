z1 = int(input())
z2 = int(input())
z3 = int(input())

if z3**2 == z2**2 + z1**2 or z1**2 == z2**2 + z3**2 or z2**2 == z3**2 + z1**2:
    print('YES')
else:
    print('NO')

