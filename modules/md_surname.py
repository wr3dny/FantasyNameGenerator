import random
surname_prefix = ['Mac', 'Mc', 'O\'', 'al-', 'ibn ']


def surname_generator(parts_list):
    generated_surname = []
    surname_length = random.randint(2, 4)
    k = 0
    for k in range(0, surname_length):
        generated_surname.append(random.choice(parts_list))
        k += 1

    surname_out: str = ' '.join(generated_surname)
    surname_out = surname_out.replace(' ', '')
    surname_out = surname_out.capitalize()

    options = ['nothing', 'prefix', 'suffix', 'double', 'double + prefix', 'double + suffix']

    switch = random.choices(options, weights=[9, 3, 3, 3, 1, 1], k=1)

    match(switch):
        case ['nothing']:
            surname_out = surname_out
        case ['prefix']:
            prefix = random.choice(surname_prefix)
            surname_out = prefix + surname_out
        case ['suffix']:
            surname_out = surname_out + 'son'
        case ['double']:
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
        case ['double + prefix']:
            prefix = random.choice(surname_prefix)
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
            surname_out = prefix + surname_out
        case ['double + suffix']:
            generated_surname2 = []
            surname_length = random.randint(2, 3)
            k = 0
            for k in range(0, surname_length):
                generated_surname2.append(random.choice(parts_list))
                k += 1
            surname_out2: str = ' '.join(generated_surname2)
            surname_out2 = surname_out2.replace(' ', '')
            surname_out2 = surname_out2.capitalize()
            surname_out2 = surname_out + '-' + surname_out2
            surname_out = surname_out2 + 'son'

    return surname_out

