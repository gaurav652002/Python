def KnightAttack(b_x, b_y, q_x, q_y):
    # creating empty board
    boardkn = []
    for y in range(b_y):
        row = []
        for x in range(b_x):
            row.append(" ")
        boardkn.append(row)

    # Knight attack
    try:
        boardkn[q_y-2][q_x+1] = "o"
    except:
        pass

    try:
        boardkn[q_y-3][q_x] = "o"
    except:
        pass

    try:
        boardkn[q_y][q_x+1] = "o"
    except:
        pass

    try:
        boardkn[q_y-3][q_x-2] = "o"
    except:
        pass

    try:
        boardkn[q_y][q_x-3] = "o"
    except:
        pass

    try:
        boardkn[q_y-2][q_x-3] = "o"
    except:
        pass

    try:
        boardkn[q_y+1][q_x-2] = "o"
        
    except:
        pass

    try:
        boardkn[q_y+1][q_x] = "o"
        
    except:
        pass
    # knight's position
    boardkn[q_y-1][q_x-1] = "Kn"


    #king's input

    k_x=int(input("king's location:\n x: "))
    k_y=int (input(" y: "))
    # king attack
    try:
        if boardkn[q_y-2][q_x+1]==boardkn[k_y-1][k_x] or boardkn[q_y-3][q_x]==boardkn[q_y-3][q_x]or boardkn[q_y][q_x+1==boardkn[q_y-3][q_x] or boardkn[q_y-3][q_x]==boardkn[q_y-3][q_x] or boardkn[q_y-3][q_x]==boardkn[q_y-3][q_x] or boardkn[q_y-3][q_x]==boardkn[q_y-3][q_x]

            boardkn[k_y-1][k_x] = "x"
    except:
        pass

    try:
        if
        boardkn[k_y-2][k_x] = " "
    except:
        pass

    try:
        boardkn[k_y][k_x] = " "
    except:
        pass

    try:
        boardkn[k_y-2][k_x-2] = " "

    except:
        pass

    try:
        boardkn[k_y][k_x-2] = " "

    except:
        pass

    try:
        boardkn[k_y-1][k_x-2] = " "

    except:
        pass

    try:

        boardkn[k_y][k_x-1] = " "

    except:
        pass

    try:

        boardkn[k_y-2][k_x-1] = " "
    except:
        pass   
    # king's position
    boardkn[k_y-1][k_x-1] = "K"

    # printing board
    look = ""
    for y in boardkn:
        for x in boardkn[boardkn.index(y)]:
            look += ("|"+x+"|  ")
        look += ("\n\n")
    print(look)
bx=int(input())
by=int (input())
qx=int(input())
qy=int(input())
KnightAttack(bx,by, qx,qy)