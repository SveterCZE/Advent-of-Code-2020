def part1():
    correct = 0
    with open("input.txt", "r", encoding = "utf8") as f:
        for line in f:
            first, second, letter, password = parse_line(line)
            if check_pass(first, second, letter, password) == True:
                correct += 1
    print(correct)

def parse_line(line):
    first_num = []
    second_num = []
    password = []
    mezera = False
    dvojtecka = False
    
    char = []
    for char in line:
        if char.isnumeric() == True:
            if mezera == False:
                first_num.append(char)
            else:
                second_num.append(char)
            #     print("je")
        elif char == "-":
             mezera = True
        elif char.isalpha() == True:
            if dvojtecka == False:
                letter = char
            else:
                password.append(char)
        elif char == ":":
            dvojtecka = True
            
        # print(char)
        # if char == '-':
        #     min_freq_rider = rider
        # elif char == " ":
        #     max_freq_rider = rider
        # rider += 1
    # first = int("".join(first_num))
    # second = int("".join(second_num))
    # print (first, second, letter, password)
    return (int("".join(first_num)), int("".join(second_num)), letter, "".join(password))
    
def check_pass(first, second, letter, password):
    temp = 0
    for char in password:
        if char == letter:
            temp += 1
    if temp >= first and temp <= second:
        return True
    else:
        return False
            
def part2():
    correct = 0
    with open("input.txt", "r", encoding = "utf8") as f:
        for line in f:
            first, second, letter, password = parse_line(line)
            if check_pass_part2(first, second, letter, password) == True:
                correct += 1
    print(correct)

def check_pass_part2(first, second, letter, password):
    match = 0
    if password[first - 1] == letter:
        match += 1
    if password[second - 1] == letter:
        match += 1
    if match == 1:
        return True
    else:
        return False

part1()
part2()
