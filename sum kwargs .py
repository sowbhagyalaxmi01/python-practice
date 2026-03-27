def sum_values(**kwargs):
    total = 0
    for value in kwargs.values():
        total += value
    return total

print(sum_values(a=10, b=20, c=30))