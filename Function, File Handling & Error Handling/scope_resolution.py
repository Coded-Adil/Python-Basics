# Scope -> A region where a variable is accessible

x = 10  # Global scope

print("Global scope:", x)  # Output: 10
print("-----------------------------------------")                                                  
def new_function():
    print("Accessing global variable inside function:", x)  # Output: 10
    print("-----------------------------------------")
    y = 5  # Local scope
    print("Local scope:", y)  # Output: 5

new_function()
print("-----------------------------------------")
# print("Trying to access local variable y outside function:", y) # Error: NameError

def another_function():
    x = 100  # Local variable with the same name as global
    print("Inside another_function, local x =", x)  # Output: 100

another_function()

# --------------------------------------------------
# LEGB Rule -> Local, Enclosing, Global, Built-in
# --------------------------------------------------

# global keyword to modify the global variable
# nonlocal keyword to modify the enclosing variable

n = "Global" # Global variable

def outer_function():
    n = "Enclosing"  # Enclosing variable
    def inner_function():
        global n  # Accessing the global variable
        # nonlocal n  # Accessing the enclosing variable
        n = "Local"  # Local variable
        print("Inside inner_function, local n =", n)  # Output: Local
    inner_function()
    print("Inside outer_function, enclosing n =", n)  # Output: Enclosing

outer_function()
print("In global scope, global n =", n)  # Output: Global
print("-----------------------------------------")