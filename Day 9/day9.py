def main():
    numbers = get_input()
    # print(numbers)
    s1_result = part1(numbers)
    part2(numbers, s1_result)


def part1(numbers):
    preamble_size = 25
    rider = 0
    for elem in numbers[preamble_size:]:
        # print("Starting number: ", numbers[rider + preamble_size])
        # print("Numbers to consider: ", numbers[rider:rider + preamble_size])
        possible_sums = get_possible_sums(numbers[rider:rider + preamble_size])
        if numbers[rider + preamble_size] not in possible_sums:
            temp = numbers[rider + preamble_size]
            print(temp)
            return temp
        rider += 1

def part2(numbers, s1_result):
    # print("hledam", s1_result)
    for i in range(len(numbers)):
        temp_figures = []
        for j in range(i, len(numbers)):
            temp_figures.append(numbers[j])
            if sum(temp_figures) == s1_result:
                lo, hi = get_lo_hi(temp_figures)
                # print("Found it!", temp_figures, lo, hi)
                print (lo + hi)
                return
            elif sum(temp_figures) > s1_result:
                break
    return

def get_possible_sums(list_numbers):
    possible_sums = []
    delka = len(list_numbers)
    for i in range(delka):
        for j in range(delka):
            if i != j:
                possible_sums.append(list_numbers[i] + list_numbers[j])
    return possible_sums
    
def get_input():
    f = open("input.txt", "r")
    numbers = []
    for line in f:
        numbers.append(int(line[:-1]))
    return numbers

def get_lo_hi(temp_figures):
    lo = temp_figures[0]
    hi = temp_figures[0]
    for elem in temp_figures:
        if elem < lo:
            lo = elem
        elif elem > hi:
            hi = elem
    return lo, hi

main()
