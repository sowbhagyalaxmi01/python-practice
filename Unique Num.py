arr = [1,2,2,3,4,4,5]

unique = set()

for num in arr:
    if arr.count(num) == 1:
        unique.add(num)

print(unique)