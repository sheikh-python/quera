def temp(c):
    if c > 100:
        return 'Steam'
    elif c < 0:
        return 'Ice'
    else:
        return 'Water'


t = int(input())
print(temp(t))
