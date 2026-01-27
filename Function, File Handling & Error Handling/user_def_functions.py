# User Defined Functions
# ---------------------------
# 1. No Input, No Return -> def function_name(): ...

def my_first_function(): # Function Definition
    a = 10
    b = 20
    c = a + b
    print(f"Sum: {c}")

my_first_function() # Function Call

# ---------------------------
print("-------------------------------------------")
# 2. Input, No Return -> def function_name(param1, param2): ...

def add_two_numbers(num1, num2): # arguments
    result = num1 + num2
    print(f"Addition: {result}")

# a = input("Enter first number: ")
# b = input("Enter second number: ")

# add_two_numbers(int(a), int(b))
add_two_numbers(2, 3) # parameters

# ---------------------------
print("-------------------------------------------")
# 3. Input, Return -> def function_name(param1, param2): ... return value

# If a function returns a value, we can store it in a variable or use it directly

def multiply_two_numbers(num1, num2):
    result = num1 * num2
    return result

result = multiply_two_numbers(4, 5)
print(f"Multiplication: {result}")

# ---------------------------
print("-------------------------------------------")
# 4. No Input, Return -> def function_name(): ... return value
def get_greeting_message():
    message = "Hello from the function!"
    return message

greet_msg = get_greeting_message()
print(greet_msg)