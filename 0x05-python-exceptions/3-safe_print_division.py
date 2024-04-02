#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    except TypeError:
        print("Inside result: Both inputs must be integers.")
        return None
    else:
        print("Inside result: {:.2f}".format(result))
        return result
    finally:
        print("Inside result: Done processing.")
