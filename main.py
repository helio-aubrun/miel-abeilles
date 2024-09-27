from beehive import Beehive

BEEHIVE = Beehive()  # Beehive


def print_bees():
    for i in range(3):
        print(f"Bee {i}  {BEEHIVE.population[i]}")


def print_beehive():
    print(BEEHIVE)


if "__main__" == __name__:
    print_beehive()
    for i in range(6):
        top = BEEHIVE.select()
        BEEHIVE.multiplication_population(top)
        BEEHIVE.mutate_beehive()
        print_beehive()
        BEEHIVE.print_top_bees(10)
