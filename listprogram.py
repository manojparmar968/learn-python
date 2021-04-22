# l = ['a','b','c','d','e','f','g','h']
l = [1,2,3,8,9,5,7,6,4]

# count a total number

# n = 123654
# count = 0
# while(n>0):
#     count += 1
#     n = n//10
#     # print("l = ",l)
# print("total number of digits", count)

# count even and odd from given list

even = 0
odd = 0
for x in l:
    if x%2 == 0:
        even += 1
    else:
        odd += 1
print("Total even number ", even," Total odd number ", odd)
