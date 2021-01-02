def main():

    initial_input = get_initial_input()
    for i in range(6):
        initial_input = create_additional_layer(initial_input)    
        tb_deactivated, tb_activated = activate_or_deactivate(initial_input)
        for elem in tb_activated:
            activate_cell(initial_input,elem[0],elem[1],elem[2])
        for elem in tb_deactivated:
            de_activate_cell(initial_input,elem[0],elem[1],elem[2])
    # print_square(initial_input)
    print(sum_of_active(initial_input))
    return

def activate_cell(initial_input,a,b,c):
    initial_input[a][b][c] = "#"
    return

def de_activate_cell(initial_input,a,b,c):
    initial_input[a][b][c] = "."
    return    

def print_square(initial_input):
    for elem in initial_input:
        print("\n")
        for item in elem:
            print("".join(item))

def get_initial_input():
    f = open("input.txt", "r")
    initial_input = []
    for line in f:
        temp = []
        for elem in line:
            temp.append(elem)
        initial_input.append(temp[:-1])
    return [initial_input]

def create_additional_layer(initial_input):
    extend_existing_layers(initial_input)
    new_layer = (create_empty_list(len(initial_input[0][0])))
    initial_input.insert(0, new_layer.copy())
    new_layer = (create_empty_list(len(initial_input[0][0])))
    initial_input.append(new_layer.copy())
    return initial_input

def create_empty_list(length):
    temp = []
    for i in range(length):
        temp2 = []
        for j in range(length):
            temp2.append(".")
        temp.append(temp2)
    return temp

def create_empty_row(length):
    temp = []
    for j in range(length):
        temp.append(".")
    return temp


def extend_existing_layers(initial_input):
    for elem in initial_input:
        # print(elem)
        for item in elem:
            item.insert(0, ".")
            item.append(".")
            # print(item)
    for elem in initial_input:
        new_line = create_empty_row(len(initial_input[0][0]))        
        elem.insert(0, new_line.copy())
        elem.append(new_line.copy())

def activate_or_deactivate(initial_input):
    activate = []
    de_activate = []
    for i in range(len(initial_input)):
        for j in range(len(initial_input[0])):
            for k in range(len(initial_input[0])):
                act = get_active_neighbours(initial_input, i, j, k)
                if initial_input[i][j][k] == "#":
                    if act != 2:
                        if act != 3:
                            de_activate.append([i, j, k])
                if initial_input[i][j][k] == ".":
                    if act == 3:
                        activate.append([i, j, k])
    return de_activate, activate

def get_active_neighbours(initial_input, i, j, k):
    act_neighbours = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x == 0 and y == 0 and z == 0:
                    continue
                else:
                    try:
                        if initial_input[i+x][j+y][k+z] == "#":    
                            act_neighbours += 1
                    except:
                        continue
    return act_neighbours

def sum_of_active(initial_input):
    counter = 0
    for i in range(len(initial_input)):
        for j in range(len(initial_input[0])):
            for k in range(len(initial_input[0])):
                if initial_input[i][j][k] == "#":
                    counter += 1
    return counter 
main()
