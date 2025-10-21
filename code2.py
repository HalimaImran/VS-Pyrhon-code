
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
sample_list = [1, 2, 3, 3, 4, 4, 5, 3, 7, 5]
print("Unique List:", unique_elements(sample_list))
