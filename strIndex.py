string_one = "This is a string"

# Indexing
# Print the one character
print(string_one[0])  # Output: T
print(string_one[15]) # Output: g
print(string_one[4])  # Output: ' ' (space character)

# Negative Indexing
print(string_one[-16]) # Output: T
print(string_one[-1]) # Output: g

# Length of the string
print(len(string_one)) # Output: 16

# Max_Index = len(string_one) - 1

# last character print
print(string_one[len(string_one) - 1]) # Output: g

### Immutable Nature of Strings
string_two = "Immutable data type"

print(string_two[1])

#string_two[1] = "X"  # This will raise a TypeError: 'str' object does not support item assignment
print(string_two)