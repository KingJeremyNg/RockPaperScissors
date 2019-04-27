#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

class Player:
    #Default Constructor method
    def __init__(self):
        self.myMoves = []
        self.opponentMoves = []

    #Method learn to record both players' moves into lists myMoves and opponentMoves
    def learn(self, my_move, their_move):
        self.myMoves.append(my_move)
        self.opponentMoves.append(their_move)

    #Method getMyMoves() to return list containing all moves played by player 1
    def getMyMoves(self):
        return self.myMoves

    #Method getOpponentMoves() to return list containing all moves played by player 2
    def getOpponentMoves(self):
        return self.opponentMoves

#Class RockPlayer that returns only "rock"
class RockPlayer(Player):
    def move(self):
        return 'rock'

#Class PaperPlayer that returns only "paper"
class PaperPlayer(Player):
    def move(self):
        return 'paper'

#Class ScissorsPlayer that returns only "scissors"
class ScissorsPlayer(Player):
    def move(self):
        return 'scissors'

#Class RandPlayer that returns a random move from list, "moves"
class RandPlayer(Player):
    def move(self):
        return moves[random.randint(0,2)]

#Class ReflectPlayer that returns Player 1's last move
class ReflectPlayer(Player):
    def move(self):
        temp = self.getOpponentMoves()
        #If it is the first round and opponent's move list is empty, return a random move
        if not temp:
            return moves[random.randint(0,2)]
        else:
            return temp[-1]

#Class CyclePlayer that returns moves in order of rock -> paper -> scissors ->...
class CyclePlayer(Player):
    def move(self):
        temp = self.getMyMoves()
        #If it is the first round and CyclePlayer's move list is empty, return a random move
        if not temp:
            return moves[random.randint(0,2)]
        else:
            return moves[(moves.index(temp[-1]) + 1) % 3]

#Class HumanPlayer that accepts and validates users input
class HumanPlayer(Player):
    def move(self):
        command = ""
        while (command.lower() not in moves):
            command = input("Please enter a move.\n")
            if (command.lower() not in moves):
                print("Please enter a valid move: rock, paper, scissors\n")
        return command

#Method beats that returns true or false if player 1 wins or loses against player 2 in round
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

#Class Game stores and controls a match
class Game:
    #Constructor method to initialize variables
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.myPoints = 0
        self.opponentPoints = 0
        self.roundsPlayed = 0

    #Method play_rounds() generates moves for both players and decides winner of the round
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.roundsPlayed += 1
        print("Player 1: {0}  Player 2: {1}".format(move1, move2))
        if (move1 == move2):
            print("You tied the round")
        elif (beats(move1, move2)):
            self.myPoints += 1
            print("You won the round")
        else:
            self.opponentPoints += 1
            print("Your lost the round")

    #Method play_game(rounds) plays a number of rounds specified by user input and decides overall winner
    def play_game(self, rounds):
        print("\nGame start!")
        for round in range(rounds):
            #If any player's points exceeds (rounds / 2) then they are guaranteed to win the match
            if (self.myPoints > rounds / 2.0 or self.opponentPoints > rounds / 2.0):
                print("\nBest out of {0} rounds is over. Winner has been decided!".format(rounds))
                self.winner()
                print("Please enter a command. Type 'HELP' for list of commands")
                return
            print("\nRound {0}:".format(round + 1))
            self.play_round()
        print("\nGame over!")
        self.winner()
        print("Please enter a command. Type 'HELP' for list of commands")

    #Method winner() to print the outcome of the match
    def winner(self):
        if (self.myPoints > self.opponentPoints):
            print("You won the match with {0} points while your opponent had {1} points!\n".format(self.myPoints, self.opponentPoints))
        elif (self.myPoints == self.opponentPoints):
            print("You tied the match with {0} points!\n".format(self.myPoints))
        else:
            print("You lost the match with {0} points while your opponent had {1} points!\n".format(self.myPoints, self.opponentPoints))

#Method help() to print a user command list
def help():
    print("")
    print("Commands:\tCommand Description:")
    print("PLAY [rounds]\tStart a game with parameter [rounds] as integer")
    print("QUIT\t\tExit the program")
    print("HELP\t\tGenerate command list")
    print("")

#Main method
if __name__ == '__main__':
    commandLine = ""
    commands = []
    print("Please enter a command. Type 'HELP' for list of commands")
    while (commandLine.lower() != "quit"):

        #Accept user input
        commandLine = input("").lower()

        #Splits the command line into a list while removing all whitespace
        commands = commandLine.split()

        #If command is "quit" then break out of while loop
        if (commands[0] == "quit"):
            print("\nExiting program...\n")
            break

        #If command is "help", print command list
        elif (commands[0] == "help"):
            help()

        #If command is "play", command line has at least 2 parameters and parameter 2 is a valid integer then continue
        elif (commands[0] == "play" and commands.__len__() >= 2):
            if (commands[1].isdigit()):
                rounds = int(commands[1])
                if (rounds > 0):
                    #Randomizing opponent
                    player = random.randint(1, 6)
                    if (player == 1):
                        game = Game(HumanPlayer(), RockPlayer())
                    if (player == 2):
                        game = Game(HumanPlayer(), PaperPlayer())
                    if (player == 3):
                        game = Game(HumanPlayer(), ScissorsPlayer())
                    if (player == 4):
                        game = Game(HumanPlayer(), RandPlayer())
                    if (player == 5):
                        game = Game(HumanPlayer(), ReflectPlayer())
                    if (player == 6):
                        game = Game(HumanPlayer(), CyclePlayer())
                    game.play_game(rounds)
                else:
                    print("Invalid number of rounds. Type 'HELP' for list of commands")
            else:
                print("Invalid parameter. Type 'HELP' for list of commands")
        else:
            print("Invalid command. Type 'HELP' for list of commands")