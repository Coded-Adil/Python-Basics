def my_function(f_name, l_name, age):
    print(f"My name is {f_name} {l_name} and I am {age} years old.")

# my_function("Adil", "Rahman", 24)
# my_function("Adil", 24, "Rahman") # Wrong order will give incorrect result
my_function(age=24, l_name="Rahman", f_name="Adil")  # Using key arguments to pass values in any order


#------------------------------------------------------------------
print("-----------------------------------------")

# Arbitary Number of Key Arguments
# def new_function(**data): # data and kwargs are commonly used names
def new_function(**kwargs):
    print(kwargs)  # kwargs is a dictionary
    print(f"My name is {kwargs['name']}, I am {kwargs['age']} years old, I live in {kwargs['city']}, and my id is {kwargs['id']}.")

new_function(name="Adil", age=24, city="Tokyo", id=222010276)
