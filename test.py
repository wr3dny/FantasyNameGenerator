def female_name(name):
    if name[-1] == 'a':
        fem_name = name
    else:
        fem_name = name + 'a'
    return fem_name

name_to_check = 'Ada'

print(female_name(name_to_check))