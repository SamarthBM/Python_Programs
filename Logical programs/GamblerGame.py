"""
* @Author: Samarth BM.
* @Date: 2021-09-12 20:10  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-12 20:10 
* @Title: :To simulate the gambler game.
"""

import random

def gambler_game():
    """
    Description:
        This function is to simulate the gambler game.
        The stake and goal are taken as input.
        Random function is used to win and loose the player.
        Game is continued till player stake is 0 or is equal to goal.

    """    

    try:
        stake = int(input("Enter the stake amount: "))
        goal = int(input("Set a goal amount to win: "))

        win = 0
        loss = 0
        num_of_bets = 0

        if(stake > 0 and goal > stake):
            while not(stake == 0 or stake == goal): # Keeps looping until stake is 0 or equal to goal
                gamble = random.randint(0,1) # Generates two random numbers 0 and 1
                num_of_bets += 1

                if gamble == 0:
                    stake += 1
                    win += 1
                else:
                    stake -= 1
                    loss += 1
        else:
            print("Enter a valid stake and goal amount")

        print("Number of times won is: ", win)
        print("Number of tmes lost is: ", loss)
        print("Total bets placed is: ", num_of_bets)

        # Calculating win and loss percentage
        win_percentage = (win/num_of_bets)*100
        loss_percentage = (loss/num_of_bets)*100

        print("Win percentage is: ", win_percentage)
        print("Loss percentage is: ", loss_percentage)

    except Exception as e:
        print("Exception occured is: ", e)
        
if __name__ == "__main__":
    gambler_game()