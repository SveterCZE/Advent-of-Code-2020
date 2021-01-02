def get_input():
    f = open("input.txt", "r")
    numbers = []
    for line in f:
        numbers.append(line[:-1])    
    bus_lines = []
    temp = []
    for char in numbers[1]:
        if char.isnumeric() == True:
            temp.append(char)
        else:
            if len(temp) > 0:
                new = ""
                for x in temp:
                    new += x
                bus_lines.append(int(new))
            temp = []
        
    return int(numbers[0]), bus_lines

def get_input2():
    f = open("input.txt", "r")
    numbers = []
    for line in f:
        numbers.append(line)    
    bus_lines = []
    temp = []
    for char in numbers[1]:
        if char.isnumeric() == True:
            temp.append(char)
        else:
            if len(temp) > 0:
                new = ""
                for x in temp:
                    new += x
                bus_lines.append(int(new))
            if char == "x":
                bus_lines.append("x")
            temp = []
        
    return bus_lines


def main():
    timestamp, bus_lines = get_input()
    part1(timestamp, bus_lines)
    bus_lines_v2 = get_input2() 
    part2(bus_lines_v2)
        
def part1 (timestamp, bus_lines):
    i = 0
    while True:
        for elem in bus_lines:
            if (timestamp + i) % elem == 0:
                print (elem * i)
                return
            else:
                continue
        i += 1

def part2(buses):
    bus_rider = 0 
    time_pointer = 1
    adder = 1
    
    while True:
        if time_pointer % buses[bus_rider] == (buses[bus_rider] - bus_rider) % buses[bus_rider]:
            if bus_rider == 0:
                adder = buses[bus_rider]
            else:
                adder = adder * buses[bus_rider]
            # if bus_rider + 1 != len(buses):
            try:
                while buses[bus_rider + 1] == "x":
                    bus_rider += 1
            except:
                pass
            bus_rider += 1
            # print(time_pointer)
        if bus_rider == len(buses):
            break    
        time_pointer += adder
    
    print(time_pointer)
    return

main()
