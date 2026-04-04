def func(a, *args):
    return a + sum(args)

print(func(5, 1, 2, 3))