def load():
    field = []
    temp = []
    with open("input.txt", "r", encoding = "utf8") as f:
        for line in f:
            if line == "\n":
                # print("empty")
                field.append(temp)
                temp = []
            else:
                temp.append(line[:-1])
    return field


def part1(field):
    celkem = 0
    for elem in field:
        temp = "".join(elem)
        chars = []
        for char in temp:
            if char not in chars:
                chars.append(char)
        celkem += len(chars)
    return celkem

def part2(field):
    temp = 0
    for elem in field:
        chars = [c for c in elem[0]]
        chars_disq = []
        for item in elem:
            # print(item)
            for c in chars:
                if c not in item:
                    if c not in chars_disq:
                        chars_disq.append(c)
            
        # print(chars)
        # print(chars_disq)
        chars_pass = []
        for i in chars:
            if i not in chars_disq:
                chars_pass.append(i)
        temp = temp + len(chars_pass)
    return temp

def main():
    field = load()
    first = part1(field)
    second = part2(field)
    print(first, second)
    return 0

main()
