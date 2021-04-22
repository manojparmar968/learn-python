
# for i in range(len(numbers)):
#     if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
#         numbers[i] = 'fizzbuzz'
#     elif numbers[i] % 3 == 0:
#         numbers[i] = 'fizz'
#     elif numbers[i] % 5 == 0:
#         numbers[i] = 'buzz'

for i in range(1,40+1):
    if i % 5 == 0 or i % 10 == 0:
        i = 'tom'
    elif (i % 7 == 0) or (i % 14 == 0):
        i = "cat"
    
    print(i)