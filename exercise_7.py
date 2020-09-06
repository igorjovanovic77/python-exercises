# Udemy: Automated Software Testing with Python

# Python refresher, u14:
print("# Python refresher, L14:")

def who_do_you_know():
    people = input("Enter the names of people you know,separated by commas:")  #John,Rolf,Anna,Greg
    people_list = people.split(",")  # ["John", "Rolf", "Anna", "Greg"]
    return people_list

# print(who_do_you_know())

print("list operations")
my_list = [0, 1, 2, 3, 4]
new_list = [n * 3 for n in range(5)]
print(new_list)

print("Python refresher L19 Objects in Python")

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = [5, 9, 12, 3, 1, 21]

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("John")
print(player_two.name)
print(player_one.numbers)


print("L20 A Student Example")

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
print(anna.average())
print(anna.marks)



print("L21 Classes and Objects exercise")
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        # total = 0
        # for item in self.items:
        #     total += item['price']
        # return total
        return sum([item['price'] for item in self.items])




