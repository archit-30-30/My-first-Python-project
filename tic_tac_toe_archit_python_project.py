def print_board(a):
    print("",a[1]," │",a[2]," │ ",a[3]," ")
    print("────┼────┼────")
    print("",a[4]," │",a[5]," │ ",a[6]," ")
    print("────┼────┼────")
    print("",a[7]," │",a[8]," │ ",a[9]," ")
    
def print_instructions():
    print("\n----------- WELCOME TO TIC TAC TOE ------------\n\n")
    print_board(pos)
    print()
    
    players[0] = input("Entre your name Player 1 : ")
    players[1] = input("Entre your name Player 2 : ")
    
    print("\n-------- Instructions ---------")
    print("->",players[0],"you will using X")
    print("->",players[1],"you will using 0")
    print("-> Turn starts from",players[0])
    print("-> Potisions are like :-")
    print("  1 │  2 │ 3  ")
    print("────┼────┼────")
    print("  4 │ 5  │ 6  ")
    print("────┼────┼────")
    print("  7 │ 8  │ 9  ")
    print("-> press 1 to start the game")
    flag = input()    
    return flag

def startgame():
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            print("\nthis is ur turn",players[0])
            p = int(input("Please Enter postion : "))
            v = 'x'
            pos[p] = v
            print_board(pos)
            winner = win(v)
            if winner is "nobody":
                turn = 1
                continue
            else:
                print(players[0],"Won the match")
                break
        else:
            print("\nthis is ur turn",players[1])
            p = int(input("Please Enter postion : "))
            v = '0'
            pos[p] = v
            print_board(pos)
            winner = win(v)
            if winner is "nobody":
                turn = 0
                continue
            else:
                print(players[1],"Won the match")    
                break
    else:
        print("\n\nGame is Tie")
         
def win(v):
    for i in winning_conditions:
        if (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):
            winner = players[0]
            break
        elif (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):
            winner = players[1]
            break
    else:
        winner = "nobody"
    return winner

pos = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
players = ['','']
winning_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
flag = print_instructions()
if flag == '1' or flag == '1':
    startgame()
else:
    print("Invalid Entry")






  
