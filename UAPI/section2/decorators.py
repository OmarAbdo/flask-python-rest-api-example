import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I'm the function!")

#my_function()

# decorator with arguments
# you can do more in decorator like inserting into a db not generally they are not used a lot
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print('In the decorator!')
            if number == 56:
                print("Not running the functino!")
            else:
                func(*args, **kwargs)
            print('After the decorator!')
        return function_that_runs_func
    return my_decorator            

@decorator_with_arguments(57)
def my_function_too(x, y):
    print(x + y)

my_function_too(57, 88)