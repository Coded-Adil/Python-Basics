# Error vs Exception

# Error ->> Compile Time -> Syntax Error

# Exception ->> Runtime Error -> Logical, ZeroDivisionError, ValueError, IndexError, TypeError

try: # Code that may raise an exception
    with open('data.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:  # Handling specific exception
    print("The file was not found. Please check the file path.")

