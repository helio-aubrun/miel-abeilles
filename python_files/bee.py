import random
from python_files.config import MUTATION_MARGIN, CROSS_QUOTA


class Bee:
    def __init__(self, path, id):
        self.id = id
        self._path = path
        self._distance_traveled = self.compute_distance(self._path)

    def distance_formula(self, i, path):
        distance = abs(path[i][0] - path[i + 1][0]) + abs(path[i][1] - path[i + 1][1])

        return distance

    def distance_formula_hive(self, i, path):
        distance = abs(path[i][0] - 500) + abs(path[i][1] - 500)

        return distance

    def compute_distance(self, path):
        distance_traveled = 0
        for i in range(len(path) - 1):
            distance_traveled += self.distance_formula(i, path)

        distance_traveled += self.distance_formula_hive(0, path)

        distance_traveled += self.distance_formula_hive(-1, path)

        return distance_traveled

    def mutate(self, mutate_frequency):
        test_beter_distance = False
        while not test_beter_distance:

            tmp_path = list(self._path)

            for i in range(mutate_frequency):
                a = random.randint(0, len(tmp_path) - 1)
                b = random.randint(0, len(tmp_path) - 1)
                tmp_path[a], tmp_path[b] = tmp_path[b], tmp_path[a]

            if (
                self.compute_distance(tmp_path) - self._distance_traveled
                <= MUTATION_MARGIN
            ):
                test_beter_distance = True

        self._path = list(tmp_path)
        self._distance_traveled = self.compute_distance(self._path)

    def cross_bee(self, other):
        path_parent_1 = self._path
        path_parent_2 = other.get_path()
        path_children = path_parent_1[:CROSS_QUOTA]
        for flower in path_parent_2:
            if flower not in path_children:
                path_children.append(flower)
        return path_children

    def change_path(self, new_path):
        self._path = list(new_path)
        self._distance_traveled = self.compute_distance(self._path)

    def get_id(self):
        return self.id

    def get_path(self):
        return self._path

    def get_distance(self):
        return self._distance_traveled

    def __str__(self):
        return f"id : {self.id} distance traveled :  {self._distance_traveled}"


if __name__ == "__main__":
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
