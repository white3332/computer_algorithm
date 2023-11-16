def merge_nested_lists(nested_list):
    return [item for sublist in nested_list for item in sublist]

nested_list = [[1, 8], [3, 7]]
merged_list = [merge_nested_lists(nested_list)]
print(merged_list)