
def flatten(nested_list):
    flattened = []
    for element in nested_list:
        if isinstance(element, list):
            flattened.extend(flatten(element))
        else:
            flattened.append(element)
    return flattened

nested_list = [[[2, 2, 3, 4], [2323, 12], 2]]
flattened_list = flatten(nested_list)
print(flattened_list)