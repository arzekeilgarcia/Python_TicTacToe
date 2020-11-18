def gameboard(plays_made):
    """
    Purpose:
        Draws the game board for the game Tic Tac Toe
    Use:
        gameboard(plays_made)
    -----------------------------------------------------
    Parameters:
        plays_made - it is a list as a way to determine
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


def position_chosen():
    """
    Purpose:
        the function ask the player where they choose to 
        to place their counter
    Use:
        player_choice = position_chosen()
    -----------------------------------------------------
    Parameters:
        None  
    Returns:
        player_choice -  the place where the user puts his
        counter
    """
    player_choice = int(input('Enter where you want to place your counter corresponding to the avaliable spaces on the Game Board (1-9): '))
    while(player_choice > 9 and player_choice < 1):
        print('Error, You cannot place your counter there')
        player_choice = int(input('Enter where you want to place your counter corresponding to the avaliable spaces on the Game Board (1-9): '))

    return player_choice

def main():
    #plays_made starts with values 1-9 as a way to show what's the original position of each box  
    plays_made = [1,2,3,4,5,6,7,8,9]
    gameboard(plays_made)


#calls the main method
main()