import random
from modules.md_name import name_generator
from modules.md_surname import surname_generator
from modules.md_parts import parts_generator, vowel, consonant


def female_male():
    he_her = input('He or She? (H/S): ')
    he_her = he_her.capitalize()
    while he_her != 'H' and he_her != 'S':
        he_her = input('He or She? (H/S): ')
    if he_her == 'H':
        return 'he'
    else:
        return 'her'


def fem_check(name):
    if name[-1] == 'a':
        return 'Lady'
    else:
        return 'Sir'


def land_maker():
    description = ['Silver', 'Dark', 'Moon', 'Green', 'Shadow', 'Deep', 'Frozen', 'Fiery', 'Boring', 'Old', 'Sun',
                   'Gloomy']
    place = ['mine', 'forest', 'lake', 'mountain', 'town', 'tower', 'graveyard', 'swamps', 'caves']
    land = random.choice(description) + random.choice(place)
    return land


def main():
    parts = parts_generator()
    he_r = female_male()
    name = name_generator(parts, he_r)
    surname = surname_generator(parts)
    title = fem_check(name)
    land = land_maker()

    print(f'{title} {name} {surname} of {land}')


if __name__ == '__main__':
    main()
