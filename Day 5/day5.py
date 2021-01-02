def load():
    field = []
    with open("input.txt", "r", encoding = "utf8") as f:
        for line in f:
            field.append(line[:-1])
    return field

def main():
    aircraft = {}
    ticket_IDs = []
    field = load()
    for elem in field:
        row = get_final_value(elem[:-3], 127)
        seat = get_final_value(elem[7:], 7)        
        fill_in_plane(row, seat, aircraft)        
        update_ticket_ID_list(get_ticket_ID(row, seat), ticket_IDs)        
    highest_ID = get_highest_ID(ticket_IDs)
    empty_ID = find_empty_seat(aircraft, ticket_IDs)        
    print (highest_ID)
    print (empty_ID)
    return 0
        
def get_final_value(elem, high_boundary):
    low_boundary = 0
    mid = (low_boundary + high_boundary + 1) // 2
    for char in elem:      
            if char == "F" or char == "L":
                high_boundary = high_boundary - mid
            if char == "B" or char == "R":
                low_boundary = low_boundary + mid
            mid = mid // 2
                # print(mid_boundary)
    return low_boundary

def get_ticket_ID(row, seat):
    return (row * 8) + seat

def fill_in_plane(row, seat, aircraft):
    if row in aircraft:
            aircraft[row].append(seat)
    else:
            aircraft[row] = [seat]

def get_highest_ID(ticket_IDs):
    temp = 0
    for elem in ticket_IDs:
        if elem > temp:
            temp = elem
    return temp

def find_empty_seat(aircraft, ticket_IDs):
    for key, value in aircraft.items():
        temp = 0
        for elem in value:
            temp = elem + temp
        if temp != 28:
            test_ticket_ID = get_ticket_ID(key, 28 - temp)
            if check_test_ID(test_ticket_ID, ticket_IDs) == True:
                return test_ticket_ID

def update_ticket_ID_list (ID, ticket_IDs):
    ticket_IDs.append(ID)

def check_test_ID(test_ticket_ID,ticket_IDs):
    if test_ticket_ID - 1 in ticket_IDs and test_ticket_ID + 1 in ticket_IDs:
        return True
    else:
        return False

main()
