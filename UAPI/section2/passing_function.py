#this file is an example of declartive programming 
#which is a part of functional programming
def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

#notice add_two_numbers not having a () 
#passing a function to another, kinda like flutter
print(methodception(add_two_numbers))

#a lambda function is an annoymouse function
print(methodception(lambda: 35 + 77))

my_list = [13, 56, 77, 48]
print(list(filter(lambda x: x != 13, my_list)))

(lambda x: x * 3)(5)

def f(x):
    return x * 3

f(5)

