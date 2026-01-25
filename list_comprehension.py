a = [1, 10, 23, 24, 26, 90]

result = []

# Normal way
for i in a:
    if i % 2 == 0:
        result.append(i)

print(result)

# List comprehension way
new_result = [i for i in a if i % 2 == 0]
print(new_result)

# -------------------------------------------------------------------
b = [1, 2, 3, 4, 5] # Output should be [1, 4, 3, 16, 5]

# Normal way
b_new = []

for i in b:
    if i % 2 == 0:
        b_new.append(i**2)
    else:
        b_new.append(i)

print(b_new)

# List comprehension way
b_squared_even = [i**2 if i % 2 == 0 else i for i in b]
print(b_squared_even)