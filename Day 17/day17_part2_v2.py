# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:13:25 2020

@author: petrs
"""

def main():
    initial_input = get_initial_input()
    # print("Initial:", count_active(initial_input))
    for i in range(6):
        highest, lowest = get_hi_lo(initial_input)
        # Iterate over individual items + added buffer to cover neighbouring squares
        iterator(highest + 1, lowest - 1, initial_input)
    print(count_active(initial_input))
    
def get_initial_input():
    initial_input = {}
    f = open("input.txt", "r")
    counter1 = 0
    for line in f:
        counter2 = 0
        for elem in line[:-1]:
            if elem == "#":
                initial_input[(0,0,counter1, counter2)] = elem
            counter2 += 1
        counter1 += 1
    return initial_input

def get_hi_lo(initial_input):
    lo = 0
    hi = 0
    for key, value in initial_input.items():
        for item in key:
            if item > hi:
                hi = item
            if item < lo:
                lo = item
    return hi, lo
        
def iterator(hi, lo, initial_input):
    to_be_activated = []
    to_be_deactivated = []
    for i in range(lo,hi+1):
        for j in range(lo,hi+1):
            for k in range(lo,hi+1):
                for l in range(lo,hi+1):
                    neighbours = count_neighbours(i,j,k,l,initial_input)
                    # Active
                    if (i,j,k,l) in initial_input:
                        if neighbours != 2:
                            if neighbours != 3:
                                to_be_deactivated.append([i, j, k, l])
                    # Inactive
                    else:
                        if neighbours == 3:
                            to_be_activated.append([i, j, k, l])
    # Deactivate
    deactivate(to_be_deactivated, initial_input)
    # Activate
    activate(to_be_activated, initial_input)
    return          

def deactivate(to_be_deactivated, initial_input):
    for elem in to_be_deactivated:
        initial_input.pop((elem[0], elem[1], elem[2], elem[3]))

def activate(to_be_activated, initial_input):
    for elem in to_be_activated:
        initial_input[(elem[0], elem[1], elem[2], elem[3])] = "#"

def count_neighbours(i,j,k,l,initial_input):
    neighbour_counter = 0
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for z1 in range(-1,2):
                    if (i+x, j+y, k+z, l+z1) in initial_input:
                        if x == 0 and y == 0 and z == 0 and z1 == 0:
                            pass
                        else:
                            neighbour_counter += 1
    return neighbour_counter

def count_active(initial_input):
    counter = 0
    for key in initial_input.items():
        counter += 1
    return counter
    

main()