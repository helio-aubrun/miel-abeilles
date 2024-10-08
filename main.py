from beehive import Beehive
from config import AVERAGE_COMPARAISON, NB_GENERATIONS_MUTATE, NUMBER_OF_GENERATION
from graphic import plot_curve, drow_path_bee_matplotlib, drow_path_bee_turtle, print_bar

def print_bees(beehive):
    for i in range(3):
        print(f"Bee {beehive.population.id[i]}  {beehive.population[i]}")

question_turtle = "vouler vous voire le chemin de la meilleir abeille avec turtle"
question_matplotlib = "vouler vous voire le chemin de la meilleir abeille avec matplotlib"
question_convergence_check = "vouler vous utiliser le check de convergence"

def cross_1_or_2 () :
    while True :
        try :  
            result = int(input ("utiliser la methode cross 1 ou 2 :"))
            return (result)
        except :
            print ("veiller donner 1 ou 2.")

def ask_yes_no(question):
    while True:
        answer = input(f"{question} [y/n]: ").strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("veiller donner y pour oui ou n pour non.")

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
    
def convergence_check ():
    while not_convergence(values):

        top_bees = beehive.select_top_bees()
        beehive.cross (top_bees, cross_choise)

        # print(f"beehive {beehive}")
        # beehive.print_top_bees(10)

        values.append(beehive.get_av())

    for i in range(NB_GENERATIONS_MUTATE):
    
        beehive.mutate_beehive()

        # print(f"beehive {beehive}")
        # beehive.print_top_bees(10)

        values.append(beehive.get_av())

def no_convergence_check () :
    for i in range(NUMBER_OF_GENERATION):

        top_bees = beehive.select_top_bees()
        beehive.cross (top_bees, cross_choise)
        beehive.mutate_beehive()

        # print(f"beehive {beehive}")
        # beehive.print_top_bees(10)

        values.append(beehive.get_av())

        print_bar (i + 1, NUMBER_OF_GENERATION)

if "__main__" == __name__:
    values = []
    beehive = Beehive()
    cross_choise = cross_1_or_2 ()

    values.append(beehive.get_av())

    values_last_gens = []
    values_actual_gens = []

    # print(beehive)
    # beehive.print_top_bees(10)

    if ask_yes_no (question_convergence_check) :
        convergence_check ()
    
    else :
        no_convergence_check ()


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

    plot_curve (values)

    best_bee = beehive.select_top_bees (1) [0]

    print () #to start on a new line after print the loading bar

    if ask_yes_no (question_matplotlib) :
        drow_path_bee_matplotlib (best_bee.get_path ())

    if ask_yes_no (question_turtle) :
        drow_path_bee_turtle (best_bee.get_path ())