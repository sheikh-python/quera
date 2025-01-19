nums = input().split()
a , b , l = int(nums[0]),int(nums[1]),int(nums[2])

count = 1
sum = 0

while count<=l :
    if count % 2 !=0:
        sum += a
    else:
        sum += b
    count += 1
    
print(sum)