# Check if a number is positive, negative, or zero

num = int(input("Enter a number:"))

if num > 0:
    print("The {} is positive.".format(num))
elif num == 0:
    print("The {} is zero.".format(num))
else:
    print("The {} is negative.".format(num))


name = str(input("Enter Your name: "))
print(f"Hey! I am {name}")