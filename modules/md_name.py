from modules.md_parts import parts_generator, vowel, consonant
import random


def name_generator(name_parts, he_her):
    generated_name = []
    name_ln = random.randint(2, 4)

    for i in range(0, name_ln):
        generated_name.append(random.choice(name_parts))
        i += 1

    generated_name: str = ' '.join(generated_name)
    generated_name = generated_name.replace(' ', '')
    generated_name = generated_name.capitalize()
    for x in range(0, len(generated_name)):
        gen_name_lis = []
        gen_name_lis.append(generated_name[x])

    generated_name = list(generated_name)
    rand = random.randint(0, 1)
    if rand == 0:
        rem = random.choice(generated_name)
        generated_name.remove(rem)

    if he_her == 'he':
        if generated_name[-1] == 'a':
            if generated_name[-2] in vowel:
                generated_name[-1] = 'o'
            else:
                generated_name[-1] = random.choice(consonant)

    elif he_her == 'her':
        if generated_name[-1] == 'a':
            pass
        else:
            generated_name[-1] = 'a'

    generated_name: str = ' '.join(generated_name)
    generated_name = generated_name.replace(' ', '')
    generated_name = generated_name.capitalize()

    return generated_name


