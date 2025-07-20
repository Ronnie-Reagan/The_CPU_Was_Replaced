# Simple program exercising arithmetic operations.
# Demonstrates ADD and SUB instructions.

# Registers:
#   R0 - first operand
#   R1 - second operand
#   R2 - used for intermediate results
#   R3 - unused

PROGRAM = [
    0b00110001,  # ADD R0, R1     -> R0 = R0 + R1
    0b01000010,  # SUB R0, R2     -> R0 = R0 - R2
    0b01110000,  # HALT
]

PROGRAM_LENGTH = len(PROGRAM)

