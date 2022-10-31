from cpu_sim import *

file = '/home/xzy/MATT/ACA/exp2/inst.txt'

with open(file, 'r') as f:
    ass_inst_set = []
    inst = f.readlines()
    for i in inst:
        data = i.split()
        ass_inst_set.append(data)
print(ass_inst_set)
inst_op = ['lb', 'add', 'sb', 'beq', 'bge', 'lw', 'jal', 'sw']

def link(ass_inst_set):
    set_len = len(ass_inst_set)
    inst_set = []
    for i in range(0, set_len):
        inst = [0] * 32
        #ass_inst = ass_inst_set[i].split()
        if(ass_inst_set[i][0] == 'lb'):
            inst[25:32] = [0,0,0,0,0,1,1]
            inst[17:20] = [0,0,0]
            strrd = ass_inst_set[i][1]
            numrd = int(strrd.split('r')[1])
            inst[20:25] = Num2List(numrd, 5)
            strm = ass_inst_set[i][2]
            imm = int(strm.split('(')[0])
            rs  = int(strm.split('(')[1].split(')')[0][1:4])
            inst[12:17] = Num2List(rs, 5)
            inst[0:12] = Num2List(imm, 12)
            #if(ass_inst_set[i][0][1]):
        
        if(ass_inst_set[i][0] == 'lw'):
            inst[25:32] = [0,0,0,0,0,1,1]
            inst[17:20] = [0,1,0]
            strrd = ass_inst_set[i][1]
            numrd = int(strrd.split('r')[1])
            inst[20:25] = Num2List(numrd, 5)
            strm = ass_inst_set[i][2]
            imm = int(strm.split('(')[0])
            rs  = int(strm.split('(')[1].split(')')[0][1:4])
            inst[12:17] = Num2List(rs, 5)
            inst[0:12] = Num2List(imm, 12)

        if(ass_inst_set[i][0] == 'add'):
            inst[25:32] = [0,1,1,0,0,1,1]
            inst[0:7] = [0, 0, 0, 0, 0, 0, 0]
            inst[17:20] = [0, 0, 0]
            strrd = ass_inst_set[i][1]
            numrd = int(strrd.split('r')[1])
            strr1 = ass_inst_set[i][2]
            numr1 = int(strr1.split('r')[1])
            strr2 = ass_inst_set[i][3]
            numr2 = int(strr2.split('r')[1])
            inst[20:25] = Num2List(numrd, 5)
            inst[7:12]  = Num2List(numr1, 5)
            inst[12:17] = Num2List(numr2, 5)
        if(ass_inst_set[i][0] == 'sb'):
            inst[25:32] = [0,1,0,0,0,1,1]
            inst[17:20] = [0,0,0]
            strrd = ass_inst_set[i][1]
            numrd = int(strrd.split('r')[1])
            inst[7:12] = Num2List(numrd, 5)

            strm = ass_inst_set[i][2]
            imm = int(strm.split('(')[0])
            rs  = int(strm.split('(')[1].split(')')[0][1:4])
            inst[12:17] = Num2List(rs, 5)
            temp = []
            temp[0:12] = Num2List(imm, 12)
            inst[0:7] = temp[0:7]
            inst[20:25] = temp[7:12]
        if(ass_inst_set[i][0] == 'sw'):
            inst[25:32] = [0,1,0,0,0,1,1]
            inst[17:20] = [0,1,0]
            strrd = ass_inst_set[i][1]
            numrd = int(strrd.split('r')[1])
            inst[7:12] = Num2List(numrd, 5)

            strm = ass_inst_set[i][2]
            imm = int(strm.split('(')[0])
            rs  = int(strm.split('(')[1].split(')')[0][1:4])
            inst[12:17] = Num2List(rs, 5)
            temp = []
            temp[0:12] = Num2List(imm, 12)
            inst[0:7] = temp[0:7]
            inst[20:25] = temp[7:12]
            #print("swswswsw")
        if(ass_inst_set[i][0] == 'beq'):
            inst[25:32] = [1,1,0,0,0,1,1]
            inst[17:20] = [0,0,0]
            strr1 = ass_inst_set[i][1]
            numr1 = int(strr1.split('r')[1])
            inst[7:12] = Num2List(numr1, 5)
            strr2 = ass_inst_set[i][2]
            numr2 = int(strr2.split('r')[1])
            inst[12:17] = Num2List(numr2, 5)
            imm = int(ass_inst_set[i][3])
            listnum = Num2List(imm, 12)
            inst[0:7] = listnum[0:7]
            inst[20:25] = listnum[7:12]
        if(ass_inst_set[i][0] == 'bge'):
            inst[25:32] = [1,1,0,0,0,1,1]
            inst[17:20] = [1,0,1]

        if(ass_inst_set[i][0] == 'jal'):
            inst[25:32] = [1,1,0,1,1,1,1]
            strrd = ass_inst_set[i][1]
            numrd = int(strrd.split('r')[1])
            inst[20:25] = Num2List(numrd, 5)
            imm = int(ass_inst_set[i][2])
            listnum = Num2List(imm, 20)
            inst[0:20] = listnum
        inst_set.append(inst[0:8])
        inst_set.append(inst[8:16])
        inst_set.append(inst[16:24])
        inst_set.append(inst[24:32])
    return inst_set

inst_set = link(ass_inst_set)
for i in range(0, 8):
    print(inst_set[4*i:4*i+4])

strs = '16(r236)'
strr = 'r256'
numrd = int(strr.split('r')[1])
numoffset = int(strs.split('(')[0])#16
numrs = int(strs.split('(')[1].split(')')[0][1:4])#23
print(numrd)
print(numoffset, numrs)