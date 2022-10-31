'''
-memory
---32-bit address
---8-bit cell
-register
---32 32-bit
-program
---add the number in memory address 0 and 1 to address 3
Assembly instruction:
---load r1 #0     000000000000 00000 000 00001 0000011   I-TYPE  lb r1, offset(0)+reg0
---load r2 #1     000000000001 00000 000 00010 0000011   I-TYPE  lb r2, offset(1)+reg0
---add r3 r2 r1   0000000 00001 00010 000 00011 0110011  R-TYPE  add r3, r2, r1
---store r3 #3    0000000 00011 00000 000 00011 0100011  S-TYPE  sb r3, offest(3)+reg0
mem3 = mem0 + mem1
mem width is 8. signed int varies [-128 , 127]


lb   I-TYPE imm12 rs1 000 rd 0000011 x[rd] = m[x[rs1]+imm]8  lb r1 0(r0)
lw   I-TYPE imm12 rs1 010 rd 0000011 x[rd] = m[x[rs1]+imm]32  lw r4 0(r0)

sb   S-TYPE offset7 rs2 rs1 000 offset5 0100011  sb r3 3(r0)
sw   S-TYPE offset7 rs2 rs1 010 offset5 0100011  sw r4 4(r0)

addi I-TYPE imm12 rs1 000 rd 0010011  x[rd] = x[rs1] + 32(imm12)
andi I-TYPE imm12 rs1 111 rd 0010011
add  R-TYPE                                       add r3 r2 r1
div  R-TYPE 0000001 rs2 rs1 100 rd 0110011 x[rd] = x[rs1] / x[rs2]
mul  R-type 0000001 RS2 RS1 000 RD 0110011 x[rd] = x[rs1] * x[rs2]


#beq  B-TYPE offset12|10:5 rs2 rs1 000 offset4:1|11 1100011   x[rs1]=x[rs2] => pc+offset
      beq r1 r2 imm
#bge  B-TYPE offset12|10:5 rs2 rs1 101 offset4:1|11 1100011

#jal  J-TYPE offset20|10:1|11|19:12 rd 1101111       x[rd] = pc+4;pc+offset
jr   J-TYPE 
'''
from cpu_sim import *
from Decode import *
from exe import *
from assembler import *
def Instruction_ROM(rom, inst):
    rom.append(inst[0:8])
    rom.append(inst[8:16])
    rom.append(inst[16:24])
    rom.append(inst[24:32])

def main():  # complete result = data1 + data2
    # cpu has nothing
    cpu0 = cpu(32, 5, 8, 32, 0)
    cpu0.display_reg(0, 4)
    cpu0.display_mem(0, 4)
    # init cpu#####store data1, data2, data3 to cpu.mem
    ##########    Edit here     ##########
    data1 = -64
    data2 = -64
    data3 = 100
    ######################################
    addr0 = Num2List(0 , 32)
    addr1 = Num2List(1 , 32)
    addr2 = Num2List(2 , 32)
    cpu0.store_mem(addr0, data1)
    cpu0.store_mem(addr1, data2)
    cpu0.store_mem(addr2, data3)
    cpu0.display_reg(0, 4)
    cpu0.display_mem(0, 4)
    """
    # init inst_rom
    inst1 = [0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0, 0,0,0, 0,0,0,0,1, 0,0,0,0,0,1,1]
    inst2 = [0,0,0,0,0,0,0,0,0,0,0,1, 0,0,0,0,0, 0,0,0, 0,0,0,1,0, 0,0,0,0,0,1,1]
    inst3 = [0,0,0,0,0,0,0, 0,0,0,1,0, 0,0,0,0,1, 0,0,0, 0,0,0,1,1, 0,1,1,0,0,1,1]
    inst4 = [0,0,0,0,0,0,0, 0,0,0,1,1, 0,0,0,0,0, 0,0,0, 0,0,0,1,1, 0,1,0,0,0,1,1]
    inst5 = [0] * 32
    inst_rom = []
    Instruction_ROM(inst_rom, inst1)
    Instruction_ROM(inst_rom, inst2)
    Instruction_ROM(inst_rom, inst3)
    Instruction_ROM(inst_rom, inst4)
    Instruction_ROM(inst_rom, inst5)
    #print(inst_rom)
    """
    file = '/home/xzy/MATT/ACA/exp2/inst.txt'

    with open(file, 'r') as f:
        ass_inst_set = []
        inst = f.readlines()
        for i in inst:
            data = i.split()
            ass_inst_set.append(data)
    #inst_op = ['lb', 'add', 'sb', 'beq', 'bge', 'lw', 'jal', 'sw']
    inst_rom = link(ass_inst_set)
    inst_rom.append([0]*8)#
    inst_rom.append([0]*8)
    inst_rom.append([0]*8)
    inst_rom.append([0]*8)
    inst_rom.append([0]*8)#
    inst_rom.append([0]*8)
    inst_rom.append([0]*8)
    inst_rom.append([0]*8)
    inst_rom.append([0]*8)#
    inst_rom.append([0]*8)
    inst_rom.append([0]*8)
    inst_rom.append([0]*8)
    
    pc0 = cpu0.pc
    while (pc0 < 44):
        op = Decode(inst_rom[pc0]+inst_rom[pc0+1]+inst_rom[pc0+2]+inst_rom[pc0+3])
        EXE(cpu0, op)
        pc0 = cpu0.pc
        print(pc0)
    '''
    op1 = Decode(inst1)
    op2 = Decode(inst2)
    op3 = Decode(inst3)
    op4 = Decode(inst4)
    op5 = Decode(inst5)
    EXE(cpu0, op1)
    EXE(cpu0, op2)
    EXE(cpu0, op3)
    EXE(cpu0, op4)
    EXE(cpu0, op5)
    '''
    cpu0.display_reg(0, 5)
    cpu0.display_mem(0, 8)
    
if __name__ == "__main__":
    main()