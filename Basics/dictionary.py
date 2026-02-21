# {}
# Key value pair
# indexing is not possible
# keys are immutable

a = {"rahim": 23, "karim": 24, "fahim": 25, 1: [1, 2, 3, 4], 2: {3, 4, 5}}

print(type(a))

for i in a:
    print(i)

#---------------------------------------------------
print("------------")
for i in a.values():
    print(i)


#---------------------------------------------------
print("------Keys and Values------")
print(a.keys(), a.values())

#---------------------------------------------------
print("------Items------")
for k, v in a.items():
    print(f"key name: {k}, value: {v}")

#---------------------------------------------------
x = [1, 2, 3]
y = ["Mango", "Banana", "Orange"]

# print(list(zip(x, y)))
print(dict(zip(x, y)))

#---------------------------------------------------
b = {"ahan": 23, "farhan": 24, "zahan": 25, 1: [1, 2, 3], 2: {3, 4, 5}}

# print(type(b))   # class dict
for i in b.values():
    print(i)

print("-----------------------------------------")

for i in b:
    print(b.keys(), b.values())