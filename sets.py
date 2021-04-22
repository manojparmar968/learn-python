s = set()
# print(type(s))
s = {1,2,3,5,3,2}
s.add(4)
s.update([6,7])
s.update([4,5],{6,8})

# remove element
s.discard(7)

# remove gives error if element not presernt in set
# s.remove(9) 

s.pop()
# print("s = ",s)

A = {1,2,3,}
B = {3,4,5,}

# union
# print(A.union(B))
# print(B.union(A))

# intersection
# print(A.intersection(B))
# print(B.intersection(A))

# diffrence
# print(A.difference(B))
# print(B.difference(A))

# symmetric diffrence
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))



