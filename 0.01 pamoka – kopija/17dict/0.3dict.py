#papildymas palyginmas (update)
auto_geras = {
    'Marke' : 'Opel',
    'Kainas' : 2500,
    'Turis' : 1.4,
    'Dauztas' : False
}

auto_blogas = {
    'Dauztas' : False,
    'Turis' : 1.4,
     'Kainas' : 2500,
    'Marke' : 'Opel',
}

print(id(auto_geras))
print(id(auto_blogas))

print(auto_geras == auto_blogas)

daugiau_info={
    'Rida':252525,
    'Splava' : 'Kibiras',
    'Kaina' : 3500
}

auto_geras.update(daugiau_info)
print(auto_geras)

auto_kitas = auto_blogas|daugiau_info
print(auto_kitas)