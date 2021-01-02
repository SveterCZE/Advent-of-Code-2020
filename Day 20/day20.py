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

def part2(tiles, tiles_numbers, shody, corners):      
    # TODO
    return

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
