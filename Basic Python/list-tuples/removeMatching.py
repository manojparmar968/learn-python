"""
Write a Python program that removes all occurrences of the element elem_to_remove from a list.

The output of the program should be the new list with the element removed.

If the element is not found in the list, print the message "Not Found".

If the list is empty, print "Empty List".

Hints:
The list method .remove() only removes the first occurrence of an element in a list.

The program must remove all occurrences of the element from the list.

You can get the number of occurrences of an item with the .count() list method.
"""

s = [3,2,3,1]
element_to_remove = 3

if not s:
    print("Empty List")
elif s.count(element_to_remove) == 0:
    print("Not Found")
else:
    for i in range(s.count(element_to_remove)):
        s.remove(element_to_remove)
print(s)