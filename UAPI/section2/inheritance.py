class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self): 
        return sum(self.marks) / len(self.marks)

    def friend(self, friend_name):
        #return a new student called 'friend_name' in the same school as self
        return Student(friend_name, self.school) #creating a new instance on the fly

anna = Student('Anna', 'Oxford')

friend = anna.friend("Greg")
print(friend.name)
print(friend.school)


#inheritance in python, you pass the parent class name in () to the subclass
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school) # calling the parent class init function via the super() method and then using it to set the name and the school values of the subclass
        self.salary = salary

anna = WorkingStudent('Anna', 'Oxford', 20.00)
print(anna.salary)

