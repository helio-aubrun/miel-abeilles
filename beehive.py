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

    def mutation(self, mutation_frequency):
        for i in range(mutation_frequency):
            a = random.randint(1, len(self._path) - 1)
            b = random.randint(1, len(self._path) - 1)
            tmp = self._path[b]
            self._path[b] = self._path[a]
            self._path[a] = tmp

    def get_path(self):
        return self._path

    def get_distance_traveled(self):
        return self._distance_traveled

    def __str__(self):
        return f"path : {self._path} distance traveled :  {self._distance_traveled}"


class Beehive:

    def __init__(self, nb_bees, flowers):
        self._nb_bees = nb_bees
        self._flowers = flowers
        self._generation = 0
        self.first_generation()

    def selection(self, selection_rate):
        bee_classment = sorted(
            self.population, key=lambda Bee: Bee.get_distance_traveled()
        )
        top = bee_classment[:selection_rate]
        return top

    def multiplication_population(self, top, nb_bee):
        for i in range(nb_bee):
            self.population[i] = top[i % len(top)]
        self._generation += 1

    def first_generation(self):
        self.population = []
        for i in range(self._nb_bees):
            path = random.sample(self._flowers, len(self._flowers))
            path.append((500, 500))
            path.insert(0, (500, 500))
            self.population.append(Bee(path))
        self._generation += 1

    def __str__(self):
        return f"number of bees : {self._nb_bees} generation :  {self._generation}"
