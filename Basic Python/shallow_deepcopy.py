# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# new_list = old_list

# new_list[2][2] = 9

# print('old_list', old_list)
# print('ID of old list',id(old_list))

# print('new_list', new_list)
# print('ID of new list',id(new_list))

# Shallo copy

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])
old_list[1][1] = 'AA'

print("Old list:", old_list)
print('ID of old list',id(old_list))

print("New list:", new_list)
print('ID of new list',id(new_list))

# Deep Copy

import copy

# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.deepcopy(old_list)

# old_list[1][0] = 'BB'

# print("Old list:", old_list)
# print("New list:", new_list)