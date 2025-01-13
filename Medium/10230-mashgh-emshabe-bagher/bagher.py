x = [int(i) for i in input().split()]

if 0 not in x:
    if sum(x)==180:
        print('Yes')
    else:
        print('No')
else:
    print('No')
