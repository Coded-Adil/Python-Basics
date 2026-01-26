list_1 = [1, 2, 3, 4, 5]
result = 0

i = 0
n = len(list_1)

while i<n:
    result += list_1[i]
    i += 1

print("Sum using while loop:", result)

#-------------------------------------------------------------------

list_2 = [-10, 2, 19, -3, -5] # Output should be [0, 2, 19, 0, 0]

i = 0
new_list = []
n = len(list_2)

while i<n:
    if list_2[i] < 0:
        list_2[i] = 0
    i += 1

print("Modified list using while loop:", list_2)