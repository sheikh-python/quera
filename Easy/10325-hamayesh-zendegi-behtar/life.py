r , c = input().split()

radif = abs(int(r)-11)

if 0<int(c)<=10:
    cton = int(c)
else:
    cton = abs(int(c)-21)
    
if 0 < int(c) <= 10 :
    print(f'Right {radif} {cton}')
else:
    print(f'left {radif} {cton}')
