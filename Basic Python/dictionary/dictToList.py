"""
Write a Python program that takes the content of a dictionary and converts it into a list of lists.

Each nested list should contain a key as the first element and its corresponding value as the second element.

Print the final list of lists.

🔸 Hints:
The .items() dictionary method can be helpful to solve this exercise. 
It returns a sequence with the keys of the dictionary and their corresponding values.
"""

product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}

new_list = []

for key,value in product_info.items():
    new_list.append([key,value])
print(new_list)
