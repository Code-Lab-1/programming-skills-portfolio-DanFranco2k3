pets = []

pet = {
    'animal type': 'guinea pig',
    'name': 'sofia',
    'owner': 'jay',
    'weight': 70,
    'eats': 'grass',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'nicole',
    'owner': 'joshua',
    'weight': 45,
    'eats': 'feeds',
}
pets.append(pet)

pet = {
    'animal type': 'monkey',
    'name': 'mylene',
    'owner': 'jeshua',
    'weight': 150,
    'eats': 'bananas',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")