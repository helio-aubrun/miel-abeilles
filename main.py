import random
import openpyxl
from beehive import Bee, Beehive

NB_BEE = 100

NB_TOP = 20

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

BEES = Beehive(NB_BEE, FLOWERS)


def print_bees():
    i=0
    for b in BEES.population:
        print (f"Bee {i}  {b}")


if "__main__" == __name__ :
    top = BEES.selection(NB_TOP)
    BEES.multiplication_population(top, NB_BEE)
    for bee in BEES.population : 
        if random.random() > MUTATION_RATE:
            bee.mutation(MUTATION_FREQUENCY)
    print_bees()
        