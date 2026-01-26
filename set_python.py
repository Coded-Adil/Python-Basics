# {}
# Unordered Set --> indexing not supported
# immutable
# No duplicate values allowed

a = [1, 2, 2, 3, 4, 4, 4, 5]

s = set(a)
# s[0] = 100 # Indexing not supported
# print(s[0])  # This will raise an error
print(s)  # Output: {1, 2, 3, 4, 5}

# ----------------------------------------------------
a = {1, 2, 3}
b = {2, 3, 4}

# Intersection
c = a.intersection(b)
print("Intersection:", c)  # Output: {2, 3}

# Union
d = a.union(b)
print("Union:", d)  # Output: {1, 2, 3, 4}