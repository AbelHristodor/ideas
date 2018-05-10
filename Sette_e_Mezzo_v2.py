import random

mazzo_carte = ['1d', '2d', '3d', '4d', '5d', '6d', '7d', 'fd', 'cd', 'rd', '1b', '2b', '3b', '4b', '5b', '6b', '7b',
               'fb', 'cb', 'rb', '1c',
               '2c', '3c', '4c', '5c', '6c', '7c', 'fc', 'cc', 'rc', '1s', '2s', '3s', '4s', '5s', '6s', '7s', 'fs',
               'cs', 'rs']


def switcher(carta, SommaCarte):
    str(carta)
    if carta.startswith('1'):
        SommaCarte += 1
    elif carta.startswith('2'):
        SommaCarte += 2
    elif carta.startswith('3'):
        SommaCarte += 3
    elif carta.startswith('4'):
        SommaCarte += 4
    elif carta.startswith('5'):
        SommaCarte += 5
    elif carta.startswith('6'):
        SommaCarte += 6
    elif carta.startswith('7'):
        SommaCarte += 7
    elif carta.startswith('f') or carta.startswith('c') or carta.startswith('r'):
        SommaCarte += 0.5

    return SommaCarte



print("\n########################################################\n")
print("Per riconoscere le carte:")
print("'d' sta per Denari    'b' sta per Bastoni \n'c' sta per Coppe   's' sta per spade")
print("'f' sta per Fante    'c' sta per Cavallo  e 'r' sta per Re\n ")
print("########################################################\n")

Somma_pc = 0
Somma_user = 0
print("Allora, inizio io")

while Somma_pc < 7.5 and Somma_user < 7.5:
    print("\n########################################################\n")
    print("Ho preso una carta")

    carta_pc = mazzo_carte[random.randrange(len(mazzo_carte))]
    Somma_pc = switcher(carta_pc, Somma_pc)
    carta_pc_index = mazzo_carte.index(carta_pc)
    mazzo_carte.pop(carta_pc_index)

    print(f"Somma pc : {Somma_pc}, carta pc : {carta_pc}\n")
    print("\n########################################################\n")
    print("Ok, ora tocca a te. \n")

    carta_user = mazzo_carte[random.randrange(len(mazzo_carte))]

    print(f"Allora la tua carta è: {carta_user}")

    Somma_user = switcher(carta_user, Somma_user)
    carta_user_index = mazzo_carte.index(carta_user)
    mazzo_carte.pop(carta_user_index)

    print(f"Somma utente: {Somma_user}\n")
    print("\n########################################################\n")

    choice = input("Vuoi continuare oppure fermarti? c/f ")
    print("\n########################################################\n")

    if choice == 'c':
        continue
    elif choice == 'f':
        break
    elif len(mazzo_carte) == 0:
        print("Il mazzo è vuoto!")
        print("Ho vinto IO!")
        break


if Somma_pc >= 7.5:
    print(f"La somma delle mie carte è {Somma_pc}")
    print("HO perso!")

elif Somma_user >= 7.5:
    print(f"La somma delle mie carte è {Somma_user}")
    print("Hai Perso!")
elif len(mazzo_carte) == 0:
    print("Il mazzo è vuoto, Ho vinto IO!")