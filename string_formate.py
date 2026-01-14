user_input = input("Enter your name: ")
print(user_input)
string_one = "Good Morning, {}! How are you?".format(user_input)
print(string_one)

# Another way of formatting
f_name = "Alice"
l_name = "Smith"
age = 30

string_two = "My name is {f_name} {l_name}. I am {age} years old.".format(f_name=f_name, l_name=l_name, age=age)
print(string_two)
string_three = f"My name is {f_name} {l_name} and I am {age} years old."
print(string_three)