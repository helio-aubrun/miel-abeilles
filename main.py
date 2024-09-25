import random
import openpyxl
from beehive import Bee

NB_BEE = 100

NB_TOP = 20

POPULATION = []

MUTATION_RATE = 0.2

MUTATION_FREQUENCY = 2

def import_flowers () :
    dataframe = openpyxl.load_workbook("Champ.xlsx")

    dataframe1 = dataframe.active

    list_flowers = []

    for row in range(1, dataframe1.max_row):
        pos_flowers = []
        for col in dataframe1.iter_cols(1, dataframe1.max_column):
            pos_flowers.append ( int ((col[row].value)))
        list_flowers.append ((pos_flowers[0],pos_flowers[1]))

    return list_flowers

FLOWERS = import_flowers ()

def init_population () :
    for i in range (NB_BEE) :
        path = random.sample(FLOWERS, len(FLOWERS))
        path.append((500,500))
        path.insert (0, (500,500))
        POPULATION.append (Bee(path))


def selection (NB_TOP) :
    bee_classment = sorted (POPULATION , key=lambda Bee: Bee.get_distance_traveled())
    top = bee_classment [:NB_TOP]
    return top

def multiplication_population (top):
    for i in range(NB_BEE):
        POPULATION[i] = top[i%len(top)]

def print_bees():
    i=0
    for b in POPULATION:
        print (f"Bee {i}  {b}")


if "__main__" == __name__ :
    init_population ()
    top = selection (NB_TOP)
    multiplication_population(top)
    for bee in POPULATION : 
        if random.random() > MUTATION_RATE:
            bee.mutation(MUTATION_FREQUENCY)
    print_bees()
        