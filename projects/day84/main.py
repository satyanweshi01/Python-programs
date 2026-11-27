from random import choice

from utils import render_grid, alternate
from gamestate import checkgamestate

gameloop = True

players = [
    {
        "name":"Player1",
        "sign":"X"
    },
    {
        "name":"Player2",
        "sign":"O"
    }
]
# print(players[0]["name"],players[0]["sign"])
player_loop = alternate()

grid2d = [["","",""],["","",""],["","",""]]
next_player = next(player_loop)

while gameloop:
    
    print(f"{players[next_player]["name"]} \nSign : {players[next_player]["sign"]}")
    
    user_input = eval(input("Enter position(eg. (x,y)): "))
    
    input_x = int(user_input[0]) -1
    input_y = int(user_input[1]) -1

    # print(input_x,input_y)

    # print(type(input_x))
    # print(user_input, type(user_input))
    # try:
    #     if grid2d[input_x][input_y] == "":
    #         grid2d[input_x][input_y] = "X"
    #         render_grid(grid2d)
    #     else:
    #         print("the cell is already occupied")

    # except IndexError:
    #     print("The coordinates should be 1 to 3 not more not less")
    #     user_input = eval(input("Enter position(eg. (x,y)): "))
    #     input_x = int(user_input[0]) -1
    #     input_y = int(user_input[1]) -1

    #     if grid2d[input_x][input_y] == "":
    #         grid2d[input_x][input_y] = "X"
    #         render_grid(grid2d)

    if 0<=input_x<3 and 0<=input_y<3: 
        if grid2d[input_x][input_y] == "":

            grid2d[input_x][input_y] = players[next_player]["sign"] 
            render_grid(grid2d)
            if checkgamestate(grid2d, players[next_player]["name"]):
                gameloop = False
            next_player = next(player_loop)
            
        else:
            print("The cell is already occupied")
    else:
        print("The coordinates should be 1 to 3 not more not less")
    
    
    

# future additions (if time permits)
# 1. adding a computer mode
