a = [1, 2, 3, 4, "a", 5, 6, 7]

# break - stops the loop when condition is met
for i in a:
    if type(i) == str:
        break
    else:
        print(i)

print("------------")
# continue - skips the current iteration when condition is met
for i in a:
    if type(i) == str:
        continue
    else:
        print(i)