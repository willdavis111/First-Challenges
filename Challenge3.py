def grid(num, dest):
    global actual
    for x in range(0, 8):
        min_num = x * 8
        max_num = (x+1) * 8
        if max_num > num >= min_num:
            gy = x
            gx = num - (8 * x)
    starrdxy = (gy, gx)
    for x in range(0, 8):
        min_num = x * 8
        max_num = (x+1) * 8
        if max_num > dest >= min_num:
            dy = x
            dx = dest - (8 * x)
    dest1 = (dy, dx)
    move = 0
    expanded_list = [starrdxy]
    run = True
    actual = []
    while run:
    # for go in range(0, 12):
        move += 1
        for b in expanded_list:
            one_move(b[0], b[1], actual)
        for c in actual:
            if c not in expanded_list:
                expanded_list.append(c)
        if any(one == dest1 for one in expanded_list):
            run = False
    if num == dest:
        move = 0
    print(move)

def one_move(gy, gx, actual):
    s1 = ((gy - 2), (gx - 1))
    d1 = ((gy - 2), (gx + 1))
    s2 = ((gy - 1), (gx - 2))
    d2 = ((gy - 1), (gx + 2))
    s3 = ((gy + 2), (gx - 1))
    d3 = ((gy + 2), (gx + 1))
    s4 = ((gy + 1), (gx - 2))
    d4 = ((gy + 1), (gx + 2))
    full = [s1,d1,s2,d2,s3,d3,s4,d4]
    for spot in full:
        if 0 <= spot[0] < 8 and 0 <= spot[1] < 8:
            actual.append(spot)

start = 1
end = 5
grid(start, end)