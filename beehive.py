import math
import random



class Bee:
    def __init__(self, path):
        self.path = path
        self.compute_distance_traveled()

    def compute_distance_traveled(self) -> None:
        distance_traveled = 0
        for i in range(len(self.path) - 1):
            distance_traveled += math.sqrt(
                (self.path[i][0] - self.path[i + 1][0]) ** 2
                + (self.path[i][1] - self.path[i + 1][1]) ** 2
            )
        self.distance_traveled = distance_traveled

    def mutation(self,mutation_frequency):
        for i in range (mutation_frequency):
            a = random.randint(1,len(self.path)-1)
            b = random.randint(1,len(self.path)-1)
            tmp = self.path[b]
            self.path[b]= self.path[a]
            self.path[a] = tmp
