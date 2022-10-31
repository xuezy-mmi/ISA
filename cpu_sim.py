
def List2Num(list, len):
    num = 0
    for i in range(0, len):
        num = num + list[len - 1 - i] * 2 ** i
    if (list[0] == 1):  # <0
        num = -(2 ** len - num)
    return num


def Num2List(num, len):
    list = []
    if (num >= 0):
        complement = bin(num).split('b')[1].zfill(len)
        for i in range(0, len):
            # a = int(complement[len-1-i])
            list.append(int(complement[i]))
    else:  # num < 0
        abs_num = -num
        if(abs_num == 2**(len-1)):
            list.append(1)
            for k in range(len-1):
                list.append(0)
            return list
        source = 'One' + bin(abs_num).split('b')[1].zfill(len-1)
        inverse = source.replace('1', 'z').replace('0', '1').replace('z', '0').replace('One', '1')
        complement = '1' + bin(int(inverse[1:], 2)+1).split('b')[1].zfill(len-1)
        for i in range(0, len):
            # a = int(complement[len-1-i])
            list.append(int(complement[i]))

    return list


class cpu:
    def __init__(self, reg_width, reg_addr_width, mem_width, mem_addr_width, endian):
        self.pc = 0
        self.reg_width = reg_width
        self.reg_addr_width = reg_addr_width
        self.mem_width = mem_width
        self.mem_addr_width = mem_addr_width
        self.reg = [[0] * reg_width] * 2**reg_addr_width  #############################
        #reg0-reg15:data_reg reg16-31:addr_reg
        self.mem = [[0] * mem_width] * mem_addr_width  #############################
        self.endian = endian  # 0:little endian 1:big-endian

    def store_mem(self, addr, data):
        mem_list = Num2List(data, self.mem_width)
        int_addr = List2Num(addr, self.mem_addr_width)
        self.mem[int_addr] = mem_list

    def display_reg(self, d, s):
        print("reg%d - reg%d : " % (d, s))
        for i in range(d, s):
            regnum = List2Num(self.reg[i], self.reg_width)
            print(self.reg[i], " number in this reg is %d" % regnum)

    def display_mem(self, d, s):
        print("mem%d - mem%d : " % (d, s))
        for i in range(d, s):
            memnum = List2Num(self.mem[i], self.mem_width)
            print(self.mem[i], " number in this mem is %d" % memnum)

def CompReg(cpu, regaddr1, regaddr2):
    if(cpu.reg[regaddr1] == cpu.reg[regaddr2]):
        return 1
    elif(cpu.reg[regaddr1] >= cpu.reg[regaddr2]):
        return 2
    else:
        return 0