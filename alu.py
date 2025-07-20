from registers import read_register, write_register
from memory import read_byte, write_byte, RAM_ORIGIN
from ascii_table import ascii_table

def execute(opcode, regA, regB):
    # Execute a single instruction and return (halt, new_pc)
    if opcode == 0b0000:  # NOP
        return False, None

    elif opcode == 0b0001:  # LOAD
        addr = read_register(regB)
        val = read_byte((RAM_ORIGIN[0], RAM_ORIGIN[1] + addr))
        write_register(regA, val)

    elif opcode == 0b0010:  # STORE
        val = read_register(regA)
        addr = read_register(regB)
        write_byte((RAM_ORIGIN[0], RAM_ORIGIN[1] + addr), val)

    elif opcode == 0b0011:  # ADD
        valA = read_register(regA)
        valB = read_register(regB)
        write_register(regA, (valA + valB) % 256)

    elif opcode == 0b0100:  # SUB
        valA = read_register(regA)
        valB = read_register(regB)
        write_register(regA, (valA - valB) % 256)

    elif opcode == 0b0101:  # JMP
        addr = read_register(regA)
        return False, addr

    elif opcode == 0b0110:  # PRINT
        val = read_register(regA)
        quick_print(ascii_table.get(val, "?"))

    elif opcode == 0b0111:  # HALT
        return True, None

    return False, None
