my_variable = "hello"
grades_list = [77, 80, 99, 100] # a list
grades_tuple = (77, 80, 99, 100) # a tuple (immutable lists)
grades_sets =  {77, 80, 99, 100} # a unique and unordered 

print(sum(grades_tuple) / len(grades_tuple))
grades_list.append(55)

# you can't add to a tuple but you can change it enterily  
# notice the , if it doesn't exists then it's a useless number with a ()
grades_tuple = grades_tuple + (100,) 
print(grades_tuple)

