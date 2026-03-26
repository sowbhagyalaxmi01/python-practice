def reverse_list(lst):
    """
    Function to reverse a list
    """
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# Example usage
print(reverse_list([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]