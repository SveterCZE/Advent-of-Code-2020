def main():
    numbers = get_input()
    part1(numbers)
    part2(numbers)
    
def get_input():
    f = open("input.txt", "r")
    numbers = []
    for line in f:
        numbers.append(int(line[:-1]))
    return sorted(numbers)

def part1(numbers):
    joltage = 0
    jolt1 = 0
    jolt3 = 0
    maximum = numbers[len(numbers) - 1] + 3
    for elem in numbers:
        if elem - joltage == 1:
            jolt1 += 1
            joltage +=1
        elif elem - joltage == 3:
            jolt3 += 1
            joltage += 3
    if maximum - joltage == 1:
        jolt1 += 1
        joltage +=1
    if maximum - joltage == 3:
        jolt3 += 1
        joltage +=3
    print (jolt1 * jolt3)
    return 0

def part2_recur(numbers, joltage, maximum):
    if maximum - joltage == 3:
        # print("Ahoj")
        return 1
    elif len(numbers) == 0:
        return 0
    else:
        x = 0
        for i in range(len(numbers)):
            jolt_diff = numbers[i] - joltage
            if jolt_diff >= 1 and jolt_diff <= 3:
                x = x + part2_recur(numbers[i:], joltage + jolt_diff, maximum)
    return x    

def part2_recur_memo(numbers, joltage, maximum, results):
    if maximum - joltage == 3:
        # print("Ahoj")
        return 1
    elif len(numbers) == 0:
        return 0
    else:
        x = 0
        for i in range(len(numbers)):
            jolt_diff = numbers[i] - joltage
            if jolt_diff >= 1 and jolt_diff <= 3:
                if str(numbers[i:]) in results:
                    x = x + results[str(numbers[i:])]
                else:
                    results[str(numbers[i:])] = part2_recur_memo(numbers[i:], joltage + jolt_diff, maximum, results)
                    x = x + results[str(numbers[i:])]          
    return x

def part2(numbers):
    joltage = 0
    maximum = numbers[len(numbers) - 1] + 3
    results = {}
    # x = part2_recur(numbers, joltage, maximum)
    y = part2_recur_memo(numbers, joltage, maximum, results)
    print(y)
          
main()
