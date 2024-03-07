
# Sydney Aronson and Lina Halim collaborated together
# We met up and bounced ideas off of each other. Lina did  the assemble_file method which turned the file into the instructions 
# Lina also did the hex/binary/decimal conversion methods 
# Sydney made the dictionaries that had the different opcodes, register mapping, and register to binary function. 
# Sydney also handled parsing the lines of the files, and doing the R type and I type decoding
# Together, Lina and Sydney worked on the branching part 

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
    "BEQ": {"opcode": "1100011", "funct3": "000"},
    "BNE": {"opcode": "1100011", "funct3": "001"},
}

register_mapping = {
    "zero": 0, "x0": 0,
    "ra": 1, "x1": 1,
    "sp": 2, "x2": 2,
    "gp": 3, "x3": 3,
    "tp": 4, "x4": 4,
    "t0": 5, "x5": 5,
    "t1": 6, "x6":6,
    "t2": 7, "x7":7,
    "s0": 8, "fp":8, "x8":8,
    "s1": 9, "x9": 9,
    "a0": 10, "x10": 10,
    "a1": 11, "x11": 11,
     "a2": 12, "x12": 12,
     "a3": 13, "x13": 13,
     "a4": 14, "x14": 14, 
     "a5": 15, "x15": 15,
     "a6":16, "x16": 16, 
     "a7":17, "x16": 17, 
     "s2":18, "x18": 18,
     "s3":19, "x19": 19,
     "s4":20, "x20": 20,
     "s5":21, "x21": 21,
     "s6":22, "x22": 22,
     "s7":23, "x23": 23,
     "s8":24, "x24": 24,
     "s9":25, "x25": 25,
     "s10":26, "x26": 26,
     "s11":27, "x27": 27,
     "t3":28, "x28": 28,
     "t4":29, "x29": 29,
     "t5":30, "x30": 30,
     "t6":31, "x31": 31,
}

# converter decimal to binary
def dec_to_bin(n, length):
    return format(n, 'b').zfill(length)

def bin_to_hex(binary_string):
    # Converts a binary string to a hex string, padding as necessary
    hex_string = hex(int(binary_string, 2))[2:].zfill(len(binary_string) // 4)
    return hex_string
   
# function to change register name to binary
def register_name_to_binary(name):
    register_number = register_mapping.get(name)
    if register_number is None:
        raise ValueError("Unknown register name: {name}")
    binary_representation = format(register_number, '05b')
    return binary_representation


# Assemble function
def assemble(instruction):
    instruction = instruction.replace(',', '') #remove commas
    parts = instruction.split()
    parts = [part.strip() for part in parts] #remove extra spaces idk if we need
    opcode = parts[0] #for all types the first is opcode

   
    if opcode in R_type_opcodes:
       # R type instructions
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
       # immediate instructions
        opcode_binary = I_type_opcodes[opcode]["opcode"]
        rd_binary = register_name_to_binary(parts[1])
       
        rs1_binary = register_name_to_binary(parts[2])
        immediate = format(int(parts[3]), '012b')  # assuming the immediate value fits in 12 bits
        funct3_binary = I_type_opcodes[opcode]["funct3"]
        #full binary instruction for I-type
        binary_instruction = immediate + rs1_binary + funct3_binary + rd_binary + opcode_binary
        return bin_to_hex(binary_instruction)
       
    elif opcode in B_type_opcodes:
        # Branch instructions beq x1, x2, branch
        funct3_binary = B_type_opcodes[opcode]["funct3"]
        opcode_binary = B_type_opcodes[opcode]["opcode"]
        rs1_binary = register_name_to_binary(parts[1])
        rs2_binary = register_name_to_binary(parts[2])
        imm = (dec_to_bin(int(parts[3]), 13))
        imm_rev = imm[slice(None, None,-1)]
        machine_code_binary = imm_rev[12] + imm_rev[4:10] +rs2_binary + rs1_binary + funct3_binary + imm_rev[0:4] + imm_rev[11]+ opcode_binary
        return bin_to_hex(machine_code_binary)
    else:
        print("Unsupported instruction:", opcode)
        return None
       
def assemble_file(input_file, output_file):
    input = open(input_file, 'r')
    output = open(output_file, 'w')
    for line in input:
        hex_instruction = str(assemble(line))
        output.write(hex_instruction + "\n")

#########################################################################

input_file = 'input.asm'
output_file = 'output.txt'
assemble_file(input_file, output_file)
