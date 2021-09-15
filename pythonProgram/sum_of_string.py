print(ord("a")-96)
print(ord("A")-38)
x = input("enter string: ")
sum = 0
for i in x:
    if ord(i)<97:
        sum = sum+ord(i)-38
    else:
        sum = sum+ord(i)-96
   
print(sum)