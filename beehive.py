import random
from config import MUTATION_FREQUENCY, MUTATION_RATE, NB_BEES, FLOWERS, SELECTION_RATE
from bee import Bee

class Beehive:
    def __init__(self):
        self._nb_bees = NB_BEES
        self._flowers = FLOWERS
        self.generat_first_gen()
        self.caclulate_av_distance()

    def select_top_bees (self, select_top_beesion_rate=SELECTION_RATE):
        bee_classment = sorted(
            self.population, key=lambda Bee: Bee.get_distance()
        )
        top = bee_classment[:select_top_beesion_rate]
        return top

    def multiply(self, top_bees):
        for i in range(self._nb_bees):
            data_for_bee = top_bees[random.randint (0, len (top_bees) - 1)]
            self.population[i] = Bee(data_for_bee.get_path (), data_for_bee.get_id ())
        self.caclulate_av_distance()
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


    def caclulate_av_distance(self):
        self.av = 0
        for i in range(self._nb_bees):
            self.av += self.population[i].get_distance()
        self.av = self.av / self._nb_bees

    def cross_bees(self, top):
        for i in range (len(top)):
            if i +1 == len(top):
                path_children = top[i].cross_bee(top[0])
            else :
                path_children = top[i].cross_bee(top[i+1])
            self.population[i + SELECTION_RATE].change_path(path_children)
        self.caclulate_av_distance()
        self._generation += 1

    def get_av(self):
        return self.av

    def __str__(self):
        return f"generation :  {self._generation} | average distance : {self.av}"