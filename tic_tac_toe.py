# tic tac toe using numpy
import numpy as np 
playing_matrix = np.array([('0', '0', '0'),('0', '0', '0'),('0', '0', '0')]) # starting matrix

# sign of players
p1 = "O"
p2 = "X"

# adding sign in the base matrix
def adding_symbol(matrix,row,column,player_input):
    matrix[int(row),int(column)] = player_input


is_game_on =True

# checking the winning condition
def game_winning(matrix):
    print(matrix)
        # column checking
    for pos_column in range(3):
        win_case_p1 = 0
        win_case_p2 = 0
        for pos_row in range(3):
            if matrix[pos_row,pos_column] == p1:
                    win_case_p1 += 1
            if matrix[pos_row,pos_column] == p2:
                    win_case_p2 += 1
            if win_case_p1 == 3:        
                    print("Player one wins")
                    is_game_on = False
                    break
            if win_case_p2 == 3:
                    print("Player two wins")
                    is_game_on = False
                    break
    # row checking
    for pos_row in range(3):
        win_case_p1 = 0
        win_case_p2 = 0
        for pos_column in range(3):
            if matrix[pos_row,pos_column] == p1:
                win_case_p1 += 1
            if matrix[pos_row,pos_column] == p2:
                win_case_p2 += 1
            if win_case_p1 == 3:        
                print("Player one wins")
                is_game_on = False
                break
            if win_case_p2 == 3:
                print("Player two wins")
                is_game_on = False
                break
    # diagonal checking
    win_case_p1 = 0
    win_case_p2 = 0
    for pos in [(0,0),(1,1),(2,2)]:
        if matrix[pos] == p1:
            win_case_p1 += 1            
        if matrix[pos] == p2:
            win_case_p2 += 1                        
        if win_case_p1 == 3:        
                print("Player one wins")
                is_game_on = False
                break
        if win_case_p2 == 3:
                print("Player two wins")
                is_game_on = False
                break
    
    for pos in [(0,2),(1,1),(2,0)]:
        if matrix[pos] == p1:
            win_case_p1 += 1    
            print(win_case_p1)        
        if matrix[pos] == p2:
            win_case_p2 += 1                        
        if win_case_p1 == 3:        
                print("Player one wins")
                is_game_on = False
                break
        if win_case_p2 == 3:
                print("Player two wins")
                is_game_on = False
                break

# game loop
while is_game_on:
    p1_row_input = input("Player one row input(0/1/2):")
    p1_column_input = input("Player one column input(0/1/2):")
    adding_symbol(playing_matrix,p1_row_input,p1_column_input,p1)

    game_winning(playing_matrix)

    p2_row_input = input("Player two row input(0/1/2):")
    p2_column_input = input("Player two column input(0/1/2):")
    adding_symbol(playing_matrix,p2_row_input,p2_column_input,p2)    

    game_winning(playing_matrix)

