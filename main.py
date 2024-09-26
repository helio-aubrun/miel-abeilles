import random
from config import BEEHIVE, MUTATION_RATE, MUTATION_FREQUENCY, SELECTION_RATE, NB_BEES


def print_bees():
    for i in range(3):
        print(f"Bee {i}  {BEEHIVE.population[i]}")


def print_beehive():
    print(BEEHIVE)


def mutate_beehive():
    for bee in BEEHIVE.population:
        if random.random() < MUTATION_RATE:
            bee.mutation(MUTATION_FREQUENCY)


if "__main__" == __name__:
    print_beehive()
    for i in range(6):
        top = BEEHIVE.select(SELECTION_RATE)
        BEEHIVE.multiplication_population(top)
        mutate_beehive()
        print_beehive()
        BEEHIVE.print_top_bees(10)

