# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 00:55:09 2021

@author: petrs
"""

def main():
    p1, p2 = get_initial_input()
    part1(p1.copy(), p2.copy())
    part2(p1.copy(), p2.copy())
    return
    
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

def part2(p1, p2):
    winning_player, winning_hand = recursive_game(p1,p2)
    print(counter(winning_hand))    

def recursive_game(p1, p2):
    memo = []
    while True:
        if p1 in memo:
            return 1, p1
        else:
            memo.append(p1.copy())
        played = [p1[0], p2[0]]
        p1.pop(0)
        p2.pop(0)
        # Check if recursive combat occurs
        if played[0] <= len(p1) and played[1] <= len(p2):
            winner, his_hand = recursive_game(p1.copy()[:played[0]], p2.copy()[:played[1]])
            if winner == 1:
                    p1.append(played[0])
                    p1.append(played[1])
            else:
                    p2.append(played[1])
                    p2.append(played[0])         
        # Regular-non-recursive combat
        else:
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
                return 2, p2
            else:
                return 1, p1
main()
