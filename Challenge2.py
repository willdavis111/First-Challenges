
def crossing(hall):
    hall = hall.replace('-', '')
    right = '>'
    left = '<'
    left_list = []
    right_list = []
    count = -1
    for item in hall:
        count += 1
        count2 = 0
        if item == right:
            right_list.append(count)
        elif item == left:
            left_list.append(count)
        for emp in right_list:
            for emp2 in left_list:
                if emp < emp2:
                    count2 += 2
    print(count2)

hall1 = ">----<"
hall2 = '>>--<-->>-<'
hall3 = ">>--<-->>-<><----<"
crossing(hall2)