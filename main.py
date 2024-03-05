OPCODES = {
   "BEQ": "110",
   "BNE": "111"
}

#global vars
R_type_opcodes = {
     "ADD": {"opcode": "0110011", "funct3": "000", "funct7": "0000000"},
     "MUL": {"opcode": "0110011", "funct3": "000", "funct7": "0000001"},
     "SLL": {"opcode": "0110011", "funct3": "001", "funct7": "0000000"},
     "SRL": {"opcode": "0110011", "funct3": "101", "funct7": "0000000"},
     "XOR": {"opcode": "0110011", "funct3": "100", "funct7": "0000000"},
}


I_type_opcodes = {
    "ADDI": {"opcode": "0010011", "funct3": "000"},
    "ORI": {"opcode": "0010011", "funct3": "110"},
    "ANDI": {"opcode": "0010011", "funct3": "111"},
    "SLLI": {"opcode": "0010011", "funct3": "001", "end": "0000000"},
    "SRLI": {"opcode": "0010011", "funct3": "101", "end": "0000000"},
}

B_type_opcodes = {
    "beq": {"opcode": "1100011", "funct3": "000"},
    "bne": {"opcode": "1100011", "funct3": "001"},
}

#NOT DONE
register_mapping = {
    "zero": 0, "x0": 0,
    "ra": 1, "x1": 1,
    "sp": 2, "x2": 2,
    # ...
    "a0": 10, "x10": 10,
    "a1": 11, "x11": 11,
    # ...
    "s0": 8, "x8": 8,
    "s1": 9, "x9": 9,
    # ...
    "x31": 31
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

    
    if opcode in R_type_opcodes:
        opcode_binary = R_type_opcodes[opcode]["opcode"]
        rd_binary = register_name_to_binary(parts[1])
        rs1_binary = register_name_to_binary(parts[2])
        rs2_binary = register_name_to_binary(parts[3])
        funct3_binary = R_type_opcodes[opcode]["funct3"]
        funct7_binary = R_type_opcodes[opcode]["funct7"]
    
    #full binary instruction for R-type
        binary_instruction = funct7_binary + rs2_binary + rs1_binary + funct3_binary + rd_binary + opcode_binary
        return bin_to_hex(binary_instruction)

    elif opcode in I_type_opcodes:
        opcode_binary = I_type_opcodes[opcode]["opcode"]
        rd_binary = register_name_to_binary(parts[1])
        rs1_binary = register_name_to_binary(parts[2])
        immediate = format(int(parts[3]), '012b')  # assuming the immediate value fits in 12 bits
        funct3_binary = I_type_opcodes[opcode]["funct3"]
    
    #full binary instruction for I-type
        binary_instruction = immediate + rs1_binary + funct3_binary + rd_binary + opcode_binary
        return bin_to_hex(binary_instruction)
    elif opcode in B_type_opcodes:
        # Branch instructions
        if parts[0] in ["BEQ", "BNE"]:
            rs1 = dec_to_bin(int(parts[1][1:].replace(",", "")), 5)
            rs2 = dec_to_bin(int(parts[2][1:].replace(",", "")), 5)
            imm = dec_to_bin(int(parts[3]), 12)
            machine_code_binary = opcode + rs1 + rs2 + imm
            return bin_to_hex(machine_code_binary)
        else:
            print("Unsupported instruction:", opcode)
        return None
    
    
    
instruction = "BEQ x1, x2, 4"
machine_code = assemble(instruction)
print("Instruction:", instruction)
# Expected output: 0x00208463
print("Generated machine code:", machine_code)
