#!/usr/bin/python3

def safe_print_division(a, b):
    div_result = 0

    try:
        div_result = a/b
    except (ZeroDivisionError, TypeError):
        return None
    finally:
        try:
            print("Inside result: {}".format(div_result))
        except NameError:
            pass

    return div_result
