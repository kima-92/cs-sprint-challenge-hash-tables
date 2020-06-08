

def intersection(arrays):
    list_of_dicts = []
    result = []

    # For each array
    for l in arrays:
        # Convert the array to dictionary
        d = { i : 1 for i in l }
        # Append the dictionary to list_of_dicts = []
        list_of_dicts.append(d)

    # While there's more than one dictionaryin list_of_dicts
    while (len(list_of_dicts) > 1):

        # Save the last dictionary in list_of_dicts,
        # and remove it from list_of_dicts
        last_dictinary = list_of_dicts.pop()

        # For each key in the last dictionary
        for key in last_dictinary.keys():
            # Grab another dictionary from list_of_dicts
            for another_dict in list_of_dicts:
                # If this key is not in another_dict, and not in the result
                if key in another_dict.keys() and key not in result:
                    # Save it to the result
                    result.append(key)

    # Resturn the result
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
