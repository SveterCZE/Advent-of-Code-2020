# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:50:48 2021

@author: petrs
"""
import math

def main():
    tiles = get_initial_input()
    tiles_numbers, shody, corners = part1(tiles)
    part2(tiles, tiles_numbers, shody, corners)
    # print(tiles)
    return

def get_initial_input():
    f = open("input.txt", "r")
    tiles = {}
    for line in f:
        if line[0] == "T":
            title_name = int(line.split()[1][:-1])
            tiles[title_name] = []
        elif len(line) > 1:
            temp = []
            for elem in line:
                if elem == ".":
                    temp.append("0")
                elif elem == "#":
                    temp.append("1")
            tiles[title_name].append(temp)
    return tiles

def part1(tiles):
    tiles_numbers = get_tiles_numbers(tiles)
    shody = get_matches(tiles_numbers)
    corners = get_corners(tiles_numbers, shody)
    sum_corners(corners)
    return tiles_numbers, shody, corners

class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    
class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + "->" + self.dest.getName()

class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError("Duplicate node")
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        result = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getname() + "->" + dest.getName() + "\n"
        return result[:-1] 

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

def printPath(path):
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + "->"
    return result

def DFS(graph, start, end, path, shortest, toPrint = False):
    path = path + [start]
    if toPrint:
        print("Current DFS path: ", printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
    return shortest

def BFS(graph, start, end, toPrint = False):
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print("Current BFS path: ", printPath(initPath))
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        # print("Current BFS path: ", printPath(tmpPath))
        # print("Current BFS path length: ", len(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)

def shortestPath(graph, start, end, toPrint = False):
    return DFS(graph, start, end, [], None, toPrint)


def part2(tiles, tiles_numbers, shody, corners):
    # Dirty fix to manually adjust corners in a way that allows for 
    # corners = [corners[2], corners[1], corners[3], corners[0]]
    corners = [corners[0], corners[3], corners[1], corners[2]]
    tiles_numbers_non_rotated = {}
    tiles_numbers_rotated = {}
    grid = create_empty_grid(int(math.sqrt(len(tiles))), "X")
    # print(grid)
    for key, value in tiles_numbers.items():
        tiles_numbers_non_rotated[key] = value[0]
        tiles_numbers_rotated[key] = value[1]
    # print("ROTATED", tiles_numbers_rotated)
    # print("NON-ROTATED", tiles_numbers_non_rotated)
    nodes = []
    for key,value in tiles_numbers.items():
        nodes.append(Node(str(key)))
    g = Digraph()
    for n in nodes:
        g.addNode(str(n))
    # print(tiles)
    for key, value in tiles_numbers.items():
        rider = key
        for elem in tiles_numbers_non_rotated[rider]:
            for key, value in tiles_numbers_non_rotated.items():
                if elem in value and key != rider:
                    # print("(non-rotated) S kostickou", rider, "muze sousedit kosticka", key, "protoze maji shodne strany", elem, value)
                    g.addEdge(Edge(str(rider), str(key)))
            for key, value in tiles_numbers_rotated.items():
                if elem in value and key != rider:
                    # print("(rotated)S kostickou", rider, "muze sousedit kosticka", key, "protoze maji shodne strany", elem, value)
                    g.addEdge(Edge(str(rider), str(key)))
    create_border(grid, corners, g)
    fill_in_lines(grid, corners, g)
    # print(grid)
    rotation_grid = create_empty_grid(int(math.sqrt(len(tiles))), "X")
    determine_first_tile_rotation(tiles_numbers, grid, rotation_grid)
    # rotation_grid[0][0] = 4
    determine_first_line_orientation(tiles_numbers, grid, rotation_grid)
    determine_other_lines(tiles_numbers, grid, rotation_grid)
    # print(rotation_grid)
    # orientations = determine_orientations(grid, tiles_numbers)    
    big_grid = create_big_square(len(grid), len(tiles[corners[0]]) - 2)   
    populate_big_grid(big_grid, grid, tiles, rotation_grid, tiles_numbers)
    # print(big_grid)
    # insert_squares(tiles, grid, rotation_grid)
    roughnss = search_for_monster(big_grid)
    if roughnss == 0:
        roughnss = search_for_monster(flip_grid(big_grid))
    print(roughnss)
    # print(corners)
    # print(grid[0][0])
    # print(tiles_numbers[int(grid[0][0])])
    # # print([item for sublist in tiles_numbers[int(grid[0][0])] for item in sublist])
    # print(grid[0][1])
    # print(tiles_numbers[int(grid[0][1])])
    # # print(grid[1][0])
    # print(tiles_numbers[int(grid[1][0])])
    # print(grid[2][0])
    # print(tiles_numbers[int(grid[2][0])])
    # print(grid)
    # print(big_grid)
    return

def search_for_monster(big_grid):
    for x in range(4):
        monsters_coords = []
        monsters_found = 0
        for i in range(len(big_grid)):
            for j in range(len(big_grid)):
                if big_grid[i][j] == "1":
                    try:
                        if big_grid[i+1][j-18] == "1" and big_grid[i+1][j-13] == "1" and big_grid[i+1][j-12] == "1" and big_grid[i+1][j-7] == "1" and big_grid[i+1][j-6] == "1" and big_grid[i+1][j-1] == "1" and big_grid[i+1][j] == "1" and big_grid[i+1][j+1] == "1" and big_grid[i+2][j-17] == "1" and big_grid[i+2][j-14] == "1" and big_grid[i+2][j-11] == "1" and big_grid[i+2][j-8] == "1" and big_grid[i+2][j-5] == "1" and big_grid[i+2][j-2] == "1":
                            monsters_coords.append([i,j])
                            monsters_found += 1
                    except:
                        continue
        if monsters_found == 0:
            big_grid = rotate_grid(big_grid)
        else:
            identify_monsters(big_grid, monsters_coords)
            rougness = measure_roughness(big_grid)
            return rougness
    
    return 0

def identify_monsters(big_grid, monsters_coords):
    for elem in monsters_coords:
        i = elem[0]
        j = elem[1]
        big_grid[i][j] = "M"
        big_grid[i+1][j-18] = "M"
        big_grid[i+1][j-13] = "M"
        big_grid[i+1][j-12] = "M"
        big_grid[i+1][j-7] = "M"
        big_grid[i+1][j-6] = "M"
        big_grid[i+1][j-1] = "M"
        big_grid[i+1][j] = "M"
        big_grid[i+1][j+1] = "M"
        big_grid[i+2][j-17] = "M"
        big_grid[i+2][j-14] = "M"
        big_grid[i+2][j-11] = "M"
        big_grid[i+2][j-8] = "M"
        big_grid[i+2][j-5] = "M"
        big_grid[i+2][j-2] = "M"
    return

def measure_roughness(big_grid):
    rougness = 0
    for elem in big_grid:
        for item in elem:
            if item == "1":
                rougness +=1
    return rougness
        
def determine_first_tile_rotation (tiles_numbers, grid, rotation_grid):
    rotation = 0
    next_tiles = [item for sublist in tiles_numbers[int(grid[0][1])] for item in sublist]
    # Full version
    # first_cube_numbers = [tiles_numbers[int(grid[0][0])][0][1], tiles_numbers[int(grid[0][0])][0][2], tiles_numbers[int(grid[0][0])][0][3], tiles_numbers[int(grid[0][0])][0][0], tiles_numbers[int(grid[0][0])][1][1], tiles_numbers[int(grid[0][0])][1][2], tiles_numbers[int(grid[0][0])][1][3], tiles_numbers[int(grid[0][0])][1][0]]
    # I will use just one section
    first_cube_numbers = [tiles_numbers[int(grid[0][0])][1][1], tiles_numbers[int(grid[0][0])][1][2], tiles_numbers[int(grid[0][0])][1][3], tiles_numbers[int(grid[0][0])][1][0]]
    for elem in first_cube_numbers:        
        if elem in next_tiles:
                rotation_grid[0][0] = rotation
        rotation += 1
    return 0

def determine_first_line_orientation (tiles_numbers, grid, rotation_grid):
    # Iterate over every element other than the first one    
    for i in range (1, len(grid[0][1:]) + 1):
        # elem_list = [item for sublist in tiles_numbers[int(grid[0][i])] for item in sublist]
        elem_list = [tiles_numbers[int(grid[0][i])][0][3], tiles_numbers[int(grid[0][i])][0][2], tiles_numbers[int(grid[0][i])][0][1], tiles_numbers[int(grid[0][i])][0][0], tiles_numbers[int(grid[0][i])][1][3], tiles_numbers[int(grid[0][i])][1][2], tiles_numbers[int(grid[0][i])][1][1], tiles_numbers[int(grid[0][i])][1][0]]
        rotation = 0
        # Check if the previous square is filpped or not
        if rotation_grid[0][i-1] < 4:
            previous_elem_list = tiles_numbers[int(grid[0][i - 1])][1]
        else:
            previous_elem_list = tiles_numbers[int(grid[0][i - 1])][0]
        # Iterate over elems in the border numbers of the current tile to determine its orientation                
        # print(elem_list)
        # print(previous_elem_list)
        # print(i, previous_elem_list, elem_list)
        for elem in elem_list:
            if elem in previous_elem_list:
                rotation_grid[0][i] = rotation
            rotation += 1        
    return

def determine_other_lines(tiles_numbers, grid, rotation_grid):
    for i in range(1, len(grid[0][1:]) + 1):
        for j in range (len(grid[0])):
            # print(i,j)
            rotation = 0
            # DOPLNIT SPRAVNE PORADI PRO ROTACE
            # elem_list = [item for sublist in tiles_numbers[int(grid[i][j])] for item in sublist]
            elem_list = [tiles_numbers[int(grid[i][j])][0][0], tiles_numbers[int(grid[i][j])][0][3], tiles_numbers[int(grid[i][j])][0][2], tiles_numbers[int(grid[i][j])][0][1], tiles_numbers[int(grid[i][j])][1][0], tiles_numbers[int(grid[i][j])][1][3], tiles_numbers[int(grid[i][j])][1][2], tiles_numbers[int(grid[i][j])][1][1]]
            if rotation_grid[i-1][j] < 4:
                previous_elem_list = tiles_numbers[int(grid[i-1][j])][1]
            else:
                previous_elem_list = tiles_numbers[int(grid[i-1][j])][0]
            for elem in elem_list:
                if elem in previous_elem_list:
                    # print(i,j, elem, elem_list, tiles_numbers[int(grid[i][j])], previous_elem_list)
                    rotation_grid[i][j] = rotation
                    # print("Je to tam")
                rotation += 1 

def populate_big_grid(big_grid, grid, tiles, rotation_grid, tiles_numbers):
    for i in range(len(grid)):
        for j in range(len(grid)):
            insert_individual_tile(big_grid, tiles, len(grid), i, j, grid[i][j], rotation_grid)
    

def rotate_squares(tiles, rotation_grid, i, j, tile_no):
    square_length = len(tiles[int(tile_no)])
    # print(square_length)
    # print(tiles)
    template_grid = []
    for x in range(square_length):
        y_template = []
        for y in range(square_length):
            y_template.append(tiles[int(tile_no)][x][y])
        template_grid.append(y_template)
    if rotation_grid[i][j] > 3:
        template_grid = flip_grid(template_grid)
        rotation_grid[i][j] = rotation_grid[i][j] - 4
    if rotation_grid[i][j] == 0:            
        return template_grid
    else:
        for x in range(rotation_grid[i][j]):
            template_grid = rotate_grid(template_grid)
        
        return template_grid
        
def rotate_grid(template_grid):
    grid_len = len(template_grid)        
    flipped_grid = []
    for i in range(grid_len):
        y_temp = []
        for j in range(grid_len):
            y_temp.append("x")
        flipped_grid.append(y_temp)
    for i in range(grid_len):
        for j in range(grid_len):
            flipped_grid[i][j] = template_grid[(grid_len-1) - j][i]
    return flipped_grid

def flip_grid(template_grid):
    grid_len = len(template_grid)
    flipped_grid = []
    for i in reversed(range(grid_len)):
        flipped_grid.append(template_grid[i])
    return flipped_grid

# def determine_orientations(grid, tiles_numbers):
#     orientations = create_empty_grid(len(grid))    
#     determine_first_tile_orientation(grid, tiles_numbers, orientations)
#     determine_first_line_orientation(grid, tiles_numbers, orientations)
#     determine_remaining_line_orientation(grid, tiles_numbers, orientations)
#     print(orientations)
#     return orientations

# def determine_first_tile_orientation(grid, tiles_numbers, orientations):
#     print(tiles_numbers)
#     # first_tile_rider = tiles_numbers[int(grid[0][0])]
#     # TADY CHCI DOPLNIT PEVNE 4, ABYCH SIMULOVAL VZOROVY PRIKLAD
#     first_tile_rider = [item for sublist in tiles_numbers[int(grid[0][0])] for item in sublist]
#     second_tile_rider = [item for sublist in tiles_numbers[int(grid[0][1])] for item in sublist]
#     for i in range(len(first_tile_rider)):
#         if first_tile_rider[i] in second_tile_rider:
#                 orientations[0][0] = i + 3
#                 # print("Pro prvni pozici volime orientaci", orientations[0][0])
#                 return
#         i += 1

# def determine_first_line_orientation(grid, tiles_numbers, orientations):
#     for i in range(1, len(grid)):
#         # Urcime orientaci predchoziho ctverce
#         previous_tile_orientation = orientations[0][i-1]
#         # Urcime provazne cislo, je-li vetsi nez 3, kosticka je flinpnuta a divame se jen na druhou cast cisel, jinak jen na prvni
#         if previous_tile_orientation <= 3:
#             previous_tile_border_numbers = tiles_numbers[int(grid[0][i-1])][0]
#         else:
#             previous_tile_border_numbers = tiles_numbers[int(grid[0][i-1])][1]         
#         # Create a list of all border numbers for current tile
#         current_tile_border_numers = [item for sublist in tiles_numbers[int(grid[0][i])] for item in sublist]
#         # Iterate over the numbers to determine which matches the border number of the previous tile
#         for j in range(len(current_tile_border_numers)):
#             if current_tile_border_numers[j] in previous_tile_border_numbers:
#                 orientations[0][i] = j-3
                
# def determine_remaining_line_orientation(grid, tiles_numbers, orientations):
#     print(grid)
#     for i in range(1, len(grid)):
#         for j in range(len(grid)):
#             previous_tile_orientation = orientations[i-1][j]
#             if previous_tile_orientation <= 3:
#                 previous_tile_border_numbers = tiles_numbers[int(grid[i-1][j])][0]
#             else:
#                 previous_tile_border_numbers = tiles_numbers[int(grid[i-1][j])][1]
#             print("Vkladam to do:", grid[i][j], "divam se na vazbu na", grid[i-1][j], "a hledam cisla", previous_tile_border_numbers)

def create_big_square(grid_size, tile_size):
    len_size =  grid_size * tile_size
    big_grid = []
    for i in range(len_size):
        temp = []
        for i in range (len_size):
            temp.append("")
        big_grid.append(temp)
    return big_grid
    
# def populate_big_grid(big_grid, grid, tiles):
#     # print(grid)
#     for i in range(len(grid)):
#         for j in range(len(grid)):
#             # print(i,j,grid[i][j])
#             insert_individual_tile(big_grid, tiles, len(grid), i, j, grid[i][j])

def insert_individual_tile(big_grid, tiles, grid_len, i, j, tile_no, rotation_grid):
    coord_x = i * int((len(big_grid) / grid_len))
    coord_y = j * int((len(big_grid) / grid_len))  
    rider = int((len(big_grid) / grid_len))
    # print("Vlozim kostku", tile_no)
    # print("Jeji obsah je", tiles[int(tile_no)])
    rotated_tile = rotate_squares(tiles, rotation_grid, i, j, tile_no)
    for x in range(rider):
        for y in range(rider):
            big_grid[coord_x + x][coord_y + y] = rotated_tile[x+1][y+1]




def create_border(grid, corners, g):
    create_top_border(grid, corners, g)
    create_bottom_border(grid, corners, g)
    create_left_border(grid, corners, g)
    create_right_border(grid, corners, g)

def create_top_border(grid, corners, g):
    sp2 = BFS(g, str(corners[0]), str(corners[1]), toPrint = False)
    short_path = printPath(sp2).split("->")
    for i in range(len(short_path)):
        grid[0][i] = short_path[i]
    # print("Shortest BFS Path is: ", printPath(sp2))

def create_bottom_border(grid, corners, g):
    sp2 = BFS(g, str(corners[3]), str(corners[2]), toPrint = False)
    short_path = printPath(sp2).split("->")
    for i in range(len(short_path)):
        grid[len(short_path) - 1][i] = short_path[i]
    # print("Shortest BFS Path is: ", printPath(sp2))

def create_left_border(grid, corners, g):
    sp2 = BFS(g, str(corners[0]), str(corners[3]), toPrint = False)
    short_path = printPath(sp2).split("->")
    for i in range(len(short_path)):
        grid[i][0] = short_path[i]
    # print("Shortest BFS Path is: ", printPath(sp2))

def create_right_border(grid, corners, g):
    sp2 = BFS(g, str(corners[1]), str(corners[2]), toPrint = False)
    short_path = printPath(sp2).split("->")
    for i in range(len(short_path)):
        grid[i][len(short_path) - 1] = short_path[i]
    # print("Shortest BFS Path is: ", printPath(sp2))

def fill_in_lines(grid, corners, g):
    for i in range(1, len(grid) - 1):
        sp2 = BFS(g, grid[i][0], grid[i][len(grid) - 1], toPrint = False)
        short_path = printPath(sp2).split("->")
        for j in range(len(short_path)):
            grid[i][j] = short_path[j]

def create_empty_grid(size, dummy = 0):
    grid = []
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(dummy)
        grid.append(temp)
    return grid


def add_next_cube(last_added_cube, tiles_numbers, shody, prvni_rada_puzzle):
    print(last_added_cube)
    for item in tiles_numbers[last_added_cube]:
        for elem in item:
            if shody[elem] == 1:
                print("Stranu", elem, "má taky", get_neigbouring_cube(elem, tiles_numbers, last_added_cube, prvni_rada_puzzle))
                return (get_neigbouring_cube(elem, tiles_numbers, last_added_cube, prvni_rada_puzzle))

def get_neigbouring_cube(elem, tiles_numbers, nono, prvni_rada_puzzle):
    for key, value in tiles_numbers.items():
        for item in value:
            if elem in item and key != nono and key not in prvni_rada_puzzle:
                return key
                
def get_tiles_numbers(tiles):
    tiles_numbers = {}
    for key, value in tiles.items():
        a = value[0]
        c = value[9]
        b = []
        d = []
        for elem in value:
            d.append(elem[0])
            b.append(elem[9])       
        tiles_numbers[key] = [convert_to_decimal(a), convert_to_decimal(b), convert_to_decimal(rev(c)), convert_to_decimal(rev(d))], [convert_to_decimal(c), convert_to_decimal(rev(b)), convert_to_decimal(rev(a)), convert_to_decimal(d)]
    # print(tiles_numbers)    
    return tiles_numbers

def get_matches(tiles_numbers):
    shody = {}
    for key, value in tiles_numbers.items():
        for elem in value:
            for i in elem:
                if i in shody:
                    shody[i] += 1
                else:
                    shody[i] = 0
    return shody

def get_corners(tiles_numbers, shody):
    corners = []
    for key, value in tiles_numbers.items():
        for elem in value:
            temp = 0
            for i in elem:
                temp +=  shody[i]
            if temp == 2 and key not in corners:
                corners.append(key)
    return corners

def sum_corners(corners):
    sum_corners = 1
    for elem in corners:
        sum_corners *= elem
    print(sum_corners)
    return 0
        
def convert_to_decimal(binarni):
    return int("".join(binarni), 2)

def rev (otocit):
    return otocit[::-1]
    
main()