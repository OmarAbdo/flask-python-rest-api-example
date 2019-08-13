def my_method(arg1, arg2):
    return arg1 + arg2

#endless params like the the rest param ...args in js
def addtion_simplified(*args):
    return sum(args)
#what_are_kwagrs? they are named params
def what_are_kwagrs(*args, **kwagrs):
    print(args)
    print(kwagrs)    

#notice that the posional args must come first then the 
#named args can come later in any order
def named_with_postional_args(arg1, name, age):
    print(name)
    print(age)

what_are_kwagrs(12,11,13, name='Jose', location='UK')
named_with_postional_args(36, name="omar", age="22")