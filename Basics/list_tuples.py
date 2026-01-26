my_list = [1, 2, 3, "Shanto", "Pranto", 8.9]

print(my_list)

# list is mutable
my_list[2] = 100
print(my_list)
print(my_list[-1])
print(len(my_list))

# s = "Shanto" --> "S", "h", "a", "n", "t", "o"

s = "Shanto"
print(list(s))

# Adding elements to a list
my_list.append("Hemel")
print(my_list)

print(my_list.index("Shanto"))
my_list.reverse()
print(my_list)

# tuple() ---> immutable
my_tuple = (1, 2, 3)
print(my_tuple)
# my_tuple[1] = 100  # This will raise an error
new_tuple = (4, 5)
my_tuple += new_tuple
print(my_tuple)

# Reverse a tuple
reversed_tuple = tuple(reversed(my_tuple))
print(reversed_tuple)