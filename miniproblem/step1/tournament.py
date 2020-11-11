# setp1/tournament.py

import random
from statistics import mean
from operator import attrgetter

from .struct import Player
from .database import AVLTree


class Tournament():
    def __init__(self):
        print("Welcome to ZeratoR's Among Us tournament ! \n\n")
        playerNames = []
        with open("assets/names.txt") as f:
            lines = f.readlines()
            for line in lines:
                playerNames.append(str(line).rstrip("\n"))
        players = [Player(player[0], player[1]) for player in list(zip(playerNames, [0 for _ in range(100)]))]
        self.ladder = AVLTree()
        [self.ladder.insert(player) for player in players] # All players are insterted in the database with a score of 0
        [self.rounds(playerNames, roundNumber) for roundNumber in range(1, 10)] # We play the 10 rounds of 3 games
        self.finals()

    def rounds(self, playerNames, number):
        print(f"Round number {number} is being played:")
        print("First game...")
        firstScores = [random.randint(0, 12) for _ in range(100 - ((number - 1) * 10))]
        print("Second game...")
        secondScores = [random.randint(0, 12) for _ in range(100 - ((number - 1) * 10))]
        print("Third game...")
        thirdScores = [random.randint(0, 12) for _ in range(100 - ((number - 1) * 10))]
        averageScores = [round(mean(data), 2) for data in list(zip(firstScores, secondScores, thirdScores))]
        self.update_ladder(averageScores)
        worstPlayers = []
        for _ in range(10):
            worst = self.ladder.get_min()
            worstPlayers.append(worst.name)
            self.ladder.delete(worst)
        print(f"These players are out > {worstPlayers} \n")

    def finals(self):
        print("Finals...")
        for player in self.ladder.inorder_traverse():
            player.score = 0
        scores = [[random.randint(0, 12) for _ in range(5)] for i in range(10)]
        averageScores = [round(mean(data), 2) for data in scores]
        self.update_ladder(averageScores)
        scoreboard = self.ladder.inorder_traverse()
        podium = sorted(scoreboard, key=attrgetter("score"), reverse=True)
        print([finalist.name + " " + str(finalist.score) for finalist in podium])

    def update_ladder(self, averageScores):
        newLadder = AVLTree()
        i = 0
        for player in self.ladder.inorder_traverse():
            player.score += averageScores[i]
            newLadder.insert(player)
            i += 1
        self.ladder = newLadder

    @staticmethod
    def run():
        test = Tournament()
