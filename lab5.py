import string

text = 'щ  зсдлъэд фцяб  цоцюъбк сня пбь  емйюсцдъ й  цяъцк'
symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' # + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper() + string.ascii_letters
print(text)

def n_grams(text, n):
    d = {}
    for key in range(len(text)):
        sub_text = text[key : key+n]
        if d.get(sub_text):
            d[sub_text] += 1
        else:
            d[sub_text] = 1
    return d

d_two = n_grams(text, 2)
print(d_two, len(d_two))

d_three = n_grams(text, 3)
print(d_three, len(d_three))