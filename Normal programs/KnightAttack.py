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

    q_x=int(input("king's location:\n x: "))
    q_y=int (input(" y: "))
    # king attack
    try:
        boardkn[q_y-1][q_x] = " "
    except:
        pass

    try:
        boardkn[q_y-2][q_x] = " "
    except:
        pass

    try:
        boardkn[q_y][q_x] = " "
    except:
        pass

    try:
        boardkn[q_y-2][q_x-2] = " "

    except:
        pass

    try:
        boardkn[q_y][q_x-2] = " "

    except:
        pass

    try:
        boardkn[q_y-1][q_x-2] = " "

    except:
        pass

    try:

        boardkn[q_y][q_x-1] = " "

    except:
        pass

    try:

        boardkn[q_y-2][q_x-1] = " "
    except:
        pass   
    # king's position
    boardkn[q_y-1][q_x-1] = "K"

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