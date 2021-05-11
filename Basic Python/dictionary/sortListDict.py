"""
Write a Python program that sorts (in ascending order) the lists contained as values in a dictionary.

The dictionary contains key-value pairs that match strings to lists. You need to sort these lists.

The lists have to be mutated (changed).

Notice how all the lists are now sorted in ascending order.

🔸 Hints:
The .sort() method sorts a list (the list is mutated/changed).

Be careful with using sorted() because it only returns a sorted copy of the list.
"""

my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}

for i in my_dict.values():
    i.sort()
print(my_dict)