# 🌾 FarmerCPU — A Crop-Based Virtual CPU in *The Farmer Was Replaced*

FarmerCPU is a spatially-simulated CPU built entirely inside the game world of *The Farmer Was Replaced*. It uses crops to represent binary memory, encodes instructions as fields, and drives execution through your bot’s programmable script.

The goal: to simulate a working 4-bit or 8-bit processor with **RAM, ROM, Registers, ALU, PC**, and console output — without using any dynamic string functions, and with as much logic embedded in the world as possible.

---

## 🧠 Core Concepts

| Concept         | Real CPU Component      | In-Game Equivalent                        |
|-----------------|-------------------------|-------------------------------------------|
| Bit             | Flip-flop               | Crop (Bush = 1, Grass = 0)                |
| Byte            | 8-bit value             | 8 adjacent tiles                          |
| RAM             | Memory                  | Grid of crop-defined bitfields            |
| ROM             | Instruction storage     | Fixed crop layout (read-only)             |
| Register        | Fast-access memory      | Defined memory areas in field             |
| ALU             | Logic unit              | Python logic that reads/writes fields     |
| PC              | Program Counter         | Field marker or script variable           |
| Output          | Terminal                | `quick_print()` with manual ASCII         |
| Clock           | CPU cycle               | Each bot loop iteration                   |

---

## 🧱 Field Layout (Recommended 25×25)

```
ROM:       (0,0) → (15,7)     # 16 instructions × 8 tiles each
REGISTERS: (17,0) → (24,3)    # 4 registers × 4/8-bit wide
RAM:       (0,10) → (15,20)   # 8–16 bytes of general memory
DISPLAY:   (17,10) → (24,15)  # Optional: ASCII or pixel output
```

---

## 🌿 Bit Encoding

### 1-bit Mode

```
Entities.Grass = 0
Entities.Bush  = 1
```

Each tile stores one bit. Crop layouts encode instructions, data, and register values.

---

## 🧾 Instruction Format

Each instruction is 8 bits across 8 horizontal tiles:

```
[ OPCODE (4 bits) ][ REG A (2 bits) ][ REG B or IMM (2 bits) ]
```

| Opcode | Mnemonic | Description             |
|--------|----------|-------------------------|
| 0000   | NOP      | No operation            |
| 0001   | LOAD     | REG A ← MEM[REG B]      |
| 0010   | STORE    | MEM[REG B] ← REG A      |
| 0011   | ADD      | REG A ← REG A + REG B   |
| 0100   | SUB      | REG A ← REG A - REG B   |
| 0101   | JMP      | PC ← REG A              |
| 0110   | CMP      | Compare A and B         |
| 0111   | HALT     | Stop execution          |

---

## 🧪 Bot Execution Cycle

```
while True:
    instruction = memory.read_instruction(pc)
    opcode, a, b = memory.decode(instruction)
    alu.execute(opcode, a, b)
    pc += 1
```

The bot acts as:
- Fetch unit
- Decoder
- ALU
- Bus controller
- Clock

All operations are physically applied to the farm grid.

---

## 🔤 Manual ASCII Table

`chr()` and `str()` are forbidden — simulate output using a fixed table.

```
ascii_table = {
    32: " ", 33: "!", 44: ",", 46: ".",
    72: "H", 87: "W", 100: "d", 101: "e",
    108: "l", 111: "o", 114: "r",
    # Add more as needed
}
```

---

## 🖨️ Output Function

```
def print_string(start_addr, length):
    for i in range(length):
        val = read_memory(start_addr + i)
        if val in ascii_table:
            quick_print(ascii_table[val])
        else:
            quick_print("?")
```

This reads byte values from field memory and prints mapped characters via `quick_print()`.

---

## 📦 Project Structure

```
cpu/
├── main.py             # Main loop (CPU driver)
├── memory.py           # Read/write bit-level field memory
├── alu.py              # Arithmetic logic operations
├── registers.py        # Register access helpers
├── ascii_table.py      # Manual char mapping
├── programs/
│   ├── hello_world.py  # Encoded "HELLO, WORLD!"
│   └── math_test.py    # ALU test program
```

---

## ✅ Features

- ✅ Field-encoded RAM, ROM, and Registers
- ✅ 1-bit physical crop encoding
- ✅ 8-bit instruction pipeline
- ✅ Manual ASCII printing with `quick_print()`
- ✅ Pure spatial simulation — no string ops or cheats

---

## 🚧 Planned

- [ ] Conditional Jumps + Flags
- [ ] Stack pointer + basic function call sim
- [ ] Branching logic
- [ ] ALU extension: AND, OR, XOR, etc.
- [ ] Crop-display ASCII screen

---

## 🧠 Philosophy

This isn’t an emulator *in* code — it's a CPU *built from crops*.

Just like Redstone computers in Minecraft or Logic World, this project is about building computation from primitive, spatial parts. The Python script is merely the control unit walking across a world of bits — the real computer **is the farm**.

---
