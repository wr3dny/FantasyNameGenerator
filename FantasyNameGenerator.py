import random


vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'q', 's', 't', 'v',
             'x', 'z', 'h', 'r', 'w', 'y']
vowel_consonant = vowel + consonant
surname_prefix = ['Mac', 'Mc', 'O\'', 'Ur-', 'al-', 'ibn ']
surname_suffix = ['son', 'sson']


def parts_generator():
    vcv_list = []
    for v in vowel:
        for c in consonant:
            vc = v + c
            cv = c + v
            vcv_list.append(vc)
            vcv_list.append(cv)
    return vcv_list


def name_generator(parts_list):
    generated_name = []
    name_length = random.randint(1, 4)
    j = 0
    for j in range(0, name_length):
        generated_name.append(random.choice(parts_list))
        j += 1

    yes_or_no = ['yes', 'no']
    cut_name = random.choice(yes_or_no)

    generated_name: str = ' '.join(generated_name)
    generated_name = generated_name.replace(' ', '')

    if name_length == 1:
        generated_name = list(generated_name)
        generated_name.append(random.choice(vowel_consonant))
    elif cut_name == 'yes' and name_length != 1:
        generated_name = list(generated_name)
        generated_name.pop(random.randrange(len(generated_name)))

    name_out: str = ' '.join(generated_name)
    name_out = name_out.replace(' ', '')
    name_out = name_out.capitalize()
    return name_out


def surname_generator(parts_list):
    generated_surname = []
    surname_length = random.randint(1, 4)
    k = 0
    for k in range(0, surname_length):
        generated_surname.append(random.choice(parts_list))
        k += 1

    surname_out: str = ' '.join(generated_surname)
    surname_out = surname_out.replace(' ', '')
    surname_out = surname_out.capitalize()

    prefix_choice = ['no', 'yes']
    prefix_yes_no = random.choice(prefix_choice)
    if prefix_yes_no == 'yes':
        prefix = random.choice(surname_prefix)
        surname_out = prefix + surname_out
    else:
        surname_out

    sufix_choice = ['no', 'yes']
    sufix_yes_no = random.choice(sufix_choice)

    if sufix_yes_no == 'yes':
        if surname_length <= 3:
            generated_surname2 = []
            surname_length = random.randint(2, 3)
            k = 0
            for k in range(0, surname_length):
                generated_surname2.append(random.choice(parts_list))
                k += 1

            surname_out2: str = ' '.join(generated_surname2)
            surname_out2 = surname_out2.replace(' ', '')
            surname_out2 = surname_out2.capitalize()
            surname_out = surname_out + '-' + surname_out2

        elif surname_out[1] != 's':
            surname_out = surname_out + 'sson'
        else:
            surname_out = surname_out + 'son'
    else:
        surname_out

    return surname_out


def fem_check(name):
    if name[-1] == 'a':
        return 'Lady'
    else:
        return 'Sir'


def land_maker():
    description = ['Silver', 'Dark', 'Moon', 'Green', 'Shadowy', 'Deep', 'Frozen', 'Fiery', 'Boring', 'Old']
    place = ['mine', 'forest', 'lake', 'mountain', 'town', 'tower', 'graveyard', 'swamps']
    land = random.choice(description) + random.choice(place)
    return land

def main():
    parts_list = parts_generator()
    name = name_generator(parts_list)
    surname = surname_generator(parts_list)
    title = fem_check(name)
    land = land_maker()

    print(f'{title} {name} {surname} of {land}')


if __name__ == '__main__':
    main()

