from cpu_sim import *
def Op_LB(cpu, op):#mem to reg   op = 1
    target_reg_addr = op[1]
    addr_in_reg = List2Num(cpu.reg[op[2]], cpu.reg_width)
    source_mem_addr = addr_in_reg + op[4]
    
    if(target_reg_addr < 16):
        data = [cpu.mem[source_mem_addr][0]]*24 + cpu.mem[source_mem_addr]
        cpu.reg[target_reg_addr] = data
    else:# >=16
        addr = [0] * 24 + cpu.mem[source_mem_addr]
        cpu.reg[target_reg_addr] = addr
    cpu.pc = cpu.pc + 4

def Op_LW(cpu, op):
    rs = op[2]
    offset = op[4]
    mem_addr = List2Num(cpu.reg[rs], cpu.reg_width) + offset
    data = cpu.mem[mem_addr]+cpu.mem[mem_addr+1]+cpu.mem[mem_addr+2]+cpu.mem[mem_addr+3]#list
    rd = op[1]
    cpu.reg[rd] = data
    cpu.pc = cpu.pc + 4

def Op_ADD(cpu, op):#op = 2
    target_reg_addr = op[1]
    source_reg_addr1 = op[2]
    source_reg_addr2 = op[3]
    data1 = cpu.reg[source_reg_addr1]  # 32list
    data2 = cpu.reg[source_reg_addr2]  # 32list
    result = List2Num(data1, 32) + List2Num(data2, 32)
    if(result < -2**(cpu.mem_width-1)):
        print("result negative overflow!")
    elif(result >= 2**(cpu.mem_width-1)):
        print("result positive overflow!")
    else:
        cpu.reg[target_reg_addr] = Num2List(result, 32)
    cpu.pc = cpu.pc + 4


def Op_SB(cpu, op):#reg to mem   op = 3
    addr_in_reg = List2Num(cpu.reg[op[2]], cpu.reg_width)
    target_mem_addr = addr_in_reg + op[4]
    source_reg_addr = op[1]
    if(source_reg_addr < 16):
        data = List2Num(cpu.reg[source_reg_addr], cpu.reg_width)
        dlist = Num2List(data, cpu.mem_width)
        cpu.mem[target_mem_addr] = dlist
    else:
        addr = cpu.reg[source_reg_addr]  # 32list
        cpu.mem[target_mem_addr] = addr[24:32]
    cpu.pc = cpu.pc + 4

def Op_SW(cpu, op):
    addr_in_reg = List2Num(cpu.reg[op[2]], cpu.reg_width)
    target_mem_addr = addr_in_reg + op[4]
    source_reg_addr = op[1]
    #data = List2Num(cpu.reg[source_reg_addr], cpu.reg_width)
    #dlist = Num2List(data, cpu.reg_width)
    data = cpu.reg[source_reg_addr]
    #print(data)
    cpu.mem[target_mem_addr] = data[0:8]
    cpu.mem[target_mem_addr+1] = data[8:16]
    cpu.mem[target_mem_addr+2] = data[16:24]
    cpu.mem[target_mem_addr+3] = data[24:32]
    cpu.pc = cpu.pc + 4

def Op_BEQ(cpu, op):#op = 4
    r1 = op[1]
    r2 = op[2]
    if(CompReg(cpu, r1, r2) == 1):
        cpu.pc = cpu.pc + op[4]
    else:
        cpu.pc = cpu.pc + 4

def Op_BGE(cpu, op):#op = 5
    r1 = op[1]
    r2 = op[2]
    if(CompReg(cpu, r1, r2) == 2):
        cpu.pc = cpu.pc + op[4]
    else:
        cpu.pc = cpu.pc + 4

def Op_JAL(cpu, op):
    rd = op[1]
    cpu.reg[rd] = cpu.pc + 4
    cpu.pc = cpu.pc + op[4]


def Op_Finish(cpu):
    print("Instructions Implement Finish")
    m0 = List2Num(cpu.mem[0], cpu.mem_width)
    m1 = List2Num(cpu.mem[1], cpu.mem_width)
    m3 = List2Num(cpu.mem[3], cpu.mem_width)
    print("mem3 = mem0 + mem1 = %d = %d + %d" % (m3, m0, m1))
    cpu.pc = cpu.pc + 4


def EXE(cpu, op):
    if (op[0] == 0):
        Op_Finish(cpu)
    if (op[0] == 1):
        Op_LB(cpu, op)
    if (op[0] == 2):
        Op_ADD(cpu, op)
    if (op[0] == 3):
        Op_SB(cpu, op)
    if (op[0] == 4):
        Op_BEQ(cpu, op)
    if (op[0] == 5):
        Op_BGE(cpu, op)
    if (op[0] == 6):
        Op_LW(cpu, op)
    if (op[0] == 7):
        Op_JAL(cpu, op)
    if (op[0] == 8):
        Op_SW(cpu, op)
