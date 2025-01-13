n = list(input())
n = list(map(lambda x:int(x),n))
n = str(sum(n))
while len(n)!=1:
    n = list(map(lambda x:int(x),n))
    n = str(sum(n))
print(int(n))