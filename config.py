NB_BEES = 100  # number of bees in the beehive

SELECTION_RATE = 20  # How many bees we keep per generation

MUTATION_RATE = 0.2  # How many bees will mutate

MUTATION_FREQUENCY = 2  # How many flower will change in a bee mutate path


def import_flowers():
    flowers = []
    with open("Champ.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    x, y = map(float, line.split(","))
                    flowers.append((x, y))
                except:
                    pass

    return flowers


FLOWERS = import_flowers()  # List of tuple that containt flowers' positions
