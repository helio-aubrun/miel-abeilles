NB_BEES = 100  # number of bees in the beehive

SELECTION_RATE = 20  # How many bees we keep per generation

MUTATION_RATE = 0.4  # How many bees will mutate

MUTATION_FREQUENCY = 2  # How many flower will change in a bee mutate path

from flowers import import_flowers_txt

FLOWERS = import_flowers_txt()  # List of tuple that containt flowers' positions

MUTATION_MARGIN = 300  # When the mutation is consider as benefic

NUMBER_OF_GENERATION = 100  # How many generation the programme compute

CROSS_QUOTA = 20 # The part that we keep from the first parent during the crossover

AVERAGE_COMPARAISON = 10