board_pos = [[1,2,3],[4,5,6],[7,8,9]]
players = ['x', 'o']
turn = 0

#this function creates a board and displays a message
def create_board():   
#creates the board with numbers in each cell
    for i in range(0,3):
        for j in range(0,3):
            bar = '|' if j != 2 else '' #prevents extra bar from showing up
            print(f' {board_pos[i][j]}' + f'{bar}', end = '')
        print()
        print('--+--+--') if i != 2 else print('')

#message to display depending on state of the game
    #board is full, these functions are defined later in the code
    if full_check() == True:
        print("Draw")
    elif final_check() == False:
        print(f"{players[turn]}'s turn")
    else:
        print(f"{players[turn]} wins")

#checks if there is a horizontal win
def hz_check():
    for i in range(0, 3):
        if board_pos[i][0] == board_pos[i][1] == board_pos[i][2]:
            return True
        
    return False

#checks if there is a vertical win
def vt_check():
    for j in range(0, 3):
        if board_pos[0][j] == board_pos[1][j] == board_pos[2][j]:
            return True

    return False

#checks if there is a diagonal win
def diagonal_check():
    if board_pos[0][0] == board_pos[1][1] == board_pos[2][2]:
        return True
    
    elif board_pos[0][2] == board_pos[1][1] == board_pos[2][0]:
        return True
    
    return False

#checks if the board is full by checking each individual cell and seeing if its either x or o
#it returns false when it comes across an unused number
#its important to keep the return True outside of the loop so that everything is checked before this value is returned
def full_check():

    for i in board_pos:
        for j in i:
            if j != 'x' and j != 'o':
                return False

    return True

#lets the user choose where to place their x or o on the grid
#it also has input validation and alternates between the players

def user_input():
    #global makes the changes to these variables carry over to the rest of the program
    #its better to use function parameters instead but it stopped working when I tried this
    global players
    global turn

#contains all of the unused spaces in each grid
    free_spaces = []
    
#the first line of this looks at the three lists in board_pos which represent each row
#the second line looks at the three values within each of the three lists
#the third line looks at each of these values and checks them 
#if they aren't x or o then they are appended
    for i in board_pos:
        for j in i:
            if j != 'x' and j != 'o':
                free_spaces.append(j)
    

    condition = True
    while condition:
        try:   
            move = int(input(f'select a number: {free_spaces}: '))

#converts chosen number into grid value
            if move in free_spaces:
                if move <= 3:
                    i = 0
                    j = move-1
                elif move <= 6:
                    i = 1
                    j = (move-1) % 3
                elif move <= 9:
                    i = 2
                    j = (move-1) % 3
                
                board_pos[i][j] = players[turn]

#changes the player from x to o and vice versa by alternating the player index (turn variable) between 0 and 1
                if turn == 0 and final_check() == False:
                    turn += 1
                elif turn == 1 and final_check() == False:
                    turn -= 1
                else:
                    turn = turn
            
#This is very important as it creates the next board after the player has been changed
                print()
                create_board()
                condition = False
            
            else:
                raise ValueError

#if the user types something that isn't in the empty spaces 
        except ValueError:
            print('Your input is not one of the empty spaces')

#groups all of the check functions together and returns a value to determine if the game is over
def final_check():

    if vt_check() == True:
        return True

    elif hz_check() == True:
        return True

    elif diagonal_check() == True:
        return True
    
    elif full_check() == True:
        return True

#if none of the checks are equal to true, the function returns false and the game keeps going
    else:
        return False

#this function creates a loop that keeps allowing user input in each iteration until there is a winner determined by final check
def play():
    #creates an updated board after every move
    create_board()

    while final_check() == False:
        user_input()
        
play()