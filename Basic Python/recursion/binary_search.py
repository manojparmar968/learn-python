"""
Write a Python program that implements the Binary Search algorithm recursively.

The function should search for an element in a list or sequence and return its index.

If the element is not found, the value returned should be -1.
"""
# option 1

def binary_search(arr,elem):
    low = 0
    high = len(arr)-1
    while(low <= high):
        mid = (low + high) // 2

        if elem > arr[mid]:
            low = mid+1
        elif elem < arr[mid]:
            high = mid-1
        elif elem == arr[mid]:
            return mid
    return -1

arr = [2,15,20,30]
elem = 20

found = binary_search(arr, elem)
if found == -1:
    print("Not Found")
else:
    print("element is present at index",str(found))

# option 2

def bs(seq, low, high, elem):
    if low > high:
        return -1
    else:
        middle = (low + high) // 2

        if elem == seq[middle]:
            return middle
        elif elem < seq[middle]:
            return bs(seq, low, middle - 1, elem)
        else:
            return bs(seq, middle + 1, high, elem)

my_list = [1, 2, 3, 4, 5, 6, 7]
print(bs(my_list, 0, len(my_list), 6))