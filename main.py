from memory import fetch_instruction, decode_instruction
from registers import read_register, write_register
from alu import execute
from ascii_table import ascii_table
from programs.hello_world import PROGRAM_LENGTH

pc = 0  # program counter

def run():
    # Run the loaded program starting at pc
    global pc
    while pc < PROGRAM_LENGTH:
        instr = fetch_instruction(pc)
        opcode, regA, regB = decode_instruction(instr)
        halt, new_pc = execute(opcode, regA, regB)
        if halt:
            break
        if new_pc is not None:
            pc = new_pc
        else:
            pc += 1
