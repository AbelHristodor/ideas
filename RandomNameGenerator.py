import random
import string

input_letter_1 = input(
    "Type 'v' for vowel, 'c' for consonant, 'l' for a random letter")
input_letter_2 = input(
    "Type 'v' for vowel, 'c' for consonant, 'l' for a random letter")
input_letter_3 = input(
    "Type 'v' for vowel, 'c' for consonant, 'l' for a random letter")
input_letter_4 = input(
    "Type 'v' for vowel, 'c' for consonant, 'l' for a random letter")
input_letter_5 = input(
    "Type 'v' for vowel, 'c' for consonant, 'l' for a random letter")

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"


def generator():
    if input_letter_1 == 'v':
        letter1 = random.choice(vowels)
    elif input_letter_1 == 'c':
        letter1 = random.choice(consonants)
    else:
        letter1 = random.choice(string.ascii_letters)

    if input_letter_2 == 'v':
        letter2 = random.choice(vowels)
    elif input_letter_2 == 'c':
        letter2 = random.choice(consonants)
    else:
        letter2 = random.choice(string.ascii_letters)

    if input_letter_3 == 'v':
        letter3 = random.choice(vowels)
    elif input_letter_3 == 'c':
        letter3 = random.choice(consonants)
    else:
        letter3 = random.choice(string.ascii_letters)

    if input_letter_4 == 'v':
        letter4 = random.choice(vowels)
    elif input_letter_4 == 'c':
        letter4 = random.choice(consonants)
    else:
        letter4 = random.choice(string.ascii_letters)

    if input_letter_5 == 'v':
        letter5 = random.choice(vowels)
    elif input_letter_5 == 'c':
        letter5 = random.choice(consonants)
    else:
        letter5 = random.choice(string.ascii_letters)

    name = letter1 + letter2 + letter3 + letter4 + letter5
    
    return name


print(generator())
