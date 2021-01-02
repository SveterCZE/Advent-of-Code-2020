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
    f = open("input2.txt", "r")
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
    corners = [corners[2], corners[1], corners[3], corners[0]]
    tiles_numbers_non_rotated = {}
    tiles_numbers_rotated = {}
    grid = create_empty_grid(int(math.sqrt(len(tiles))))
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
                    # print("S kostickou", rider, "muze sousedit kosticka", key, "protoze maji shodne strany", elem, value)
                    g.addEdge(Edge(str(rider), str(key)))
            for key, value in tiles_numbers_rotated.items():
                if elem in value and key != rider:
                    # print("S kostickou", rider, "muze sousedit kosticka", key, "protoze maji shodne strany", elem, value)
                    g.addEdge(Edge(str(rider), str(key)))
    create_border(grid, corners, g)
    fill_in_lines(grid, corners, g)
    big_grid = create_big_square(len(grid), len(tiles[corners[0]]) - 2)   
    populate_big_grid(big_grid, grid, tiles)
    print(corners)
    print(grid[0][0])
    print(tiles_numbers[int(grid[0][0])])
    print(grid[0][1])
    print(tiles_numbers[int(grid[0][1])])
    print(grid[1][0])
    print(tiles_numbers[int(grid[1][0])])
    print(grid[2][0])
    print(tiles_numbers[int(grid[2][0])])
    # print(grid)
    # print(big_grid)
    return

def create_big_square(grid_size, tile_size):
    len_size =  grid_size * tile_size
    big_grid = []
    for i in range(len_size):
        temp = []
        for i in range (len_size):
            temp.append("")
        big_grid.append(temp)
    return big_grid
    
def populate_big_grid(big_grid, grid, tiles):
    # print(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            # print(i,j,grid[i][j])
            insert_individual_tile(big_grid, tiles, len(grid), i, j, grid[i][j])

def insert_individual_tile(big_grid, tiles, number_squares, i, j, tile_no):
    coord_x = i * int((len(big_grid) / number_squares))
    coord_y = j * int((len(big_grid) / number_squares))  
    rider = int((len(big_grid) / number_squares))
    # print("Vlozim kostku", tile_no)
    # print("Jeji obsah je", tiles[int(tile_no)])
    for x in range(rider):
        for y in range(rider):
            big_grid[coord_x + x][coord_y + y] = tiles[int(tile_no)][x+1][y+1]

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

def create_empty_grid(size):
    grid = []
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(0)
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
        b = value[9]
        c = []
        d = []
        for elem in value:
            c.append(elem[0])
            d.append(elem[9])       
        tiles_numbers[key] = [convert_to_decimal(a), convert_to_decimal(b), convert_to_decimal(c), convert_to_decimal(d)], [convert_to_decimal(rev(a)), convert_to_decimal(rev(b)), convert_to_decimal(rev(c)), convert_to_decimal(rev(d))]
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