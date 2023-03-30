vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'q', 's', 't', 'v',
             'x', 'z', 'h', 'r', 'w', 'y']
vowel_consonant = vowel + consonant




def parts_generator():
    vcv_list = []
    for v in vowel:
        for c in consonant:
            vc = v + c
            cv = c + v
            vcv_list.append(vc)
            vcv_list.append(cv)
    return vcv_list


