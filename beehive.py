import math
import random



class Bee:
    def __init__(self, path):
        self._path = path
        self._compute_distance_traveled()

    def _compute_distance_traveled(self) -> None:
        distance_traveled = 0
        for i in range(len(self._path) - 1):
            distance_traveled += math.sqrt(
                (self._path[i][0] - self._path[i + 1][0]) ** 2
                + (self._path[i][1] - self._path[i + 1][1]) ** 2
            )
        self._distance_traveled = distance_traveled

    def mutation(self,mutation_frequency):
        for i in range (mutation_frequency):
            a = random.randint(1,len(self._path)-1)
            b = random.randint(1,len(self._path)-1)
            tmp = self._path[b]
            self._path[b]= self._path[a]
            self._path[a] = tmp

    def get_path(self):
        return self._path
    
    def get_distance_traveled(self):
        return self._distance_traveled
    
    def __str__(self):
        return f"path : {self._path} distance traveled :  {self._distance_traveled}"
