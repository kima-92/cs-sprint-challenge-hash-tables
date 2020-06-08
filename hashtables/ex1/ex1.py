

def get_indices_of_item_weights(weights, length, limit):
    # limit - package's wait limit
    # weigts - an array of items weigts
    # length - len(weigts)

    answer = ()
    weights_dict = {}

    # For each index in weight
    for i in range(0, length):
        # Store current weight
        weight = weights[i]

        # Get the needed weight
        needed_weight = limit - weight
        
        # If needed_weight is in the weights_dict
        if needed_weight in weights_dict:

            # Save the index of needed_weight
            needed_index = weights_dict[needed_weight]

            # If the index of weight is GREATER than the index of weights_dict[needed_weight]
            if i > needed_index:
                high = i  # weight
                low = needed_index  # weights_dict[limit - weight]

                answer = (high, low)
            # Else: If the index of weight is LESS than the index of weights_dict[needed_weight]
            else:
                low = i  # weight
                high = needed_index  # weights_dict[limit - weight]

                answer = (high, low)

        # Save this weight in the weights_dict,
        #  with it's index as the value
        weights_dict[weight] = i

    # Return answer (touple) (0,1)

    # If we got an answer, return answer
    if answer != ():
        return answer
    # If not, return None
    return None
