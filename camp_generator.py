def generat_and_save_flower (nb_flower, name = "camp"): 
    from random import randint

    with open (str (name) + "_" + str (nb_flower) + ".txt","w") as file :
        for i in range (nb_flower) :
            file.write (str (randint (0, 1000)) + "," + str (randint (0, 1000)) + '\n')

if __name__ == "__main__" :

    test_input = False
    while not test_input :
        try :
            nb_flower = int (input ("donner le nombre de fleur a generer sou nombre entier: "))
            test_input = True
        except :
            print ("veiller donner un nombre entier")

    generat_and_save_flower (nb_flower)