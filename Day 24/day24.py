def main():
    instructions = get_input()
    black_tiles = part1(instructions)
    part2(black_tiles)
    
    return

def get_input():
    f = open("input.txt", "r")
    instructions = []
    for line in f:
        temp = []
        i = 0
        while i < len(line) - 1:
            if line[i] == "e" or line[i] == "w":
                temp.append(line[i])
                i+=1
            else:
                temp.append(line[i] + line[i+1])
                i+=2
        instructions.append(temp)
    return instructions
        
def part1(instructions):
    memo = {}
    # print(instructions)
    for elem in instructions:
        coordinates_x = 0
        coordinates_y = 0
        coordinates_z = 0
        for item in elem:
            if item == "e":
                coordinates_x += 1
                coordinates_y -= 1  
            elif item == "w":
                coordinates_x -= 1
                coordinates_y += 1
            elif item == "se":
                coordinates_y -= 1
                coordinates_z += 1
            elif item == "sw":
                coordinates_x -= 1
                coordinates_z += 1
            elif item == "nw":
                coordinates_y += 1
                coordinates_z -= 1
            elif item == "ne":
                coordinates_x += 1
                coordinates_z -= 1
        # print(elem)
        check_coordinates(coordinates_x, coordinates_y, coordinates_z, memo)
    black = 0
    black_tiles = {}
    for key, value in memo.items():
         if value % 2 != 0:
             black += 1
             black_tiles[key] = value
    print (len(black_tiles))
    return black_tiles

def check_coordinates(coordinates_x, coordinates_y, coordinates_z, memo):
    if (coordinates_x, coordinates_y, coordinates_z) in memo:
        memo[(coordinates_x, coordinates_y, coordinates_z)] += 1
    else:
        memo[(coordinates_x, coordinates_y, coordinates_z)] = 1

def part2(black_tiles):
    # print("Zacatek:", len(black_tiles))
    for i in range(100):
        neighbouring_white = {}
        blacks_to_be_turned = {}
        for key, value in black_tiles.items():
            neighbouring_black = get_neighbouring_black_tiles(key[0], key[1], key[2], black_tiles, neighbouring_white)
            if neighbouring_black == 0 or neighbouring_black > 2:
                blacks_to_be_turned[key] = value
        turn_black_to_white(blacks_to_be_turned, black_tiles)
        turn_white_to_black(neighbouring_white, black_tiles)
    print("Round:", i + 1, len(black_tiles))
    return

def get_neighbouring_black_tiles(coord_x, coord_y, coord_z, black_tiles, neighbouring_white):
    neighbouring_black_cubes = 0
    cube_directions = [[+1, -1, 0], [+1, 0, -1], [0, +1, -1], [-1, +1, 0], [-1, 0, +1], [0, -1, +1]]
    for elem in cube_directions:
        if (coord_x + elem[0], coord_y + elem[1], coord_z + elem[2]) in black_tiles:
            neighbouring_black_cubes += 1
        else:
            if (coord_x + elem[0], coord_y + elem[1], coord_z + elem[2]) not in neighbouring_white:
                neighbouring_white[(coord_x + elem[0], coord_y + elem[1], coord_z + elem[2])] = 1
            else:
                neighbouring_white[(coord_x + elem[0], coord_y + elem[1], coord_z + elem[2])] += 1
    return neighbouring_black_cubes
        
def turn_black_to_white(blacks_to_be_turned, black_tiles):
    for key, value in blacks_to_be_turned.items():
        black_tiles.pop(key)
    return 0

def turn_white_to_black(neighbouring_white, black_tiles):
    for key, value in neighbouring_white.items():
        if value == 2:
            black_tiles[key] = 1
    return 0
    
main()
