# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:39:24 2021

@author: petrs
"""

import re

def main():
    rules, messages = get_initial_input("input.txt")
    part1(rules, messages)
    rules, messages = get_initial_input("input4.txt")
    part1(rules, messages)
    
def get_initial_input(source):
    f = open(source, "r")
    rules = {}
    messages = []
    for line in f:
        if line[0] == "a" or line[0] == "b":
            messages.append(line[:-1]) 
        elif line[0].isnumeric() == True:
            rule = line.split(":")[0]
            if "|" in line:
                temp_list = []
                temp2_list = []
                rider = line.split()[1:]
                for elem in rider:
                    if elem == "|":
                        temp_list.append(temp2_list)
                        temp2_list = []
                    else:
                        temp2_list.append(elem)  
                temp_list.append(temp2_list)
                rules[rule] = temp_list
            elif line[-2] == "a" or line[-2] == "b":
                rules[rule] = line[-2]
            else:
                rules[rule] = line.split()[1:]

    return rules, messages
    
def part1(rules, messages):
    regex = "^" + regex_builder_v2(rules, "0", 0) + "$"
    match_counter = 0
    for elem in messages:
        if re.match(regex, elem) != None:
            match_counter += 1
    print(match_counter)
    return

    return temp
def regex_builder_v2(rules, selected_rule, recursive_depth):
    regex = ""
    regex_counter = 0
    for elem in rules[selected_rule]:
        if isinstance (elem, list):
            temp_regex = ""
            for item in elem:
                if isinstance (rules[item], list):
                    if recursive_depth < 20:
                        temp_regex += "(" + regex_builder_v2(rules, item, recursive_depth + 1) + ")"
                    else:
                        temp_regex += "()"
                elif isinstance (rules[item], str):
                    temp_regex += rules[item]
            if regex_counter == 0:
                temp_regex += "|"
                regex_counter += 1
            regex += temp_regex
        else:
            if isinstance (rules[elem], list):
                if recursive_depth < 20:
                    regex += "(" + regex_builder_v2(rules, elem, recursive_depth + 1) + ")"
                else:
                    regex += "()"
            elif isinstance (rules[elem], str):
                regex += rules[elem]

    return regex

main()