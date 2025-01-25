a = int( input())
b = int( input())

out = []

for i in range(a+1,b):
    if i>1 : 
        for j in range(2,i):
            if i%j ==0:
                break
        else:
            out.append(i)
print(*out,sep=',')