import os
import pathlib

# file = open('name.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# with open('name.txt', 'r') as f:
#     content = f.read()
#     print(content)

# with open('name.txt', 'w') as f:
#     f.write("VoVo Squad \n")  # Overwrites the file
#     f.write("Writing in the file using Python \n")

# Append mode
# with open('name.txt', 'a') as f:
#     f.write("\nWriting in the file using Python \n")

# lines = ['I am learning Python.\n', 'File handling is easy.\n', 'This is the third line.\n']
# with open('name.txt', 'a') as f:
#     f.writelines(lines)

# with open('name.txt', 'r') as f:
#     content = f.read()
#     print(content)

#-----------------------------Existence of a file-------------------------------------

if os.path.exists('test.txt'):
    print("The file exists.")
else:
    print("The file does not exist.")


file_path = pathlib.Path('name.txt')
if file_path.exists():
    print("The file exists.")
else:
    print("The file does not exist.")

print(os.path.abspath('name.txt'))  # Get absolute path of the file
print(os.path.getsize('name.txt'))  # Get size of the file in bytes

with open('name.txt', 'r') as f:
    print(f.tell())  # Current position of the cursor
    print(f.read(10))  # Read first 10 characters