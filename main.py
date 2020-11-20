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
    print('{}|{}|{}'.format(plays_made[0][0],plays_made[1][0],plays_made[2][0]))
    print('-+-+-')
    print('{}|{}|{}'.format(plays_made[0][1],plays_made[1][1],plays_made[2][1]))
    print('-+-+-')
    print('{}|{}|{}'.format(plays_made[0][2],plays_made[1][2],plays_made[2][2]))

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
    while(player_choice > 9 and player_choice < 1):
        for i in range(len(plays_made)):
            for j in range(len(plays_made)):
                if(player_choice <= 3 and player_choice >= 1):
                    if(plays_made[0][player_choice - 1] == 'X' or plays_made[0][player_choice - 1] == 'O'):
                        print('Error, You cannot place your counter there')
                        player_choice = int(input('Enter where you want to place your counter corresponding to the avaliable spaces on the Game Board (1-9): '))
                elif(player_choice <= 6 and player_choice >= 4):
                    if(plays_made[1][player_choice - 1] == 'X' or plays_made[1][player_choice - 1] == 'O'):
                        print('Error, You cannot place your counter there')
                        player_choice = int(input('Enter where you want to place your counter corresponding to the avaliable spaces on the Game Board (1-9): '))
                elif(player_choice <= 9 and player_choice >= 7):
                    if(plays_made[2][player_choice - 1] == 'X' or plays_made[2][player_choice - 1] == 'O'):
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
    if(which_player % 2) != 0:
        if(player_choice <= 3 and player_choice >= 1):
            plays_made[player_choice - 1][0] = 'X'
        elif(player_choice <= 6 and player_choice >= 4):
            plays_made[player_choice - 4][1] = 'X'
        elif(player_choice <= 9 and player_choice >= 7):
            plays_made[player_choice - 7][2] = 'X'
                        
    else:
        if(player_choice <= 3 and player_choice >= 1):
            plays_made[player_choice - 1][0] = 'O'
        elif(player_choice <= 6 and player_choice >= 4):
            plays_made[player_choice - 4][1] = 'O'
        elif(player_choice <= 9 and player_choice >= 7):
            plays_made[player_choice - 7][2] = 'O'
    #reprints the game board
    gameboard(plays_made)

    return plays_made

def checking_full(plays_made):
    """
    Purpose:
        checks to see if the game board is full with X's 
        or O's
    Use:
        is_full = checking_full(plays_made)
    -----------------------------------------------------
    Parameters:
        plays_made - the list that holds the information 
        of where players' counters are already placed and 
        where they aren't
    Returns:
        is_full - a True or False statement that tells the
        game if the game board is full or not
    """
    
    counter = 0
    for i in range(len(plays_made)):
        for j in range(len(plays_made)):
            if(plays_made[i][j] == 'X' or plays_made[i][j] == 'O'):
                counter += 1
    #from the start of the game, the game board isn't filled so that's why is_full is starting at False 
    is_full = False
    if(counter == 9):
        is_full = True

    return is_full

def game_condition(plays_made, counter):
    """
    Purpose:
        checks to see if anyone has won the game or not
    Use:
        game_condition()
    -----------------------------------------------------
    Parameters:
        plays_made - the list that holds the information 
        of where players' counters are already placed and 
        where they aren't
        counter - the player's counter 
    Returns:
        is_won - a True or False statement that tells the
        game if someone has won or not
    """
    is_won = False
    for i in range(len(plays_made)):
        for j in range(len(plays_made)):
            if(plays_made[0][j] == counter and plays_made[1][j] == counter and plays_made[2][j] == counter):
                is_won = True
            elif(plays_made[i][0] == counter and plays_made[i][1] == counter and plays_made[i][2] == counter):
                is_won = True
            elif(plays_made[0][0] == counter and plays_made[1][1] == counter and plays_made[2][2] == counter):
                is_won = True
            elif(plays_made[2][0] == counter and plays_made[1][1] == counter and plays_made[0][2] == counter):
                is_won = True

    return is_won
    

def play_again():
    """
    Purpose:
        It is a simple function that asks the user if they
        want to play again
    Use:
        play_again()
    -----------------------------------------------------
    Parameters:
        None
    Returns:
        None
    """
    play_again = input('Would you like to play again? (y/n): ')
    if(play_again.lower() == 'y' or play_again.lower() == 'yes'):
        main()

    return

def main():
    #plays_made starts with values 1-9 as a way to show what's the original position of each box  
    plays_made = [[1,4,7],[2,5,8],[3,6,9]]
    #prints the game board once for now
    gameboard(plays_made)
    which_player = 1
    is_won = False
    while(is_won != True):
        if(which_player % 2) != 0:
            counter = 'X'
        else:
            counter = 'O'
        player_choice = position_chosen(plays_made)
        update_board(plays_made, player_choice,which_player)
        is_won = game_condition(plays_made, counter)
        if(is_won):
            if(counter == 'X'):
                print('Player One Won')
            else:
                print('Player Two Won')

        is_full = checking_full(plays_made)
        if(is_full):
            print('It is a Cat Game, No One Won')

        which_player += 1
        
    #asks the user if they want to play again    
    play_again()

#calls the main method
main()