#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None or not a_dictionary:
        return None

    largest_val_key = max(a_dictionary, key=a_dictionary.get)
    return largest_val_key
