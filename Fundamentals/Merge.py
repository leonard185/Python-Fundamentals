def merge_dicts(dict1, dict2):
    # Create a new dictionary to store the merged results
    merged_dict = dict1.copy()  # Start with a copy of dict1
    
    # Iterate through the second dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            # If the key exists in both dictionaries, sum the values
            merged_dict[key] += value
        else:
            # If the key is only in the second dictionary, add it
            merged_dict[key] = value
    
    return merged_dict

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merged = merge_dicts(dict1, dict2)
print(merged)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
