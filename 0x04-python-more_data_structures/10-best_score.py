#!/usr/bin/python3

def best_score(a_dictionary):
    largest_value = 0
    largest_val_key = ""

    if a_dictionary == None:
        return None
    else:
        for key in a_dictionary.keys():
            if a_dictionary[key] > largest_value:
                largest_value = a_dictionary[key]
                largest_val_key = key
            else:
                largest_value = largest_value

    return largest_val_key
