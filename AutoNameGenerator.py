import random, string

number_input_letters = input ("How many letters do you want the name to have?  ")

input_letters = []
for j in input_letters:
    input_letters = input("v , c or l? ")

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

for i in range(int(number_input_letters)):
    input_letters.append("input_letter")

def generator():
    for k in input_letters:
        if input_letters[i] == 'v':
            input_letters[i] = random.choice(vowels)
        elif input_letters[i] == 'c':
            input_letters[i] == random.choice(consonants)
        else: input_letters[i] == random.choice(string.ascii_letters)
    name = input_letters 
    print(name)




    



