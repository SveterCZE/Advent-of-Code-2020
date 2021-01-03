def main():
    vstup = get_input()
    curated_results2 = part1(vstup)
    part2(curated_results2)

def part1(vstup):
    list_of_allergens = get_list_allergens(vstup)
    curated_results = []
    counter = 0
    for elem in list_of_allergens:
        curated_results.append([])
        muj_list = []
        for item in vstup:
            if elem in item[1]:
                if len(muj_list) == 0:
                    # print(elem, item[1])
                    for ingredient in item[0]:
                        muj_list.append(ingredient)
                else:
                    break
        for item in vstup:
            if elem in item[1]:
                muj_temp_list = list(set(muj_list).intersection(item[0]))
                muj_list = muj_temp_list.copy()
        curated_results[counter] = [elem, muj_list]
        counter += 1
    curated_results2 = []
    while True:
        # Get cleary defined allergen
        for elem in curated_results:
            if len(elem[1]) == 1:
                temp = elem[1][0]
                curated_results2.append([elem[0], temp])
                curated_results.remove(elem)        
        # Clean other tables
        for elem in curated_results:
             if temp in elem[1]: 
                 elem[1].remove(temp) 
        if len(curated_results) == 0:
            break   
    curated_results2.sort()
    curated_results3 = []
    for elem in curated_results2:
        curated_results3.append(elem[1])   
    counter = 0
    for elem in vstup:
        for word in elem[0]:
            if word not in curated_results3:
                counter += 1
    print(counter)
    return curated_results2
    
def part2(curated_results2):
    outcome = ""
    for elem in curated_results2:
        outcome = outcome + elem[1] + ","
    print(outcome[:-1])
    return 0
                
def get_list_allergens(vstup):
    list_of_allergens = []
    for elem in vstup:
        for item in elem[1]:
                if item not in list_of_allergens:
                    list_of_allergens.append(item)
    return list_of_allergens

def get_input():
    f = open("input.txt", "r")
    vstup = []
    for line in f:
        potraviny = []
        alergeny = []
        alerg = False
        for elem in line.split(" "):
            if elem[0] == "(":
                alerg = True
            if alerg == False:
                potraviny.append(elem)
            elif alerg == True:
                if "contains" not in elem:
                    if elem[-1] == ",":    
                        alergeny.append(elem[:-1])
                    else:
                        alergeny.append(elem)
        alergeny[-1] = alergeny[-1][:-2]
        vstup.append([potraviny, alergeny])
    return vstup

main()
