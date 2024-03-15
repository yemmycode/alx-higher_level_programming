#!/usr/bin/python3
import dis

def print_defined_names(filename):
    with open(filename, 'rb') as file:
        code = file.read()
    instructions = dis.get_instructions(code)
    names = set()
    for instruction in instructions:
        if instruction.opname == 'LOAD_CONST' and type(instruction.argval) == str:
            names.add(instruction.argval)
    for name in sorted(names):
        if not name.startswith('__'):
            print(name)

if __name__ == "__main__":
    print_defined_names('hidden_4.pyc')
