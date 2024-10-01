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
    average_last_gen = int(beehive.get_av())

    values.append (beehive.get_av())

    print (beehive)
    beehive.print_top_bees (10)

    for i in range(100):

        top_bees = beehive.select_top_bees ()
        beehive.multiply (top_bees)
        average_actual_gen = int(beehive.get_av())
        if 0 >= average_last_gen - average_actual_gen <= 500():
            beehive.mutate_beehive ()
            print (average_last_gen)
            average_last_gen = int(beehive.get_av())
            

        print (f"beehive {beehive}")
        beehive.print_top_bees (10)

        values.append (beehive.get_av())


    plot_in_terminal (values)