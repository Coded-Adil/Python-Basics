import functools

# Anonymous function -> Unnamed function

def square(x):
    return x * x

print(square(5))  # Output: 25

# Using lambda to create the same function
# Only returns but can not print
# lambda arguments: expression
square = lambda x: x * x

print(square(4))  # Output: 16

# Lambda function to add two numbers
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10

# Sort a list of tuples based on the second element using lambda
students = [("Rahim", 60), ("Karim", 75), ("Salam", 50), ("Jamal", 100)]

sorted_students = sorted(students, key=lambda x: x[1])  # Sort by marks # ascending order
print(sorted_students)

sorted_students_desc = sorted(students, key=lambda x: x[1], reverse=True)  # descending order
print(sorted_students_desc)

# --------------------------------------------------
print("-----------------------------------------")
# map(), filter(), reduce()

# Map
nums = [1, 2, 3, 4]

sq_nums = list(map(lambda x: x*x, nums))
print(sq_nums)  # Output: [1, 4, 9, 16]


# Filter
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4]

# Reduce
sum_nums = functools.reduce(lambda x, y: x + y, nums)
print(sum_nums)  # Output: 10