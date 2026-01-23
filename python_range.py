# a = range(10)
a = list(range(10))
print(a)            # range(0, 10)

b = tuple(range(10))
print(b)            # range(0, 10)

# range(start, end, sequence)

c = list(range(1, 10, 2))
print(c)            # range(1, 10, 2)

even_till_100 = list(range(0, 101, 2))
print(even_till_100)

reverse_even_till_100 = list(range(100, -1, -2))
print(reverse_even_till_100)