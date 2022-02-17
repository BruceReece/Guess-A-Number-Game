#  CSC-171 Week #5 Program example Random Number Guessing Game
#
#  Programmed by:  prof aw
#  date:  10/06/2016
#  Edited by: Bruce Reece
#  Date edited: 09/24/2018


""" Description:  Write a program that generates a random number in the range of 1 - 100
    and asks the user to guess the number; if they guess correctly, congratulate them
    for winning the game (and stop playing).  Otherwise, give them some help by telling
    them if their guess was " Too high" or "Too low".  Give them 7 tries to win.

    To think about .... you should always be able to guess the correct number within
    7 tries if you 'guess smart'  """

# demonstrates topics from weeks 1 - 5:
#     loops, decisions, randomness


import random  # need to import the random module to generate random number

# instructions
def inst():
      print(" I'm thinking of a number between 1 and 100... can you guess it? ")
      print("\n You will be granted seven tries to get it right.... I will give")
      print(" you hints....whether your guess is too high or too low to help you")


def playerGess():
      while True:  #############################This group of codes will only accept strings or char only
           playerNam = input("What is your name \n")
           if not playerNam.isdigit():
                 break;
           else:
                 print(" Invalid input...") ##################################
      secretNumber = random.randint(1,100) # generate a random secret number between 1 and 100
      for guessNumber in range (1,8):  # allows 1 - 7 guesses
            print(playerNam +" guess number " + str(guessNumber) + " > ", end='')
            userGuess = input()
            if userGuess.isdigit(): #////////////////////////////////////////////////
               userGuess = int(userGuess)
               if (userGuess == secretNumber):
                  print (" Congratulations " + playerNam+", you guessed the secret number, " + str(secretNumber)\
                  + " in " + str(guessNumber) + " tries, you are a smart cookie!")
                  break;
               elif userGuess > secretNumber:
                  print (" Too high ")
                  if guessNumber == 7:  # This will display the secret number if the player doesn't guess the number
                        print(" The secret number is "+ str(secretNumber))
               else:
                  print (" Too low ")
                  if guessNumber == 7:
                        print(" The secret number is "+ str(secretNumber))
            else:      #////////////////////////////////////////////////
               print(" That was not a valid guess....but we are counting it, try again")

#main -- run the functions above

def main():
      inst()
# This will loops if player chooses to play, will break if player doesn't want to play,
# and will loop if player inter invalid inputs
      while True: 
            playGame = input("Do you still want to play? 'y' for yes and 'n' for no. ")
            if playGame == "y":
                  playerGess()
                  continue;
            elif playGame == "n":
                  print (" Goodbye .... ")
                  break
            else:
                  print(" Invalid input... ")

     # game over
main()




    
