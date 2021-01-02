def main():
    coordinates = get_input()
    part1(coordinates)
    part2(coordinates)

def get_input():
    f = open("input.txt", "r")
    numbers = []
    for line in f:
        temp = []
        temp.append(line[0])
        temp.append(int(line[1:-1]))
        numbers.append(temp)
    return numbers

def part1(coordinates):
    SeverJih = 0
    VychodZapad = 0
    direction = "E"
    direction_dict = {"E": 90, "N": 0, "S": 180, "W": 270}
    for elem in coordinates:
        # print(SeverJih, VychodZapad)
        if elem[0] == "N":
            SeverJih += elem[1]
        elif elem[0] == "S":
            SeverJih -= elem[1]
        elif elem[0] == "E":
            VychodZapad += elem[1]
        elif elem[0] == "W":
            VychodZapad -= elem[1]
        elif elem[0] == "L":
            temp = (direction_dict[direction] - elem[1]) % 360
            if temp < 0:
                temp = temp + 360
            for key, item in direction_dict.items():
                if item == temp:
                    direction = key
                    # print(key)
        elif elem[0] == "R":
            temp = (direction_dict[direction] + elem[1]) % 360
            if temp < 0:
                temp = temp + 360
            for key, item in direction_dict.items():
                if item == temp:
                    direction = key
        elif elem[0] == "F":
            if direction == "N":
                SeverJih += elem[1]
            elif direction == "S":
                SeverJih -= elem[1]
            elif direction == "E":
                VychodZapad += elem[1]
            elif direction == "W":
                VychodZapad -= elem[1]  
    
    print(abs(SeverJih) + abs(VychodZapad))

def part2(coordinates):
    SeverJih_Lod = 0
    VychodZapad_Lod = 0
    # direction = "E"
    # direction_dict = {"E": 90, "N": 0, "S": 180, "W": 270}
    SeverJih_WP = 1
    VychodZapad_WP = 10
    for elem in coordinates:
        if elem[0] == "N":
            SeverJih_WP += elem[1]
        elif elem[0] == "S":
            SeverJih_WP -= elem[1]
        elif elem[0] == "E":
            VychodZapad_WP += elem[1]
        elif elem[0] == "W":
            VychodZapad_WP -= elem[1]
        elif elem[0] == "L":
            moves = elem[1] // 90
            for i in range(moves):
                temp1 = SeverJih_WP
                temp2 = VychodZapad_WP
                SeverJih_WP = temp2
                VychodZapad_WP = -temp1
        elif elem[0] == "R":
            moves = elem[1] // 90
            for i in range(moves):
                temp1 = SeverJih_WP
                temp2 = VychodZapad_WP      
                SeverJih_WP = -temp2
                VychodZapad_WP = temp1
        elif elem[0] == "F":
            SeverJih_Lod += elem[1] * SeverJih_WP
            VychodZapad_Lod += elem[1] * VychodZapad_WP
    print(abs(SeverJih_Lod) + abs(VychodZapad_Lod))

                
main()
