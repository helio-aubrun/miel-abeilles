from beehive import Beehive
from config import AVERAGE_COMPARAISON, NB_GENERATIONS_MUTATE


def print_bees(beehive):
    for i in range(3):
        print(f"Bee {beehive.population.id[i]}  {beehive.population[i]}")


def plot_in_terminal(values: list) -> None:
    import plotext as plt

    plt.plot([i for i in range(len(values))], values)
    plt.title("Evolution of average distance of bees per generation")
    plt.show()

def compute_average_values(values):
    average = 0
    for i in range(len(values)):
        average += values[i]
    average = average / len(values)
    return average

def not_convergence (values) :
    if len(values) >= AVERAGE_COMPARAISON*2:
        try :
            values_last_gens = list(values[-AVERAGE_COMPARAISON*2:][:AVERAGE_COMPARAISON])
            values_actual_gens = list(values[-AVERAGE_COMPARAISON:])
            return not (0 <=compute_average_values(values_last_gens) - compute_average_values(values_actual_gens) <= 50)
        except :
            return True
    else:
        return True

if "__main__" == __name__:
    values = []
    beehive = Beehive()

    values.append(beehive.get_av())
    values_last_gens = []
    values_actual_gens = []

    print(beehive)
    beehive.print_top_bees(10)

    while not_convergence(values):
        top_bees = beehive.select_top_bees()
        beehive.cross_bees(top_bees)
        print("cross")
        #beehive.mutate_beehive ()
        print(f"beehive {beehive}")
        beehive.print_top_bees(10)
        values.append(beehive.get_av())
    for i in range(NB_GENERATIONS_MUTATE):
        print ('mutate')
        beehive.mutate_beehive()
        print(f"beehive {beehive}")
        beehive.print_top_bees(10)
        values.append(beehive.get_av())
    # for i in range (50):
    #     beehive.mutate_beehive ()
    #     print(f"beehive {beehive}")
    #     beehive.print_top_bees(10)
    #     values.append(beehive.get_av())
    # for i in range(50):

    #     top_bees = beehive.select_top_bees()
    #     beehive.cross_bees(top_bees)
    #     average_actual_gen = int(beehive.get_av())
    #     if  0 <= average_last_gen - average_actual_gen <= 500:
    #          beehive.mutate_beehive ()
    #          average_last_gen = int(beehive.get_av())

    #     print(f"beehive {beehive}")
    #     beehive.print_top_bees(10)

    #     values.append(beehive.get_av())

    plot_in_terminal(values)