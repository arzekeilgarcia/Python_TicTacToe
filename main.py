#imports

#constants


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


def position_chosen(plays_made):
    """
    Purpose:
        the function ask the player where they choose to 
        to place their counter
    Use:
        player_choice = position_chosen()
    -----------------------------------------------------
    Parameters:
        plays_made - the list that holds the information 
        of where players' counters are already placed and 
        where they aren't 
    Returns:
        player_choice -  the place where the user puts his
        counter
    """
    player_choice = int(input('Enter where you want to place your counter corresponding to the avaliable spaces on the Game Board (1-9): '))
    while(player_choice > 9 and player_choice < 1 or plays_made[player_choice - 1] == 'X' or plays_made[player_choice - 1] == 'O'):
        print('Error, You cannot place your counter there')
        player_choice = int(input('Enter where you want to place your counter corresponding to the avaliable spaces on the Game Board (1-9): '))

    return player_choice

def update_board(plays_made, player_choice,which_player):
    """
    Purpose:
        updates the game board after the user chooses 
        where to place their counter on the game board
    Use:
        update_board()
    -----------------------------------------------------
    Parameters:
        plays_made - the list that holds the information 
        of where players' counters are already placed and 
        where they aren't
        player_choice - the choice that the player made of 
        where they wanted their counter to be placed 
        which_player - identifies which player selected to
        place down their counter
    Returns:
        plays_made - the list that holds the information 
        of where players' counters are already placed and 
        where they aren't
    """


    return

def main():
    #plays_made starts with values 1-9 as a way to show what's the original position of each box  
    plays_made = [1,2,3,4,5,6,7,8,9]
    #prints the game board once for now
    gameboard(plays_made)

    player_choice = position_chosen()
    update_board(player_choice)
    #call win condition function 
    #while loop to keep game running or not


#calls the main method
main()