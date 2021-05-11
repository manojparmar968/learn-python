"""
Write a Python program that creates and print a dictionary that maps each element in a list to its corresponding frequency (how many times it occurs in the list).

The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a".
"""

l = ["a","b","a","c","a","c"]
freq_Dict = {}

for elem in l:
    if elem not in freq_Dict:
        freq_Dict[elem] = 1
    else:
        freq_Dict[elem] += 1
print(freq_Dict)