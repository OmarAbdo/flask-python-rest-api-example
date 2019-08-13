# python dictionaries are associative arrayes

my_dict = {
    'name': 'Jose',
    'age' : 50,
    'grades' : [13, 45, 66, 92]
}

another_dict = {1: 15, 2: 20, 3: 45}

lottery_player = {
    'name': 'Rolf',
    'number': (12, 43, 54, 423)
}

universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

nested_dictionary = {
    'one': {
        'name' : 'some thing',
        'age' : 1234,
    },
    'two': {
        'name' : 'something else',
        'age' : 1234,
    },
}

print(sum(lottery_player['number']))