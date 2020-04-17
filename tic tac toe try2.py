board=["0","1","2","3","4","5","6","7","8",]
winner=None
gamestart=True
player_1="X"
player_2="O"
player=[player_1,player_2]


#=============================================Action in Board======================================================================
# display the board
def display_board():
    print(" ---------------------------")
    print("|    "+board[0]+"    |   "+board[1]+"    |    "+board[2]+"   |")
    print(" ---------------------------")
    print("|    "+board[3]+"    |   "+board[4]+"    |    "+board[5]+"   |")
    print(" ---------------------------")
    print("|    "+board[6]+"    |   "+board[7]+"    |    "+board[8]+"   |")
    print(" ---------------------------")
    
display_board()

def playgame():
    global gamestart
    count=0
    positions=[0,1,2,3,4,5,6,7,8]
    while gamestart:
        if(count%2==0):
            players=player[0]
            position=int(input(f"{players} Enter the position from [0-8]"))
            if position in positions:
                board[position]=players
                d=position
                positions.remove(d)
                count=count+1
                print("Count is ",count)
                check_win(players)
                print("Winner is ",winner)
                
                


            else:
                print("Position is not available it's occupied")
                print("positions available are:",positions)
                pass
        

            print(positions)
            display_board()

        elif(count%2==1):
            players=player[1]
            position=int(input(f"{players} Enter the position from [0-8]"))
            if position in positions:
                board[position]=players
                d=position
                positions.remove(d)
                count+=1
                print("Count is ",count)
                check_win(players)
                print("Winner is ",winner)

            else:
                print("Position is not available it's occupied")
                print("positions available are:",positions)
                pass
        
        
            print(positions)
            display_board()
        if(count>=9):
            gamestart=False
print(winner)

        
 
    
    
    
#==check if player won
def check_win(players):
    check_rows(players)
    check_cols(players)
    check_diag(players)

def check_rows(players):
    global gamestart
    global winner
    row1=board[0]==board[1]==board[2]==players
    row2=board[3]==board[4]==board[5]==players
    row3=board[6]==board[7]==board[8]==players
    if row1 or row2 or row3:
        winner=players
        gamestart=False
    if row1:
        winner=board[0]
    elif row2:
        winner=board[3]
    elif row3:
        winner=board[6]

    return winner

def check_cols(players):
    global gamestart
    global winner
    col1=board[0]==board[3]==board[6]==players
    col2=board[1]==board[4]==board[7]==players
    col3=board[2]==board[5]==board[8]==players
    if col1 or col2 or col3:
        winner=players
        gamestart=False
    if col1:
        winner=board[0]
    elif col2:
        winner=board[1]
    elif col3:
        winner=board[2]

    return winner

def check_diag(players):

    global gamestart
    global winner
    diag1=board[0]==board[4]==board[6]==players
    diag2=board[1]==board[4]==board[7]==players
    
    if diag1 or diag2 :
        gamestart=False
    if diag1:
        winner=board[0]
    elif diag2:
        winner=board[1]

    return winner


playgame()


