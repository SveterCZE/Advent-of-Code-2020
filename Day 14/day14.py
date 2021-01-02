def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    
def get_input():
    f = open("input.txt", "r")
    instructions = []
    temp = []
    for line in f:
        number_switch = False
        if line[0:3] == "mas":
            if len(temp) != 0:
                instructions.append(temp)
                temp = []
                temp.append(line[7:-1])
            else:
                temp = []
                temp.append(line[7:-1])
        else:
            mem = []
            ins = []
            for char in line[4:]:
                if char.isnumeric() == True:
                    if number_switch == False:
                        mem.append(char)
                    else:
                        ins.append(char)
                elif char == "=":
                    number_switch = True            
            temp.append(((int("".join(mem)), int("".join(ins)))))
    instructions.append(temp)
    return instructions

def convert_to_bin(num):
    return '{0:036b}'.format(num)

def apply_mask(binary, mask):
    bin_temp = []
    bin_temp[:0]=binary
    for i in range(len(mask)):
        if mask[i] == "1":
            bin_temp[i] = "1"
        elif mask[i] == "0":
            bin_temp[i] = "0"
    return "".join(bin_temp)

def convert_to_deci(binary):
    return int(binary, 2)

def part1(instructions):
    memo = {}
    for elem in instructions:
        mask = elem[0]
        for item in elem[1:]:
            binary = convert_to_bin(item[1])
            binary = apply_mask(binary, mask)
            deci = convert_to_deci(binary)
            memo[item[0]] = deci
    memo_sum = 0
    for key, value in memo.items():
        memo_sum += value
    print(memo_sum)

def part2(instructions):
    memo = {}
    for elem in instructions:
        mask = elem[0]
        variables_mask = get_mask_variables(mask)
        for item in elem[1:]:
            masks_v2(item, mask, variables_mask, memo)
    memo_sum = 0
    for key, value in memo.items():
        memo_sum += value
    print(memo_sum)    

def masks_v2(item, mask, variables_mask, memo):
    for i in range (2**variables_mask):
        helper_bin = convert_to_bin(i)
        apply_mask_v2(item[0], item[1], mask, helper_bin, i, variables_mask, memo)
        

def apply_mask_v2(address, value, mask, helper_bin, rider, variables_mask, memo):
    addr_bin = []
    addr_bin[:0] = convert_to_bin(address)
    bin_rider = convert_to_bin(rider)[-variables_mask:]
    bin_counter = 0
    for i in range(len(addr_bin)):
         if mask[i] == "1":
             addr_bin[i] = "1"
         elif mask[i] == "X":
             addr_bin[i] = bin_rider[bin_counter]
             bin_counter += 1    
    mem_addr = convert_to_deci("".join(addr_bin))
    memo[mem_addr] = value


def get_mask_variables(mask):
    temp = 0
    for char in mask:
        if char == "X":
            temp +=1
    return temp
        

main()
