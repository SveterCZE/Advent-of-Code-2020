def main():
    card, door = get_input()
    # card, door = 5764801, 17807724
    temp = 7
    i = 1
    card_loop_size = 0
    door_loop_size = 0
    # Getting loop sizes 
    while True:
        temp *= 7
        temp = temp % 20201227
        i += 1
        if temp == card:
            card_loop_size = i
        if temp == door:
            door_loop_size = i        
        if card_loop_size != 0 and door_loop_size != 0:
            break
    # print(card_loop_size, door_loop_size)
    # get keys based on loop sizes
    enc_key1 = 1
    for i in range(card_loop_size):
        enc_key1 *= door
        enc_key1 = enc_key1 % 20201227
        # print(temp)
   
    enc_key2 = 1
    for i in range(door_loop_size):
        enc_key2 *= card
        enc_key2 = enc_key2 % 20201227
    if enc_key1 == enc_key2:
        print(enc_key1)
    else:
        print("Fail")

    
    
def get_input():
    f = open("input.txt", "r")
    keys = []
    for line in f:
        keys.append(int(line[:-1]))
    return keys[0], keys[1]

main()
