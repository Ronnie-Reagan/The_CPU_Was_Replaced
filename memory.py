from utils import goto
from registers import read_register, write_register

ROM_ORIGIN = (0, 0)
RAM_ORIGIN = (0, 10)
BITS = {
    0: Entities.Grass,
    1: Entities.Bush
}

def read_bit(x, y):
    goto((x, y))
    return 1 if get_entity_type() == Entities.Bush else 0

def write_bit(x, y, value):
    goto((x, y))
    plant(BITS[value])

def read_byte(origin):
    value = 0
    for i in range(8):
        x, y = origin[0] + i, origin[1]
        value |= read_bit(x, y) << (7 - i)
    return value

def write_byte(origin, val):
    for i in range(8):
        x, y = origin[0] + i, origin[1]
        bit = (val >> (7 - i)) & 1
        write_bit(x, y, bit)

def fetch_instruction(index):
    row = ROM_ORIGIN[1] + index
    return read_byte((ROM_ORIGIN[0], row))

def decode_instruction(byte):
    opcode = (byte >> 4) & 0b1111
    regA = (byte >> 2) & 0b11
    regB = byte & 0b11
    return opcode, regA, regB
