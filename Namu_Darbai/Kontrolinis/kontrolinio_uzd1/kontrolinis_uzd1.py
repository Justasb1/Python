with open('./duom1.txt', 'r') as f:
    lines = f.readlines()

result = []
for line in lines:
    deciphered_chars = []
    for char in line:
        ascii_code = ord(char)
        if ascii_code >= 65 and ascii_code <= 90:
            deciphered_chars.append(chr((90 - ascii_code) + 65))
            continue
        if ascii_code >= 97 and ascii_code <= 122:
            deciphered_chars.append(chr((122 - ascii_code) + 97))
            continue
        deciphered_chars.append(char)
    deciphered_string = ''.join(deciphered_chars)
    result.append(deciphered_string)

with open('./rez1.txt', 'w') as f:
    f.writelines(result)