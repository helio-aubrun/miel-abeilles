import math
import random

class Bee:
    def __init__(self, path, id):
        self.id = id
        self._path = path
        self.compute_distance_traveled()

    def compute_distance_traveled(self) -> None:
        distance_traveled = 0
        for i in range(len(self._path) - 1):
            distance_traveled += math.sqrt(
                (self._path[i][0] - self._path[i + 1][0]) ** 2
                + (self._path[i][1] - self._path[i + 1][1]) ** 2
            )
        self._distance_traveled = distance_traveled

    def mutation(self, mutation_frequency):
        for i in range(mutation_frequency):
            a = random.randint(1, len(self._path) - 1)
            b = random.randint(1, len(self._path) - 1)
            self._path[a], self._path[b] = self._path[b], self._path[a]

        self.compute_distance_traveled()

    def get_path(self):
        return self._path

    def get_distance_traveled(self):
        return self._distance_traveled

    def __str__(self):
        return f"id : {self.id} distance traveled :  {self._distance_traveled}"