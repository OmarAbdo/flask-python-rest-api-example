should_continue = True
if should_continue:
    print('Hello')

known_people = ['John', 'Anna', 'Mary']
person = input("Enter the person you know: ")

if person in known_people:
    print('You know {}!'.format(person))
    #print('You know {person}!') # this syntax is wrong
else:
    print('You don\'t know {}!'.format(person))

    
