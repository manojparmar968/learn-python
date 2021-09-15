"""
Count All The 2 From given array
"""
arr=[1,2,2,3,4,5,6,2,7,8,9,2,8]
count = 0
match = 2

for i in range(len(arr)):
    if arr[i] == match:
        count = count+1
print("count",count)