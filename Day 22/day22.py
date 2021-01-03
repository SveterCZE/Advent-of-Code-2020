def main():
    p1, p2 = get_initial_input()
    part1(p1, p2)
    
def get_initial_input():
    f = open("input.txt", "r")
    p1 = []
    p2 = []
    p2_act = False
    for line in f:
        if "Player 2:" in line:
            p2_act = True
        if line[:-1].isnumeric() == True and p2_act == False:
            p1.append(int(line))
        elif line[:-1].isnumeric() == True and p2_act == True:
            p2.append(int(line))
    return p1, p2

def game(p1, p2):
    while True:
        played = [p1[0], p2[0]]
        p1.pop(0)
        p2.pop(0)
        if played[0] > played[1]:
            played.sort(reverse = True)
            for elem in played:
                p1.append(elem)
        else:
            played.sort(reverse = True)
            for elem in played:
                p2.append(elem)
        if len(p1) == 0 or len(p2) == 0:
            if len(p1) == 0:
                return p2
            else:
                return p1

def counter(winning_hand):
    score = 0
    multiplier = len(winning_hand)
    for elem in winning_hand:
        score += elem*multiplier
        multiplier -= 1
    return score

def part1(p1, p2):
    winning_hand = game(p1, p2)
    print(counter(winning_hand))
    

main()
