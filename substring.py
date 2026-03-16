# Program to check whether the word "python" appears in a user-entered string (case-insensitive)

text = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison
if "python" in text.lower():
    print("The word 'python' appears in the string.")
else:
    print("The word 'python' does not appear in the string.")
