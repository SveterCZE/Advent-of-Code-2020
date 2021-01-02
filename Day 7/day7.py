def load():
    field = []

    with open("input3.txt", "r", encoding = "utf8") as f:
        for line in f:
            temp = []
            for word in line.split(): 
                temp.append(word)
            field.append(temp)
    return field

def get_rules(field):
    rules = {}
    for item in field:
        # print(item)
        rules[(item[0] + " " + item[1])] = []
        for i in range(len(item)):
            if item[i].isnumeric() == True:
                rules[(item[0] + " " + item[1])].append((item[i], item[i+1] + " " + item[i+2]))
    return rules

def search_bags(rules, bag_type, types_found):
    matches = 0
    for key, value in rules.items():
        for elem in value:
            if elem[1] == bag_type and key not in types_found:    
                types_found.append(key)
                # print (key, elem)
                matches += 1
                matches = matches + search_bags(rules, key, types_found)
    return matches

def search_bags_v2(rules, bag_type, mezisoucet = 0):
    if len(rules[bag_type]) == 0:
        return 1
    else:
        temp = []
        for key, value in rules.items():            
            if key == bag_type:
                # print(key, value)
                temp.append(1)
                for elem in value:
                    # print(elem)
                    x = int(elem[0]) * search_bags_v2(rules, elem[1], mezisoucet)
                    temp.append(x)
                    # print(temp)
        return sum(temp)

def main():
    field = load()
    rules = get_rules(field)
    types_found = []
    task1 = search_bags(rules, "shiny gold", types_found)  
    task2 = search_bags_v2(rules, "shiny gold") - 1
    # print(rules)
    print(task1, task2)
main()
