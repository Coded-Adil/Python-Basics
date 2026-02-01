# Error vs Exception

# Error ->> Compile Time -> Syntax Error

# Exception ->> Runtime Error -> Logical, ZeroDivisionError, ValueError, IndexError, TypeError

try: # Code that may raise an exception
    with open('name.txt', 'r') as f:
        print(f.read())
    print(10/2)  # This will raise ZeroDivisionError

    # x = int("abc")  # This will raise ValueError
    x = int("10")  # This will raise ValueError
    print(x)

    a = [1, 2, 3]
    # print(a[5])  # This will raise IndexError

    x = 10  # This will raise NameError
    print(x)

except IndexError:  # Handling specific exception
    print("Error: List index out of range.")
except ValueError:  # Handling specific exception
    print("Error: Invalid value provided.")
except ZeroDivisionError:  # Handling specific exception
    print("Error: You cannot divide a number by zero.")
except FileNotFoundError:  # Handling specific exception
    print("Error: The file was not found. Please check the file path.")
except Exception as e:  # Handling all exceptions
    print("An error occurred:", e)

else:  # Code to run if no exception occurs
    print("All operations were successful.")

finally:  # Code that will run no matter what
    print("Execution completed.")

#------------------------------------------------------------------
print("-----------------------------------------")

# Raising Exceptions Manually
def check_file(filename):
    if not filename.endswith('.txt'):
        print("Only .txt files are allowed.")
    else:
        print("File is valid.")

check_file("document.pdf")
check_file("notes.txt")