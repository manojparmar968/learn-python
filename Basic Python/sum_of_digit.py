# Python Program for Sum the digits of a given number

l = [1,2,3,4]
n = 1234
sum = 0

# Using Range Function

# for i in range(0,len(l)+1):
#    sum += i
# print('sum',sum)

# using in function

# for i in str(n):
#     sum += int(i)
# print('sum',sum)

# using while loop

while(n != 0):
    sum += n%10
    n = n//10
print('sum', sum)