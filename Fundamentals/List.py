def sort_by_age(list_of_tuples):
    # Use sorted() with a key function to sort by the second item (age) in each tuple
    return sorted(list_of_tuples, key=lambda x: x[1])

# Example usage
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
sorted_people = sort_by_age(people)
print(sorted_people)  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
