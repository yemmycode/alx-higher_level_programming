#!/usr/bin/python3

def remove_char_at(input_str, index):
    if index < 0:
        return input_str
    return input_str[:index] + input_str[index+1:]
