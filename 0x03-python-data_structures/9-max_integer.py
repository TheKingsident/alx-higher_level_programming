#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        largest_num = my_list[0]
        for num in my_list:
            if num > largest_num:
                largest_num = num

    return largest_num
