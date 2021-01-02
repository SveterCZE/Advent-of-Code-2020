def main():
    target_step = 2020
    target_step_v2 = 30000000
    init_list = [0,13,1,8,6,15]
    part1(target_step, init_list)
    part1(target_step_v2, init_list)
    
def part1(target_step, init_list):
    i = 1
    memo = {}
    last_spoken = 0
    # Initialise the first list
    for elem in init_list:
        memo[elem] = [0, i]
        last_spoken = elem
        # print("Turn: ", i, "number spoken: ", last_spoken)
        i += 1
    # print(last_spoken, memo)    
    while i <= target_step:
        # Check if last spoken number had been spoken once or more times
        if memo[last_spoken][0] == 0:
            update_memo(0, i, memo)
            last_spoken = 0
        else:
            last_spoken = memo[last_spoken][1] - memo[last_spoken][0]
            update_memo(last_spoken, i, memo)
        # print("Turn: ", i, "number spoken: ", last_spoken)
        i += 1
    print(last_spoken)        

def update_memo(figure, i, memo):
    if figure in memo:
        memo[figure][0] = memo[figure][1]
        memo[figure][1] = i
    else:
        memo[figure] = [0, i]

main()
