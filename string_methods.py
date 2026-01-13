name_one = "rahim"

print(name_one.title())  # Output: Rahim
print(name_one)

name_one = name_one.title()
print(name_one)  # Output: Rahim

print(name_one.upper())  # Output: RAHIM
print(name_one.lower())  # Output: rahim
print(name_one.swapcase())  # Output: rAHIM

fruit = "banana"
print(fruit)
print(fruit.count("n"))  # Output: 2

fruit = fruit.replace("banana", "orange")
print(fruit)  # Output: orange
print(fruit.count("o"))  # Output: 1