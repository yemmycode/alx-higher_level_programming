#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []  
    try:
        for i in range(list_length):
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result.append(0) 
            else:
                try:
                    division_result = my_list_1[i] / my_list_2[i]
                    result.append(division_result)
                except ZeroDivisionError:
                    print("division by 0")
                    result.append(0)  
                except (TypeError, ValueError):
                    print("wrong type")
                    result.append(0) 
    finally:
        return result
