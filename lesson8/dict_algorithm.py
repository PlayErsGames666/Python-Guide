person = {
    'user_1' : {
        'first_name': 'Haram',
        'last_name': 'Mutanov',
        'age': 37,
        'address': ['c. Tashkent', 'dis. Maxim Gorkiy', 'h/a 14/156'],
        'hobby': ['coding', 'gaming', 'rest', 'dalbayob'],
        'grades': {'math': 5, 'geography': 4, 'chemistry': 3},
    },
    'user_2' : {

    }
}

print(person.items())
print(person['user_1']['hobby'][3])