import math
def challenge1(area):
    global square_list
    square_list = []
    run = True
    while run:
        num = math.sqrt(int(area))
        i, d = divmod(num, 1)
        num2 = i ** 2
        area = int(area) - num2
        if area == 0:
            run = False
        formated = num2 if num2 % 1 else int(num2)
        square_list.append(formated)
    square_list = str(square_list)
    square_list = square_list.replace('[', '')
    square_list = square_list.replace(']', '')
    print(square_list)
    # return square_list

challenge1(24)