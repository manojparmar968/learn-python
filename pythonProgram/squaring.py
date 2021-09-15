num = int(input("enter a number: "))
sum_of_square = 0
sum_of_cube = 0
for i in range(1,num+1):
    sum_of_square = sum_of_square+i**2
print(sum_of_square)

for i in range(1,num+1):
    sum_of_cube = sum_of_cube+i*3
print(sum_of_cube)