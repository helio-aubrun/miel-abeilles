import math
import random

class Bee:
    def __init__(self, path, id):
        self.id = id
        self._path = path
        self._distance_traveled = self.compute_distance(self._path)

    def compute_distance(self,path):
        distance_traveled = 0
        for i in range(len(path) - 1):
            distance_traveled += math.sqrt(
                (path[i][0] - path[i + 1][0]) ** 2
                + (path[i][1] - path[i + 1][1]) ** 2
            )
        return distance_traveled

    # def mutate(self, mutate_frequency):
    #     for i in range(mutate_frequency):
    #         a = random.randint(1, len(self._path) - 2)
    #         b = random.randint(1, len(self._path) - 2)
    #         self._path[a], self._path[b] = self._path[b], self._path[a]

    #     self.compute_distance()

    def mutate(self, mutate_frequency):
        test_beter_distance = False
        while not test_beter_distance :
            
            tmp_path = list (self._path)

            for i in range(mutate_frequency):
                a = random.randint(1, len(tmp_path) - 2)
                b = random.randint(1, len(tmp_path) - 2)
                tmp_path[a], tmp_path[b] = tmp_path[b], tmp_path[a]

            if self.compute_distance(tmp_path) - self._distance_traveled <= 800:
                test_beter_distance = True
        
        self._path = list (tmp_path)

    def get_id (self) :
        return self.id
    
    def get_path(self):
        return self._path

    def get_distance(self):
        return self._distance_traveled

    def __str__(self):
        return f"id : {self.id} distance traveled :  {self._distance_traveled}"


if __name__ == "__main__" :
    # Example path of coordinates
    path = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

    # Create a Bee object
    bee = Bee(path, 1)

    # Original path and distance
    print("Original path:", bee.get_path())
    print("Original distance:", bee.get_distance())

    # Mutate the path
    bee.mutate(2)

    # Mutated path and new distance
    print("Mutated path:", bee.get_path())
    print("New distance:", bee.get_distance())
