num = [-1,0,1,2,3,5,6]
sum = 3
count = 0

# option 1

# for i in range(len(num)-1):
#     for j in range(i+1,len(num)):
#         if num[i]+num[j] == sum:
#             count += 1
#             print("index at",i,"and",j," = ",num[i]+num[j])
# print(count)

# option 2

# def findsum(num,sum):
#     for i in range(len(num)-1):
#         for j in range(i+1, len(num)):
#             if num[i]+num[j] == sum:
#                 # print("num[i] = ",num[i]," and value of i = ",i)
#                 print("Pair found at index ",i,j," = ")
#                 # return 1
#     # return -1

# findsum(num,sum)

# option 3

def sum_count(num,sum):
    count = 0
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j] == sum:
                count += 1
    return count

print(sum_count(num,sum))