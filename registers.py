from memory import read_byte, write_byte

REGISTER_BASE = (17, 0)

def register_origin(index):
    return (REGISTER_BASE[0], REGISTER_BASE[1] + index)

def read_register(index):
    return read_byte(register_origin(index))

def write_register(index, val):
    write_byte(register_origin(index), val)
