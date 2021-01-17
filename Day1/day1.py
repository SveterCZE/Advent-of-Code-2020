def main():
    figure = []
    with open("input.txt", "r", encoding = "utf8") as f:
        for line in f:
            figure.append(int(line[:4]))
    for i in range(len(figure)):
        for j in range(i + 1, len(figure)):
            if figure[i] + figure[j] == 2020:
                print (figure[i] * figure[j])

def part2():
    figure = []
    with open("input.txt", "r", encoding = "utf8") as f:
        for line in f:
            figure.append(int(line[:4]))
    for i in range(len(figure)):
        for j in range(i + 1, len(figure)):
            for k in range (i + 2, len(figure)):
                if figure[i] + figure[j] + figure[k] == 2020:
                    print (figure[i], figure[j], figure[k])
                    print (figure[i] * figure[j] * figure[k])
                    return

main()
part2()
