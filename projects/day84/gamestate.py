
def checkgamestate(grid,curr_player):
    if ((grid[0][0] == grid[0][1] == grid[0][2] != "") or 
        (grid[1][0] == grid[1][1] == grid[1][2] != "") or
        (grid[2][0] == grid[2][1] == grid[2][2] != "") or 

        (grid[0][0] == grid[1][0] == grid[2][0] != "") or
        (grid[0][1] == grid[1][1] == grid[2][1] != "") or
        (grid[0][2] == grid[1][2] == grid[2][2] != "") or

        (grid[0][0] == grid[1][1] == grid[2][2] != "") or
        (grid[0][2] == grid[1][1] == grid[2][0] != "")):
        

        print(f"{curr_player} Wins!!!")
        return True

if "__main__" == __name__ :
    checkgamestate([["X","X","X"],["","",""],["","",""]],"player1")
    checkgamestate([["","",""],["X","X","X"],["","",""]],"player2")
    checkgamestate([["","",""],["","",""],["X","X","X"]],"player3")
    checkgamestate([["X","",""],["X","",""],["X","",""]],"player4")
    checkgamestate([["","X",""],["","X",""],["","X",""]],"player5")
    checkgamestate([["","","X"],["","","X"],["","","X"]],"player6")
    checkgamestate([["-1","-1","-1"],["-1","-1","X"],["-1","-1","X"]],"player7")
    checkgamestate([["","",""],["","","X"],["","",""]],"player8")

