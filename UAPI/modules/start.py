import support
from   support import helloWorld
# from support import * # you can also do this
# Import built-in module math
import math

support.print_func('Zara')
#print_func('Zara') #this won't work without the module name support
helloWorld() # however, this can work
support.helloWorld() # and this is also valid


#variables and and Scoping
Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

print(Money)
AddMoney()
print(Money)

content = dir(math)
print(content)

myModuleNames = dir(support)
print(myModuleNames)



# The reload() Function
# When the module is imported into a script, the code in the top-level portion of a module is executed only once.
# Therefore, if you want to reexecute the top-level code in a module, you can use the reload() function. The reload() function imports a previously imported module again. The syntax of the reload() function is this −
# reload(module_name)

