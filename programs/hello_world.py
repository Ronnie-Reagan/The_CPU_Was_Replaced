# You will plant these values manually in ROM coordinates (0,0) to (0,12)
# Each is an 8-bit instruction line encoded left to right as crops

PROGRAM = [
    0b00010100,  # LOAD R1, R0  (R0 contains RAM index 0)
    0b01100001,  # PRINT R1
    0b00010100,  # LOAD R1, R0  (repeat to simulate HELLO)
    0b01100001,  # PRINT R1
    # ...
    0b01110000   # HALT
]

PROGRAM_LENGTH = len(PROGRAM)
