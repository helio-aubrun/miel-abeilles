from config import NUMBER_OF_GENERATION
from beehive import Beehive


def print_bees(beehive):
    for i in range(3):
        print(f"Bee {beehive.population.id[i]}  {beehive.population[i]}")

def plot_in_terminal(values: list) -> None:
    import plotext as plt

    plt.plot([i for i in range(len(values))], values)
    plt.title("Evolution of average distance of bees per generation")
    plt.show()


if "__main__" == __name__:
    values = []
    beehive = Beehive()

    values.append (beehive.get_av())

    print (beehive)
    beehive.print_top_bees (10)

    for i in range(NUMBER_OF_GENERATION):

        top_bees = beehive.select_top_bees ()
        beehive.multiply (top_bees)
        beehive.mutate_beehive ()

        print (f"beehive {beehive}")
        beehive.print_top_bees (10)

        values.append (beehive.get_av())

    plot_in_terminal (values)


