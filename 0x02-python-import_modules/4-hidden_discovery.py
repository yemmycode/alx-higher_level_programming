import dis
import marshal

def extract_names_from_pyc(pyc_file):
    """
    Extracts names from a compiled Python module (.pyc file).
    """
    with open(pyc_file, 'rb') as f:
        magic_number = f.read(4)  # Read the magic number
        timestamp = f.read(4)     # Read the timestamp
        code_object = marshal.load(f)  # Load the code object

    # Disassemble the code object to extract names
    instructions = dis.get_instructions(code_object)
    names = set()
    for instr in instructions:
        if instr.opname == 'LOAD_CONST':
            const = code_object.co_consts[instr.arg]
            if isinstance(const, str) and not const.startswith('__'):
                names.add(const)

    return sorted(names)

if __name__ == '__main__':
    pyc_filename = 'hidden_4.pyc'  # Provide the path to your hidden_4.pyc file
    extracted_names = extract_names_from_pyc(pyc_filename)

    for name in extracted_names:
        print(name)
