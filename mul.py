#Print the multiplication table of 3 (3 × 1 → 3 × 10) using a for loop.

# n=3
# for i in range(1,11):
#     print(n*i)

i=1
while i<=10:
    print(3*i)
    i+=1

    i = 0
while i < 10:
    print(f"3 x {i+1} = {3*(i+1)}")
    i += 1


for i in range(1, 11):
    print(f"3 x {i} = {3*i}")
