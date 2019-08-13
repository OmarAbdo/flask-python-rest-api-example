#!/usr/bin/python

# print("Hello, Python!")
# # raw_input("\n\nPress the enter key to exit.")


# var1 = 100
# if var1:
#     print("1 - Got a true expression value")
#     print(var1)

# var = 100
# if var == 200:
#    print "1 - Got a true expression value"
#    print var
# elif var == 150:
#    print "2 - Got a true expression value"
#    print var
# elif var == 100:
#    print "3 - Got a true expression value"
#    print var
# else:
#    print "4 - Got a false expression value"
#    print var

# print "Good bye!"

# def printme( str ):
#     "This prints a passed string into this function"
#     123
#     print(str)
#     return
# printme('omar')

#!/usr/bin/python

# Function definition is here
def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print( "Output is: ")
    print( arg1)
    for var in vartuple:
       print(var)
    return;
 
# Now you can call printinfo function
#printinfo(arg1 = 10)
# printinfo(arg1 = 10, 70, 50, 11) # won't work
printinfo(10)
printinfo(70, 60, 50)

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )