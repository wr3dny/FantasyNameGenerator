import random
from md_parts import vowel_consonant, parts_generator
surname_prefix = ['Mac', 'Mc', 'O\'', 'al-', 'ibn ']
surname_suffix = ['son', 'sson']


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
    # else:
    #     surname_out

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
    # else:
    #     surname_out

    return surname_out


print(surname_generator(parts_generator()))