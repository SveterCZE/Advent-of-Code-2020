import re

def main():
    valid_tickets, permitted_numbers, my_ticket = part1()
    part2(valid_tickets, permitted_numbers, my_ticket)

    
def get_input():
    f = open("input.txt", "r")
    tickets = []
    permitted_numbers = []
    for line in f:
        temp = []
        if line[0].isnumeric() == True:
            tickets.append([int(e) for e in line.split(',')])
        elif line[0].isnumeric() == False and "-" in line:
            p = " ".join([s for s in re.findall(r'\w+', line) if s.isalpha() == True][:-1])
            temp.append(p)
            x = [int(s) for s in re.findall(r'\d+', line)]
            for elem in range(x[0], x[1] + 1):
                temp.append(elem)
            for elem in range(x[2], x[3] + 1):
                temp.append(elem)
        if len(temp) > 0:
            permitted_numbers.append(temp)
    return tickets[1:], permitted_numbers, tickets[:1]

def part1():
    tickets, permitted_numbers, my_ticket = get_input()
    invalid_sum = 0
    valid_tickets = []
    for elem in tickets:
        valid_ticket = True
        for item in elem:
            if any(item in sublist for sublist in permitted_numbers) == False:
                invalid_sum += item
                valid_ticket = False
        if valid_ticket == True:
            valid_tickets.append(elem)
    print ("Part 1 outcome:", invalid_sum)
    return valid_tickets, permitted_numbers, my_ticket[0]

def part2(valid_tickets, permitted_numbers, my_ticket):
    solution_matrix = []
    for elem in valid_tickets[0]:
        temp = []
        for item in permitted_numbers:
            temp.append([item[0], True])
        solution_matrix.append(temp)        
    for elem in valid_tickets:
        counter = 0
        for item in elem:
            sub_counter = 0
            for sub_item in solution_matrix[counter]:
                if item not in permitted_numbers[sub_counter]:
                    solution_matrix[counter][sub_counter][1] = False
                sub_counter += 1
            counter += 1    
    solutions_clear = []
    while True:
        counter3 = 0
        for elem in solution_matrix:        
            if len([val for sublist in elem for val in sublist if val == True]) == 1:
                   # print (counter3, elem)
                   for item in elem:
                       if item[1] == True:
                           solutions_clear.append([counter3, item[0]])
                           cleaner = item[0]
            counter3 += 1
        positive_counter = 0
        for elem in solution_matrix:
            for item in elem:
                if item[1] == True:
                    positive_counter += 1
                if item[0] == cleaner:
                    item[1] = False
        if positive_counter == 0:
            break
    part2_result = 1
    for elem in solutions_clear:
        if "departure" in elem[1]:
            part2_result = part2_result * my_ticket[elem[0]]
    print ("Part 2 outcome:", part2_result)

main()
