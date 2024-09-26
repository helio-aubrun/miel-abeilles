import math
import random
from config import MUTATION_FREQUENCY, MUTATION_RATE, NB_BEES, FLOWERS, SELECTION_RATE


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
        return f"id : {self.id} distance traveled :  {self._distance_traveled}"  # {self._path}


class Beehive:
    def __init__(self):
        self._nb_bees = NB_BEES
        self._flowers = FLOWERS
        self.first_generation()
        self.caclulate_av_distance()

    def select(self, selection_rate=SELECTION_RATE):
        bee_classment = sorted(
            self.population, key=lambda Bee: Bee.get_distance_traveled()
        )
        top = bee_classment[:selection_rate]
        return top

    def multiplication_population(self, top):
        for i in range(self._nb_bees):
            self.population[i] = top[i % len(top)]
        self.caclulate_av_distance()
        self._generation += 1

    def first_generation(self):
        self.population = []
        for i in range(self._nb_bees):
            path = random.sample(self._flowers, len(self._flowers))
            path.append((500, 500))
            path.insert(0, (500, 500))
            self.population.append(Bee(path, i))
        self._generation = 1

    def print_top_bees(self, nb):
        top = self.select(self._nb_bees)
        distances_vues = set()
        i = 0
        while len(distances_vues) < nb and i < self._nb_bees:
            distance = top[i].get_distance_traveled()

            if distance not in distances_vues:
                print(f"Bee {i}: {distance}")
                distances_vues.add(distance)
            i += 1

    def mutate_beehive(self):
        for bee in self.population:
            if random.random() < MUTATION_RATE:
                bee.mutation(MUTATION_FREQUENCY)

    def caclulate_av_distance(self):
        self.av = 0
        for i in range(self._nb_bees):
            self.av += self.population[i].get_distance_traveled()
        self.av = self.av / self._nb_bees

    def get_av(self):
        return self.av

    def __str__(self):
        return f"generation :  {self._generation} | average distance : {self.av}"
