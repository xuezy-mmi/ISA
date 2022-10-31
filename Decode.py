from cpu_sim import *

def Decode_I(inst, op):#lb #lw
    imm = List2Num(inst[0:12], 12)
    r1 = List2Num(inst[20: 25], 5)
    op[1] = r1
    r2 = List2Num(inst[12: 17], 5)
    #memaddr = List2Num()
    op[2] = r2
    op[4] = imm

def Decode_R(inst, op):#add
    r1 = List2Num(inst[20:25], 5)
    op[1] = r1
    r2 = List2Num(inst[7: 12], 5)
    op[2] = r2
    r3 = List2Num(inst[12: 17], 5)
    op[3] = r3

def Decode_S(inst, op):#sb #sw
    imm = List2Num(inst[0:7] + inst[20:25], 12)
    r1 = List2Num(inst[7:12], 5)
    op[1] = r1
    r2 = List2Num(inst[12:17], 5)
    op[2] = r2
    op[4] = imm

def Decode_B(inst, op):
    r1 = List2Num(inst[12:17], 5)
    op[1] = r1
    r2 = List2Num(inst[7:12], 5)
    op[2] = r2
    offset = List2Num(inst[0:7]+inst[20:25], 12)
    op[4] = offset

def Decode_J(inst, op):
    imm = List2Num(inst[0:20], 20)
    op[4] = imm
    rd = List2Num(inst[20:25], 5)
    op[1] = rd
    return 0
def Decode(inst):
    # OP = [lb, add, sb, beq, bge, lw, jal, sw]
    # op = [op, r1, r2, r3, imm/offset]
    op = [0, 0, 0, 0, 0]
    if (inst == [0] * 32):#finish
        op = [0, 0, 0, 0, 0]
    if (inst[25:32] == [0, 0, 0, 0, 0, 1, 1]):  # load
        if (inst[17:20] == [0, 0, 0]):#lb
            op[0] = 1
        if (inst[17:20] == [0, 1, 0]):#lw
            op[0] = 6
        Decode_I(inst, op)

    if (inst[25:32] == [0, 1, 1, 0, 0, 1, 1]):  # add
        if (inst[0:7] == [0, 0, 0, 0, 0, 0, 0] and inst[17:20] == [0, 0, 0]):
            op[0] = 2
            Decode_R(inst, op)
    if (inst[25:32] == [0, 1, 0, 0, 0, 1, 1]):# store
        
        if (inst[17:20] == [0, 0, 0]):#sb
            op[0] = 3
            #print("sdfasdfasdf")
        if (inst[17:20] == [0,1,0]):#sw
            op[0] = 8
            #print("sdfasdfasdf")
        Decode_S(inst, op)
    if (inst[25:32] == [1,1,0,0,0,1,1]):#B-TYPE
        if(inst[17:20] == [0,0,0]):#beq
            op[0] = 4
        if(inst[17:20] == [1,0,1]):#bge
            op[0] = 5
        Decode_B(inst, op)
    if(inst[25:32] == [1,1,0,1,1,1,1]):#jal
        Decode_J(inst, op)
        op[0] = 7
    return op