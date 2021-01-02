def load():
    field = []
    with open("input.txt", "r", encoding = "utf8") as f:
        for line in f:
            line_list = []
            for elem in line:
                if elem != "\n":
                # print (elem)
                    line_list.append(elem)
            field.append(line_list)
    # print(len(field))
    # print(field)
    return field

def part1():
    trees = 0
    coord_x = 0
    coord_y = 0
    field = load()
    delitel = len(field[0])
    while coord_x < len(field):
        if check_tree(field, coord_x, coord_y) == True:
            trees += 1
        coord_x += 1
        coord_y += 3
        coord_y = coord_y % delitel
        # print(coord_x)
    
    print(trees)

def part2():
    method = [(1,1), (3, 1), (5, 1), (7,1), (1,2)]
    trees_sum = 1
    field = load()
    delitel = len(field[0])
    for elem in method:
        coord_x = 0
        coord_y = 0
        trees = 0
        while coord_x < len(field):
            if check_tree(field, coord_x, coord_y) == True:
                trees += 1
            coord_x += elem[1]
            coord_y += elem[0]
            coord_y = coord_y % delitel
            # print(coord_x)    
        # print(trees)
        trees_sum = trees_sum * trees
    print(trees_sum)

    
def check_tree(field, coord_x, coord_y):
    if field[coord_x][coord_y] == "#":
        return True
    else:
        return False

part1()
part2()
