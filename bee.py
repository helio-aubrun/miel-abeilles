import math


class Bee:
    def __init__(self, path):
        self.path = path
        self.distance_traveled = self.calcul_distance_traveled()

    def calcul_distance_traveled(self):
        distance_traveled = 0
        for i in range(len(self.path) - 1):
            distance_traveled += math.sqrt(
                (self.path[i][0] - self.path[i + 1][0]) ** 2
                + (self.path[i][1] - self.path[i + 1][1]) ** 2
            )
        return distance_traveled
