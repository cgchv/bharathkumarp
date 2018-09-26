print("Welcome to Magic Number game")
board=[int( ) for i in range(9)]

def print_board():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])
    print(row1)
    print(row2)
    print(row3)
def player_move(icon):
    if icon=="A":
        number=1
    elif icon=="B":
        number=2
    print("Your turn player {}".format(number))
    
    choice,index=raw_input("Choose an index and enter the number(1 to 9) ex: 1 2").split()
    choice=int(choice)
    index=int(index)
    if board[index-1]== ' ' or board[index-1]==0:
        board[index-1]=choice
    else:
        print()
        print("The space is taken")
def is_victory(icon):
    
    if((board[0]+board[1]+board[2]==7) or (board[0]+board[1]+board[2]==14) or (board[0]+board[1]+board[2]==21)) or\
     ((board[3]+board[4]+board[5]==7) or (board[3]+board[4]+board[5]==14) or (board[3]+board[4]+board[5]==21)) or\
     ((board[6]+board[7]+board[8]==7) or (board[6]+board[7]+board[8]==14) or (board[6]+board[7]+board[8]==21)) or\
     ((board[0]+board[3]+board[6]==7) or (board[0]+board[3]+board[6]==14) or (board[0]+board[3]+board[6]==21)) or\
     ((board[1]+board[4]+board[7]==7) or (board[1]+board[4]+board[7]==14) or (board[1]+board[4]+board[7]==21)) or\
     ((board[2]+board[5]+board[8]==7) or (board[2]+board[5]+board[8]==14) or (board[2]+board[5]+board[8]==21)) or\
     ((board[0]+board[4]+board[8]==7) or (board[0]+board[4]+board[8]==14) or (board[0]+board[4]+board[8]==21)) or\
     ((board[2]+board[4]+board[6]==7) or (board[2]+board[4]+board[6]==14) or (board[2]+board[4]+board[6]==21)) :
        return True
    else:
        return False
    
    
    
    
    
while True:
    print_board()
    player_move("A")
    print_board()
    if is_victory("A"):
        print("A wins! Congratulations")
        break
    player_move("B")
    if is_victory("B"):
        print_board()
        print("B wins! Congratulations")
        break
  


