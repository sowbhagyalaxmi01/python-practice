lst = [1, 2, 2, 3, 1, 4]

seen = set()
result = []

for i in lst:
    if i not in seen:
        seen.add(i)
        result.append(i)

print(result)