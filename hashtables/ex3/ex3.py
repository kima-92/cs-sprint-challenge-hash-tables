###########


def intersection(arrays):
    list_of_dicts = []
    result = []

    # For each array
    for current_array in arrays:
        # Convert the array to dictionary
        d = { i : 1 for i in current_array }
        # Append the dictionary to list_of_dicts = []
        list_of_dicts.append(d)

        # If the length od list_of dicts is GREATER then 1
        if len(list_of_dicts) > 1:
            # For each key in current_array
            for key in current_array:
                # If the key is in the first dictionary in list_of_dicts,
                # and it's not in result yet
                if key in list_of_dicts[0] and key not in result:
                    # Append it to result
                    result.append(key)
            # Delete the first dictionary in list_of_dicts
            del list_of_dicts[0]

    # Resturn the result
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
