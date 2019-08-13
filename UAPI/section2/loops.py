my_variable = "hello"

# iterables are strings, lists, sets, tuples, and more
for character in my_variable:
    print(character)

user_wants_number = True
while user_wants_number == True:
    print(10)
    user_input = input('should we print again? (y/n)')
    if user_input == 'n':
        user_wants_number = False