#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    list_sum = 0

    for elements in uniq_list:
        list_sum += elements

    return list_sum
