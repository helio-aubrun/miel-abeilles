import random
from config import (
    MUTATION_FREQUENCY,
    MUTATION_RATE,
    NB_BEES,
    FLOWERS,
    SELECTION_RATE,
    NB_SEGMENT,
    PARENT_RATE,
    NB_PARENT_KEPT,
)
from bee import Bee


class Beehive:
    def __init__(self):
        self._nb_bees = NB_BEES
        self._flowers = FLOWERS
        self.generat_first_gen()
        self.compute_av_distance()

    def select_top_bees(self, select_top_beesion_rate=SELECTION_RATE):
        bee_classment = sorted(self.population, key=lambda Bee: Bee.get_distance())
        top = bee_classment[:select_top_beesion_rate]
        return top

    def multiply(self, top_bees):
        for i in range(self._nb_bees):
            data_for_bee = top_bees[random.randint(0, len(top_bees) - 1)]
            self.population[i] = Bee(data_for_bee.get_path(), data_for_bee.get_id())
        self.compute_av_distance()
        self._generation += 1

    def generat_first_gen(self):
        self.population = []
        for i in range(self._nb_bees):
            path = random.sample(self._flowers, len(self._flowers))
            self.population.append(Bee(path, i))
        self._generation = 0

    def print_top_bees(self, nb):
        top = self.select_top_bees(self._nb_bees)
        distances_vues = set()
        i = 0
        while len(distances_vues) < nb and i < self._nb_bees:
            distance = top[i].get_distance()

            if distance not in distances_vues:
                print(f"Bee {i}: {distance}")
                distances_vues.add(distance)
            i += 1

    def mutate_beehive(self):
        for bee in self.population:

            if random.random() < MUTATION_RATE:
                bee.mutate(MUTATION_FREQUENCY)
        # self._generation += 1
        self.compute_av_distance()

    def compute_av_distance(self):
        self.av = 0
        for i in range(self._nb_bees):
            self.av += self.population[i].get_distance()
        self.av = self.av / self._nb_bees

    def increment(self, parent_path, pos, len_segment):
        tmp = []

        while pos < len(parent_path):
            tmp.append(parent_path[pos])
            pos += 1

        return tmp

    def cross_method(self, parent_1, parent_2, nb_segment, parent_rate):
        child_1_path = []

        parent_1_path = parent_1.get_path()
        parent_2_path = parent_2.get_path()

        len_segment = len(parent_1.get_path()) // nb_segment

        pos_1, pos_2 = 0, 0

        while pos_1 <= len(parent_1_path) or pos_2 <= len(parent_2_path):

            chance = random.random()
            if chance <= parent_rate:

                child_1_path.extend(self.increment(parent_1_path, pos_1, len_segment))
                pos_1 += len_segment

            if chance >= parent_rate:

                child_1_path.extend(self.increment(parent_2_path, pos_2, len_segment))
                pos_2 += len_segment

        return list(set(child_1_path))

    def cross(self, top, test):
        self.population = [top[i] for i in range(NB_PARENT_KEPT)]

        for i in range(NB_BEES - NB_PARENT_KEPT):
            parent1 = random.choice(top)
            parent2 = random.choice(top)

            if test == 1:
                child_path = self.cross_method(
                    parent1, parent2, NB_SEGMENT, PARENT_RATE
                )
            else:
                child_path = parent1.cross_bee(parent2)
            child_pos = i + SELECTION_RATE

            self.population.append(Bee(child_path, child_pos))

        self.compute_av_distance()
        self._generation += 1

    def get_av(self):
        return self.av

    def __str__(self):
        return f"generation :  {self._generation} | average distance : {self.av}"
