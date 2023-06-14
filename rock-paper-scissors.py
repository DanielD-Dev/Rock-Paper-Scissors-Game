# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round.

import random
moves = ['rock', 'paper', 'scissors']

# The Player class is the parent class for all of the Players in this game

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class ReflectPlayer(Player):
    def __init__(self):
        self.opponent_move = 'rock'

    def move(self):
        return self.opponent_move

    def learn(self, my_move, their_move):
        self.opponent_move = their_move

class CyclePlayer(Player):
    def __init__(self):
        self.last_move = 'scissors'

    def move(self):
        if self.last_move == 'rock':
            self.last_move = 'paper'
        elif self.last_move == 'paper':
            self.last_move = 'scissors'
        else:  # self.last_move == 'scissors'
            self.last_move = 'rock'
        return self.last_move

class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input('Select: Rock, Paper or Scissors: ').lower()
            if human_move in moves:
                return human_move
            else:
                print("Invalid move. Please select: Rock, Paper or Scissors")

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            result = "Player One wins!"
            self.score1 += 1
        elif beats(move2, move1):
            result = "Player Two wins!"
            self.score2 += 1
        else:
            result = "It's a tie!"

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        return result

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round+1}:")
            round_result = self.play_round()
            print(round_result)
        print("Game over!")

        if self.score1 > self.score2:
            print("Player One wins!")
        elif self.score2 > self.score1:
            print("Player Two wins!")
        else:
            print("It's a tie!")
        print(f"Final scores: Player One: {self.score1}, Player Two: {self.score2}")

if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
