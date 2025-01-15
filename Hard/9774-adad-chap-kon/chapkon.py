num = input()

for i in num:
    if i =='0':
        print("0: ")
    else:
        print(f'{i}: ',end='')
        for j in range(int(i)):
            print(i,end='')
        print()
            
        