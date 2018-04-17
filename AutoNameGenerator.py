import random, string

number_input_letters = input("How many letters do you want the name to have? ")

input_letters = []

output_letters = []

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"


for j in range(int(number_input_letters)):
    input_letter = input("v , c or l? ")
    input_letters.append(str(input_letter))



def generator():
    for i in range(int(number_input_letters)):
        if input_letters[i] == 'v':
            letter1 = random.choice(vowels)
            output_letters.append(letter1)
        elif input_letters[i] == 'c':
            letter1 = random.choice(consonants)
            output_letters.append(letter1)
        else:
            letter1 = random.choice(string.ascii_letters)
            output_letters.append(letter1)
        i = i + 1
    name = output_letters
    print(''.join(name))


generator()




    



