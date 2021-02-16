#display the board 
grid = {'1':' ' , '2':' ' , '3':' ' , 
        '4':' ' , '5':' ' , '6':' ' , 
        '7':' ' , '8':' ' , '9':' '}

grid_keys = []
for key in grid:
    grid_keys.append(key)
#print(grid_keys)

def print_grid(grid):
    print(grid['1'] +'|'+grid['2']+'|'+grid['3'])
    print("-+-+-")
    print(grid['4'] +'|'+grid['5']+'|'+grid['6'])
    print("-+-+-")
    print(grid['7'] +'|'+grid['8']+'|'+grid['9'])
    

#start game 
def game():
    start = True
    state = "X"
    counter = 0


    while start:
        print_grid(grid)

        if state == "X": #player 1 turn
            pose = input("player X select postion.\n")
            
            if grid[pose] == ' ':
                grid[pose] = state
                counter += 1
                state = "O"
            else:
                print("this cell is filled select another . \n")
                continue
        
        else:
            pose = input("player O select postion.\n") #player 2 turn

            if grid[pose] ==' ':
                grid[pose] = "O"
                counter += 1
                state = "X"
            else:
                print("this cell os filled select another . \n")    
                continue
        
        #select winner
        if counter >= 5:
            #states to win
            #row win
            if grid['1'] == grid['2']==grid['3'] != ' ':
                print("\nwinner is :" , grid["1"] , "congratulation.\n")
                start = False
                break
            elif grid['4'] == grid['5']==grid['6'] != ' ':
                print("\nwinner is :" , grid["4"] , "congratulation.\n")
                start = False
                break
            elif grid['7'] == grid['8']==grid['9'] != ' ':
                print("\nwinner is :" , grid["7"] , "congratulation.\n")
                start = False
                break
            #cols win        
            elif grid['1'] == grid['4']==grid['7'] != ' ':
                print("\nwinner is :" , grid["1"] , "congratulation.\n")
                start = False
                break
            elif grid['2'] == grid['5']==grid['8'] != ' ':
                print("\nwinner is :" , grid["2"] , "congratulation.\n")
                start = False
                break
            elif grid['3'] == grid['6']==grid['9'] != ' ':
                print("\nwinner is :" , grid["3"] , "congratulation.\n")
                start = False
                break 
            #dignoal win
            elif grid['1'] == grid['5']==grid['9'] != ' ':
                print("\nwinner is :" , grid["1"] , "congratulation.\n")
                start = False
                break
            elif grid['3'] == grid['5']==grid['7'] != ' ':
                print("\nwinner is :" , grid["3"] , "congratulation.\n")
                start = False
                break

        #if the board full with out winner 
        if counter == 9:
            print(" \nNO WINNER \n ")
            start = False
            break
        
    #restart game
    r = input("Do you need to play agin?(y / n)\n ")
    if r == "y" or r == 'Y':
        for key in grid_keys:
            grid[key] = ' '

        game() 
    else:
        print("\n game ended \n")
                 
        
                

game()                       

        
    

