def kingattack(b_x, b_y, q_x, q_y):
    # creating empty board
    boardk = []
    for y in range(b_y):
        row = []
        for x in range(b_x):
            row.append(" ")
        boardk.append(row)

    # king attack
    try:
        boardk[q_y-1][q_x] = "o"
    except:
        pass

    try:
        boardk[q_y-2][q_x] = "o"
    except:
        pass

    try:
        boardk[q_y][q_x] = "o"
    except:
        pass

    try:
        boardk[q_y-2][q_x-2] = "o"

    except:
        pass

    try:
        boardk[q_y][q_x-2] = "o"

    except:
        pass

    try:
        boardk[q_y-1][q_x-2] = "o"

    except:
        pass

    try:

        boardk[q_y][q_x-1] = "o"

    except:
        pass

    try:

        boardk[q_y-2][q_x-1] = "o"
    except:
        pass
    
    # kings's position
    boardk[q_y-1][q_x-1] = "K"

    # printing board
    look = ""
    for y in boardk:
        for x in boardk[boardk.index(y)]:
            look += ("|"+x+"|  ")
        look += ("\n\n")
    print(look)
bx=int(input())
by=int (input())
qx=int(input())
qy=int(input())
kingattack(bx,by, qx,qy)