# 1.Turi turėti mažiausiai 12 simbolių.
# 2.Turi turėti bent 2 didžiąsiasraidės.
# 3.Turi turėti bent 2 mažąsiasraidės.
# 4.Turi turėti bent 2 skaičius.
# 5.Turi turėti bent 2 spec. simbolius (pvz., !, @, #, $ ir kt.).

with open('./duom4.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

results = []
for password_raw in lines:
    errors = []
    password = password_raw.strip()
    symbol_count = len(password)
    capital_letter_count = 0
    lower_letter_count = 0
    number_count = 0
    special_symbol_count = 0

    for char in password:
        if char.isalpha():
            if char.isupper():
                capital_letter_count += 1
            else:
                lower_letter_count += 1
        elif char.isnumeric():
            number_count += 1
        else:
            special_symbol_count += 1

    if symbol_count < 12:
        errors.append(f'Slaptažodis turi turėti mažiausiai 12 simbolių (Trūksta {12 - symbol_count} simbolių).')

    if capital_letter_count < 2:
        errors.append(f'Slaptažodis turi turėti bent 2 didžiąsias raides (Trūksta {2 - capital_letter_count} simbolių).')

    if lower_letter_count < 2:
        errors.append(f'Slaptažodis turi turėti bent 2 mažąsias raides (Trūksta {2 - lower_letter_count} simbolių).')
    
    if number_count < 2:
        errors.append(f'Slaptažodis turi turėti bent 2 skaičius (Trūksta {2 - number_count} simbolių).')

    if special_symbol_count < 2:
        errors.append(f'Slaptažodis turi turėti bent 2 spec. simbolius (Trūksta {2 - special_symbol_count} simbolių).')

    result = 'Slaptažodis tinkamas.'
    if len(errors) > 0:
        result = 'Slaptažodis netinkamas. ' + ' '.join(errors)
    results.append(f'{password} --- {result}\n')

with open('./rez4.txt', 'w', encoding='utf-8') as f:
    f.writelines(results)