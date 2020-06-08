

def has_negatives(a):
    result = []
    numbers_dict = {}

    # For each num in a
    for num in a:
        # If the negative of this num is num_dict
        if -num in numbers_dict:
            # Append the absolute number of num to result
            result.append(abs(num))  # Will return it's positive
        else:
            # Add this num to numbers_dict with itself as it's value
            numbers_dict[num] = num


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
