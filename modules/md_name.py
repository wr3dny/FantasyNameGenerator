from modules.md_parts import parts_generator, vowel_consonant
import random

mixed = parts_generator()

female = 'female'

# def name_generator(parts_list, sex):
#     female_q = str(sex)
generated_name = []
name_ln = random.randint(2, 5)

print(name_ln)
for i in range(0, name_ln):
    generated_name.append(random.choice(mixed))
    i += 1

    print(generated_name)
# if female_q == 'female':

generated_name[-1] = 'a'
generated_name: str = ' '.join(generated_name)
generated_name = generated_name.replace(' ', '')
generated_name = generated_name.capitalize()



if generated_name[-1] == generated_name[-2]:
    print("Double aa")


print(generated_name)



    # return generated_name






    # generated_name = []
    # name_length = random.randint(1, 4)
    # j = 0
    # for j in range(0, name_length):
    #     generated_name.append(random.choice(parts_list))
    #     j += 1
    #
    # generated_name: str = ' '.join(generated_name)
    # generated_name = generated_name.replace(' ', '')
    #
    # print(f'first generated {generated_name}')
    # generated_name = list(generated_name)
    # print(f'second generated {generated_name}')
    #
    #
    # if random.randint(0, 1) == 1:
    #     print(generated_name)
    #     generated_name.pop(-1)
    #     print(generated_name)
    #     generated_name = generated_name + ['a']
    #     print(generated_name)
    #
    # else:
    #     generated_name
    #
    # yes_or_no = ['yes', 'no']
    # cut_name = random.choice(yes_or_no)
    #
    # generated_name: str = ' '.join(generated_name)
    # generated_name = generated_name.replace(' ', '')
    #
    # if name_length == 1:
    #     generated_name = list(generated_name)
    #     generated_name.append(random.choice(vowel_consonant))
    # elif cut_name == 'yes' and name_length != 1:
    #     generated_name = list(generated_name)
    #     generated_name.pop(random.randrange(len(generated_name)))
    #     print(generated_name)
    #     ln = len(generated_name)
    #     print(ln)
    #
    # name_out: str = ' '.join(generated_name)
    # name_out = name_out.replace(' ', '')
    # name_out = name_out.capitalize()
    # return name_out


