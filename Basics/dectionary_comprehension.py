nums = list(range(1, 11)) # 10 values from 1 to 10

result = {i: "Even" if i % 2 == 0 else "Odd" for i in nums}

print(result)