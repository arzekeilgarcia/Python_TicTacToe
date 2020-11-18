def gameboard(plays_made):
    """
    Purpose:
        Draws the game board for the game TicTacToe
    Use:
        gameboard(plays_made)
    -----------------------------------------------------
    Parameters:
        plays_made = it is a list as a way to determine
        that holds where a player's piece is held  
    Returns:
        None
    """
    print('{}|{}|{}'.format(plays_made[0],plays_made[1],plays_made[2]))
    print('-|-|-')
    print('{}|{}|{}'.format(plays_made[3],plays_made[4],plays_made[5]))
    print('-|-|-')
    print('{}|{}|{}'.format(plays_made[6],plays_made[7],plays_made[8]))

    return

    
def main():
    #plays_made starts with values 1-9 as a way to show what's the original position of each box  
    plays_made = [1,2,3,4,5,6,7,8,9]
    gameboard(plays_made)


#calls the main method
main()