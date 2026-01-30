# file = open('name.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# Nahidul Islam Prince
# Keranigonj, Dhaka


# Abu Bakkar Siddiq Sazzad
# Uttara, Dhaka


# Raisul Islam Rifat
# Gazipur, Dhaka


# Adil Rahman Srijon
# Mirpur 10, Dhaka

with open('name.txt', 'r') as f:
    content = f.read()
    print(content)

# with open('name.txt', 'w') as f:
#     f.write("VoVo Squad \n")  # Overwrites the file
#     f.write("Writing in the file using Python \n")

# Append mode
with open('name.txt', 'a') as f:
    f.write("\nWriting in the file using Python \n")

lines = ['I am learning Python.\n', 'File handling is easy.\n', 'This is the third line.\n']
with open('name.txt', 'a') as f:
    f.writelines(lines)

with open('name.txt', 'r') as f:
    content = f.read()
    print(content)