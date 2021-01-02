import copy

def main ():
    part1()
    part2()

                
def get_instructions():
    f = open("input.txt", "r")
    instructions = []
    for line in f:
        temp = []
        temp.append(line[:3])
        temp.append(line[4])
        temp.append(int(line[5:-1]))
        instructions.append(temp)
    return instructions

def get_instruction2():
    f = open("input.txt", "r")
    instructions = []
    for line in f:
        temp = []
        temp.append(line[:3])
        if line[4] == "+":
            temp.append(int(line[5:-1]))
        else:
            temp.append(int(line[5:-1]) * -1)
        instructions.append(temp)
    return instructions

def part1():
    instructions = get_instructions()
    instructions_called = []
    instruction_pointer = 0
    accumulator = 0
    while True:
        # print(accumulator, instructions_called, instruction_pointer)
        if instruction_pointer in instructions_called:
            print("Part 1: ", accumulator)
            return accumulator
        else:
            instructions_called.append(instruction_pointer)
            if instructions[instruction_pointer][0] == "acc":
                if instructions[instruction_pointer][1] == "+":
                    accumulator += instructions[instruction_pointer][2]
                else:
                    accumulator -= instructions[instruction_pointer][2]
                instruction_pointer += 1
            elif instructions[instruction_pointer][0] == "jmp":
                if instructions[instruction_pointer][1] == "+":
                    instruction_pointer += instructions[instruction_pointer][2]
                else:
                    instruction_pointer -= instructions[instruction_pointer][2]
            elif instructions[instruction_pointer][0] == "nop":
                instruction_pointer += 1

def part2():
    instructions = get_instruction2()
    end_point = len(instructions)
    for i in range(len(instructions)):
        # print(instructions)
        instructions_mod = copy.deepcopy(instructions)
        if instructions_mod[i][0] == "nop":
            instructions_mod[i][0] = "jmp"
        elif instructions_mod[i][0] == "jmp":
            instructions_mod[i][0] = "nop"
        # print(instructions_mod)
        instructions_called = []
        instruction_pointer = 0
        accumulator = 0
        reached_last = False
        while True:
            # print(accumulator, instruction_pointer, instructions_called)
            if instruction_pointer == end_point:
                reached_last = True
            elif instruction_pointer in instructions_called:
                # print("END: ", accumulator)
                break
            else:
                instructions_called.append(instruction_pointer)
                if instructions_mod[instruction_pointer][0] == "acc":
                    accumulator += instructions_mod[instruction_pointer][1]
                    instruction_pointer += 1
                elif instructions_mod[instruction_pointer][0] == "jmp":
                    instruction_pointer += instructions_mod[instruction_pointer][1]
                elif instructions_mod[instruction_pointer][0] == "nop":
                    instruction_pointer += 1
            if reached_last == True:
               print("Part 2: ", accumulator)
               return
            
main()
