#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        new_list = []
        new_list = my_list[0:idx]
        for num in my_list[3 + 1:]:
            new_list.append(my_list[idx + 1])
        return new_list
