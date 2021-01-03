# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:24:51 2021

@author: petrs
"""

def main():
    cups = [3,6,2,9,8,1,7,5,4]
    # cups = [3,8,9,1,2,5,4,6,7]
    part1(cups.copy())
    part2(cups.copy())
    
def part1(cups):
    current = cups[0]
    for i in range(100):
        temp = [cups[((cups.index(current)) + 1) %len(cups)], cups[((cups.index(current)) + 2) %len(cups)], cups[((cups.index(current)) + 3) %len(cups)]]
        for elem in temp:
            cups.remove(elem)
        # Select destination cup
        destination = current - 1
        # If lower than 1, give it the value of the highest elem
        if destination < 1:
            destination = 9
        # Decrease a value of destination if it is in the temp_list
        while destination in temp:
            destination -= 1
            if destination < 1:
                destination = 9
        try:
            current = cups[cups.index(current) + 1]
        except:
            current = cups[(cups.index(current) + 1)%len(cups)]
        try:
            cups.insert((cups.index(destination) + 1), temp)
        except:
            cups.insert((cups.index(destination) + 1)%len(cups), temp)
        flat_list = []
        for sublist in cups:
            try:
                for item in sublist:
                    flat_list.append(item)
            except:
                    flat_list.append(sublist)
        cups = flat_list.copy()
    temp1 = []
    temp2 = []
    nula_seen = False
    for elem in cups:
        if elem == 1:
            nula_seen = True
        elif nula_seen == False:
            temp1.append(str(elem))
        else:
            temp2.append(str(elem))
    print ("".join(temp2) + "".join(temp1))
    return 0

def part2(cups):
    cups = create_extended_cups(cups)
    cups_dict = create_cups_dict(cups)
    delka = len(cups_dict)
    current = cups[0]
    for i in range(10000000):
        # Get a list of items to be moved away
        temp = []
        rider = current
        for j in range(3):
            temp.append(cups_dict[rider])
            rider = cups_dict[rider]
        # Update the circule and remove three selected items
        cups_dict[current] = cups_dict[temp[2]]
        # Urci cilovy cup
        destination = current - 1
        if destination < 1:
            destination = delka
        while destination in temp:
            destination -= 1
            if destination < 1:
                destination = delka
        # Connect the list with temporary items
        destin_temp = cups_dict[destination]
        cups_dict[destination] = temp[0]
        cups_dict[temp[2]] = destin_temp
        # Set new current value
        current = cups_dict[current]
    
    x = cups_dict[1]
    y = cups_dict[x]
    print(x * y)
    return 0

def create_extended_cups(cups):
    for i in range(len(cups) + 1, 1000000 + 1):
        cups.append(i)
    return cups        
        

def create_cups_dict(cups):
    cups_dict = {}
    cups_dict[cups[len(cups) - 1]] = cups[0]
    for i in range(len(cups) - 1):
        cups_dict[cups[i]] = cups[i+1]
    return cups_dict
                
        
main()
