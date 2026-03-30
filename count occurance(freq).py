num=[1,2,4,5,2,4,3,2,8]
print(num.count(2))
print(num.count(4))
print(num.count(1))



nums = [1, 2, 2, 3, 3, 3]
for i in set(nums):
    print(i, "=", nums.count(i))



    numbers = [1, 2, 2, 3, 4, 3, 3]
freq = {}
for n in numbers:
    freq[n] = freq.get(n, 0) + 1
print(freq)


fruits = ["apple", "banana", "apple", "cherry"]
print(fruits.count("apple"))
