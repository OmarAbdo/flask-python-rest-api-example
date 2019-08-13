lottery_player_dict = {
    'name' : 'Rolf',
    'numbers': (5,9,12,3,1,21)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

playerOne = LotteryPlayer('Omar')
playerOne.numbers = (1,2,4,5,6)
playerTwo = LotteryPlayer('Ali')

print(playerOne.name)
print(playerOne.total())
print(playerOne.numbers == playerTwo.numbers)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    #@staticmethod & @classmethod are called decerators 
    @staticmethod 
    def go_to_school():
        #print("I'm going to {}.".format(self.school))
        print("I'm going to school")


anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")

anna.marks.append(56)
print(anna.marks)
Student.go_to_school()
