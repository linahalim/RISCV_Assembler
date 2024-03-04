OPCODES = {
    "BEQ": "110",
    "BNE": "111"
}

# converter decimal to binary
def dec_to_bin(n, length):
    return format(n, 'b').zfill(length)

# converter binary to hexadecimal
def bin_to_hex(binary_string):
    hex_string = hex(int(binary_string, 2))[2:].zfill(len(binary_string) // 4)
    return hex_string

# Assemble function
def assemble(instruction):
    parts = instruction.split()
    opcode = OPCODES.get(parts[0], None)
    if opcode:
        # Branch instructions
        if parts[0] in ["BEQ", "BNE"]:
            rs1 = dec_to_bin(int(parts[1][1:].replace(",", "")), 5)
            rs2 = dec_to_bin(int(parts[2][1:].replace(",", "")), 5)
            imm = dec_to_bin(int(parts[3]), 12)
            machine_code_binary = opcode + rs1 + rs2 + imm
            return bin_to_hex(machine_code_binary)
    return None

instruction = "BEQ x1, x2, 4"
machine_code = assemble(instruction)
print("Instruction:", instruction)
# Expected output: 0x00208463
print("Generated machine code:", machine_code)
