def game(number):
    number = str(number)
    if int(number[0])>int(number[1]):
        return int(number[0])-int(number[1])
    elif number[1]>(number[0]):
        return int(number[1])-int(number[0])
    else:
        return 0

