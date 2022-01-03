import pygame
from pygame import constants
import constants
import datetime as dt
from prettytable import PrettyTable

today = dt.datetime.now()
today_string = today.strftime("%Y-%m-%d")


class Game():
    def __init__(self):
        self.score = 0
        self.level = 0
        self.lines = 0
        self.high_score = 0
        self.leaderboard = []
        self.read_leaderboard()


    def increase_level(self):
        self.level = int(self.lines / constants.LINES_PER_LEVEL)
        if constants.DELAY > constants.MIN_DELAY:
            constants.DELAY -= 0.02

    def increase_lines(self,increment):
        self.lines += increment

    def increase_points(self,lines):
        if lines == 0:
            return None
        points_system = {
            1 : (40 * (self.level + 1)),
            2 : (100 * (self.level + 1)),
            3 : (300 * (self.level + 1)),
            4 : (1200 * (self.level + 1)),
        }

        added_points = points_system[lines]
        self.score += added_points

    def read_leaderboard(self):
        with open("leaderboard.txt", "r") as f:
            leaderboard = f.readlines()
            if leaderboard == []:
                pass
            else:
                for entry in leaderboard:
                    values = entry.split()
                    score = values[0]
                    name = values[1]
                    date = values[2]
                    self.leaderboard.append((score,name,date))
                self.leaderboard = sorted(self.leaderboard,key=lambda x: x[0])
                self.high_score = self.leaderboard[0][0]


    def update_leaderboard(self):
        all_scores = [self.leaderboard[i][0] for i in range(len(self.leaderboard))]
        if all_scores == []:
            min_score = 0
        else:
            min_score = min(all_scores)
        if self.score > int(min_score):
            self.leaderboard.append((self.score,"Name",today_string))
            with open("leaderboard.txt","w") as f:
                for entry in self.leaderboard:
                    f.write(str(entry[0]) + " " + str(entry[1]) + " " + str(entry[2]) + "\n")



