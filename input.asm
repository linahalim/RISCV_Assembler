ADDI	a0, x0, 6 # this is n 
ADDI	t0, x0, 1 # this is fact
ADDI	a1, x0, 1 
ADDI 	a1, a1, 1
MUL 	t0, t0, a1
ADDI 	a1, a1, 1
BNE 	a1, a0, -8
MUL 	t0, t0, a1