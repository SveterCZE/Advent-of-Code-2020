# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:39:43 2020

@author: Petr
"""

import time

def main():
    layout = get_input()
    part1(layout)
    layout = get_input()
    part2(layout)

def part1(layout):
    while True:
        # print(layout)
        # PART 1 - Iterate and detemine number of changes
        change_to_occupied = []
        change_to_free = []
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == "L":
                    if get_occupied(layout, i, j) == 0:
                        change_to_occupied.append([i,j])
                elif layout[i][j] == "#":
                    if get_occupied(layout, i, j) >= 4:
                        change_to_free.append([i,j])            
        # PART 2 - Check if there any changes
        # print (change_to_occupied, change_to_free)
        if len(change_to_occupied) == 0 and len(change_to_free) == 0:
            temp = 0
            for i in range(len(layout)):
                for j in range(len(layout[0])):
                    if layout[i][j] == "#":
                        temp +=1
            print(temp)
            return
        # PART 3 - Update the table
        for elem in change_to_occupied:
            # print(layout[elem[0]][elem[1]])
            layout[elem[0]][elem[1]] = "#"
        for elem in change_to_free:
            # print(layout[elem[0]][elem[1]])
            layout[elem[0]][elem[1]] = "L"

def part2(layout):
    while True:
        # print(layout)
        change_to_occupied = []
        change_to_free = []
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == "L":
                    if get_occupied_v2(layout, i, j) == 0:
                        change_to_occupied.append([i,j])
                elif layout[i][j] == "#":
                    if get_occupied_v2(layout, i, j) >= 5:
                        change_to_free.append([i,j])            
        # PART 2 - Check if there any changes                
        if len(change_to_occupied) == 0 and len(change_to_free) == 0:
            temp = 0
            for i in range(len(layout)):
                for j in range(len(layout[0])):
                    if layout[i][j] == "#":
                        temp +=1
            print(temp)
            return
        # PART 3 - Update the table
        for elem in change_to_occupied:
            layout[elem[0]][elem[1]] = "#" 
        for elem in change_to_free:
            layout[elem[0]][elem[1]] = "L"
            
            
def get_input():
    f = open("input.txt", "r")
    numbers = []
    for line in f:
        temp = []
        for char in line:
            temp.append(char)
        numbers.append(temp[:-1])
    return numbers

def get_occupied(layout, i, j):
    methods = [(1,0), (-1, 0), (1,1), (-1, -1), (0, 1), (0, -1), (1, -1), (-1, 1)]
    occupied_neighbours = 0
    for elem in methods:
        if i+elem[0] >= 0 and i+elem[0] < len(layout) and j+elem[1] >=0 and j+elem[1] < len(layout[0]):
            if layout[i+elem[0]][j+elem[1]] == "#":
                occupied_neighbours += 1
    return occupied_neighbours
    
def get_occupied_v2(layout, i, j):
    methods = [(1,0), (-1, 0), (1,1), (-1, -1), (0, 1), (0, -1), (1, -1), (-1, 1)]
    occupied_neighbours = 0
    for elem in methods:
        coord = [i,j]
        seat_found = False
        coord = move(coord, elem)
        while is_valid_coord(layout, coord) == True and seat_found == False:
            # print(coord)
            if layout[coord[0]][coord[1]] == "#":
                seat_found = True
                occupied_neighbours += 1
            elif layout[coord[0]][coord[1]] == "L":
                seat_found = True
            coord = move(coord, elem)
    # print(i, j, occupied_neighbours)
    return occupied_neighbours

def move(coord, method):
    coord[0], coord[1] = coord[0] + method[0], coord[1] + method[1]
    return coord

def is_valid_coord(layout, coord):
    if coord[0] < 0:
        return False
    elif coord[1] < 0:
        return False
    elif coord[0] >= len(layout):
        return False
    elif coord[1] >= len(layout[0]):
        return False
    else:
        return True

    # for elem in methods:
    #     i2 = i
    #     j2 = j
    #     while True:
    #         i2 += elem[0]
    #         j2 += elem[1]
    #         if i2 >= 0 and i2 < len(layout) and j2 >=0 and j2 < len(layout[0]):
    #             if layout[i2][j2] == "#":
    #                 occupied_neighbours += 1
    #                 break
    #         else:
    #             break
    

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))