def main():
    initial_input = get_initial_input()
    part1(initial_input) 
    part2(initial_input)

def part1(initial_input):
    counter = 0
    for elem in initial_input:
        counter += sum_of_figures(elem)
    print(counter)

def part2(initial_input):
    counter = 0
    for elem in initial_input:
        counter += sum_of_figures_corr(elem)
    print(counter) 

def get_initial_input():
    f = open("input.txt", "r")
    outcome = []
    for line in f:
        # print(line)
        outcome.append(santize(line[:-1], 0))
    return outcome

def sum_of_figures(initial_input):
    if isinstance(initial_input[0], list) == True:
        temp_soucet = sum_of_figures(initial_input[0])
    else:
        temp_soucet = int(initial_input[0])
    for i in range(len(initial_input)):
        if initial_input[i] == "+":
            if isinstance(initial_input[i + 1], list) == True:
                temp_soucet += sum_of_figures(initial_input[i + 1])
            else:
                temp_soucet += int(initial_input[i + 1])
        elif initial_input[i] == "*":
            if isinstance(initial_input[i + 1], list) == True:
                temp_soucet *= sum_of_figures(initial_input[i + 1])
            else:    
                temp_soucet *= int(initial_input[i + 1])
    return temp_soucet
      
def sum_of_figures_corr(initial_input):
    figures_multi = []
    figures_sum = []
    for i in range(len(initial_input)):
        if initial_input[i] == "+":
            if len(figures_sum) == 0:
                if isinstance((initial_input[i - 1]), list) == False:
                    figures_sum.append(int(initial_input[i - 1]))
                else:
                    figures_sum.append(sum_of_figures_corr(initial_input[i - 1]))
                if isinstance((initial_input[i + 1]), list) == False:
                    figures_sum.append(int(initial_input[i + 1]))
                else:
                    figures_sum.append(sum_of_figures_corr(initial_input[i + 1]))
            else:
                if isinstance((initial_input[i + 1]), list) == False:
                    figures_sum.append(int(initial_input[i + 1]))
                else:
                    figures_sum.append(sum_of_figures_corr(initial_input[i + 1]))    
        if initial_input[i] == "*":
            if len (figures_sum) == 0:
                if isinstance((initial_input[i - 1]), list) == False:
                    figures_multi.append(int(initial_input[i - 1]))
                else:
                    figures_multi.append(sum_of_figures_corr(initial_input[i - 1]))                
            else:
                temp_sum = 0
                for elem in figures_sum:
                    temp_sum += elem
                figures_multi.append(temp_sum)
                figures_sum = []
    if initial_input[-2] == "*":
        if isinstance((initial_input[-1]), list) == False:
            figures_multi.append(int(initial_input[-1]))
        else:
            figures_multi.append(sum_of_figures_corr(initial_input[-1]))    
    if len(figures_sum) != 0:
        temp_sum = 0
        for elem in figures_sum:
            temp_sum += elem
        figures_multi.append(temp_sum)
    # print(figures_multi, figures_sum)    
    temp = 1
    for elem in figures_multi:
        temp *= elem
    return temp
                
def sum_of_figures_v2(initial_input):
    figures = []
    try:
        if initial_input[1] == "*":
            if isinstance(initial_input[0], list) == True:
                figures.append(sum_of_figures_v2(initial_input[0]))
            else:
                figures.append(int(initial_input[0]))
    except:
        figures.append(int(initial_input[0]))
    for i in range(len(initial_input)):
        if initial_input[i] == "+":
            if isinstance(initial_input[i + 1], list) == True:
                if isinstance(initial_input[i - 1], list) == True:
                    figures.append(sum_of_figures_v2(initial_input[i - 1]) + sum_of_figures_v2(initial_input[i + 1]))
                else:
                    figures.append(int(initial_input[i -1]) + sum_of_figures_v2(initial_input[i + 1]))
            else:
                if isinstance(initial_input[i - 1], list) == True:
                    figures.append(sum_of_figures_v2(initial_input[i - 1]) + int(initial_input[i + 1]))
                else:
                    figures.append(int(initial_input[i -1]) + int(initial_input[i + 1]))       
    temp = 1
    for elem in figures:
        temp *= elem
    # print(temp)
    return temp

    
def santize(initial_input, paren_no):
    # print("Volam:", initial_input)
    temp_list = []
    for i in range(len(initial_input)):
        if initial_input[i] == " ":
            continue
        elif initial_input[i] == "(":
            end = get_closing_paren(initial_input[i+1:])
            # print("V zavorce:", initial_input[i+1:i+end])
            outcm = santize(initial_input[i+1:i+end], paren_no)
            if len(outcm) != 0:
                temp_list.append(outcm)
            # temp_list.append(santize(initial_input[i+1:i+end], paren_no))
            paren_no += 1
        elif initial_input[i] == ")":
            paren_no -= 1
            # print("Temp po zavorce: ", temp_list)
        else:
            if paren_no == 0:
                temp_list.append(initial_input[i])        
    # print("Vracim:", temp_list)
    return temp_list

def get_closing_paren(initial_input):
    paren_no = 0
    for i in range(len(initial_input)):
        if initial_input[i] == "(":
            paren_no += 1
        if initial_input[i] == ")":
            if paren_no == 0:
                return i + 1
            else:
                paren_no -= 1
                
main()
