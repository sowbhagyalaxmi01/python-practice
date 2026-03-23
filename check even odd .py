def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(4))  
print(check_even_odd(7))  


def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
print(check_even_odd(3))