def load():
    field = []
    temp = []
    with open("input.txt", "r", encoding = "utf8") as f:
        for line in f:
            if line == "\n":
                # print("empty")
                field.append(temp)
                temp = []
            else:
                temp.append(line[:-1])    
    return field

def main():
    field = load()
    correct = 0
    correct_ver2 = 0
    # print(field)
    for item in field:
        passport_dict = {"byr": None, "iyr": None, "eyr": None, "hgt": None, "hcl": None, "ecl": None, "pid" : None, "cid": None}
        for elem in item:
            recur_parse(elem, passport_dict)
        if check_passport(passport_dict) == True:
            correct += 1
        if check_passport_ver2(passport_dict) == True:
            correct_ver2 += 1
        
        # print(passport_dict)  
    print(correct)
    print(correct_ver2)

def recur_parse(elem, passport_dict):
    temp = []
            # print(elem[0:3])
            # print(elem)
    rider = 4
    for char in elem[rider:]:
        rider += 1
        if char != " ":
            temp.append(char)
        else:
            recur_parse(elem[rider:], passport_dict)
            break
        passport_dict[elem[0:3]] = "".join(temp)
            
def check_passport(passport_dict):
    for key, value in passport_dict.items():
        if value == None:
            if key == "cid":
                continue
            else:
                return False
    return True
    
def check_passport_ver2(passport_dict):
    permitted_letters = ["a", "b", "c", "d", "e", "f"]
    permitted_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for key, value in passport_dict.items():
        if value == None:
            if key == "cid":
                continue
            else:
                return False
        if key == "byr":
            if int(value) < 1920 or int(value) > 2002:
                return False
        if key == "iyr":
            if int(value) < 2010 or int(value) > 2020:
                return False
        if key == "eyr":
            if int(value) < 2020 or int(value) > 2030:
                return False
        if key == "hgt":
            hgt_measure = ""
            hgt_figure = ""
            for char in value:
                if char.isalpha() == True:
                    hgt_measure += char
                elif char.isnumeric() == True:
                    hgt_figure += char
            if hgt_measure == "cm":
                if int(hgt_figure) < 150 or int(hgt_figure) > 193:
                    return False
            if hgt_measure == "in":
                if int(hgt_figure) < 59 or int(hgt_figure) > 76:
                    return False    
            if hgt_measure != "cm":
                if hgt_measure != "in":
                    return False
        if key == "hcl":
            if value[0] != "#":
                return False
            if len(value) != 7:
                return False
            for char in value[1:]:
                if char not in permitted_letters:
                    if char.isnumeric() != True:
                        return False
        if key == "ecl":
            if value not in permitted_colors:
                return False
        if key == "pid":
            if len(value) != 9:
                return False 
    return True

main()
