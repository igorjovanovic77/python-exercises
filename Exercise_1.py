print("Hello World!")
if 3 >= 2:
    print("Correct!")

x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

speed_of_light = 299792458   # meters per second
cycles_per_second = 2700000000  # 2.7 GHz

cycle_distance = speed_of_light / cycles_per_second

cycles_per_second = 2800000000

print(cycle_distance)

cycle_distance = speed_of_light / cycles_per_second

print(cycle_distance)

s = "start here, please"
t = "here"
print(s.find(t, 2))
print(s[2:].find(t))
# print(s.find(t)[:2])
print(s[2:].find(t) + 2)
print(s[2:].find(t[2:]))



# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url',
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
# print(start_link)
double_quote = page.find('"', start_link)
# print(double_quote)
double_quote_2 = page.find('"', double_quote + 1)
# print(double_quote_2)
url = page[double_quote + 1:double_quote_2]
print(url)




# Problem: We will be given a list of numbers as inputs. We want to
# return a list with all the prime numbers from the original list.

def find_primes(number_list):
 prime_list = []
 for n in number_list:
    if True:
        prime_list.append(n)
 return prime_list

def is_prime(number):
 if (number <= 1) or (number != int(number)):
    return False
 for i in range(2, number):
    if number%i == 0:
     return False
 return True


def find_primes(number_list):
 prime_list = []
 for n in number_list:
    if is_prime(n):
        prime_list.append(n)
 return prime_list


# quiz: find 2nd 'zip'
print("# quiz: find 2nd 'zip'")

text ='zip files are zipped'

# 1
first = text.find('zip')
second = text.find('zip', first + 1)
print(second)

# 2
first = text.find('zip')
print(text.find('zip', first + 1))

# 3
print(text.find('zip', text.find('zip')+ 1))


# quiz: rounding numbers
print("# quiz: rounding numbers")

x = 3.74159
num = x + 0.5
s = str(num)
point = s.find('.')
print(s[:point])

z = 3.2594
num = z + 0.5
print(int(num))


# text replacement:
print("# text replacement:")

# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 # uncomment this to test with different input
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

replaced = line[:line.find(marker)] + replacement + line[line.find(marker)+len(marker):]

print(replaced)

# Palindrome exercise
print("# Palindrome exercise")
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.

word = "madam"
# word = "madman"

is_palindrome = word.find(word[::-1])

print(is_palindrome)


# using procedures
print("# using procedures")

# 1
s = "milisav je sisa"
def rest_of_string(s):
    return s[1:]

print (rest_of_string("tucak"))

# 2
def inc(n):
    return n + 1

print(inc(7))

# 3
def sum(a,b):
    print("enter sum!")
    print("a is", a)
    a = a + b
    print("a is", a)
print(sum(2, 123))

# 4
def sum(a, b):
    a = a + b
    return a
print(sum(2, 123))

s = 'Hello '
t = 'Igor!'
print(sum(s, t))

# 5
def square(n):
    return n * n

print(square(5))
# or:
x = 37
print(square(x))
# or:
x = 37
y = square(x)
print(square(y))
# or:
x = 37
print(square(square(x)))  # this is called "procedure composition"

# 6
def sum3(a, b, c):
    return a + b + c

print(sum3(1, 2, 3))

# 7
def abbaize(a, b):
    return a + b * 2 + a

print(abbaize('a', 'b'))
print(abbaize('dog', 'cat'))

# 8
def find_second(search, target):
    first = search.find(target)
    second = search.find(target, first + 1)
    return second
# or:
def find_second(search, target):
    first = search.find(target)
    return search.find(target, first + 1)
# or:
def find_second(search, target):
    return search.find(target, search.find(target) + 1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print(find_second(danton, 'audace'))


# equality comparisons
print("# equality comparisons")

print(2 < 3)
print(21 < 3)
print(7 * 3 < 21)
print(7 * 3 != 21)  # not equal
print(7 * 3 == 21)  # equal


# if practice
print("# if practice")

# 1
def absolute(x):
    if x < 0:
        x = - x
    return x
print(absolute(-57))

# 2 (moj)
def bigger(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return a

# or:
def bigger(a, b):
    if a > b:
        return a
    return b

# or:
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

# or:
def bigger(a, b):
    if a > b:
        r = a
    else:
        r = b
    return r

print(bigger(2,7))
print(bigger(3,2))
print(bigger(3,3))


# is_friend exercise:
print("# is_friend exercise:")

def is_friend(name):
    if name[0] == 'D':
        return True
    else:
        return False
# or:
def is_friend(name):
    if name[0] == 'D':
        return True
    return False
# or:
def is_friend(name):
    return name[0] == 'D'

print(is_friend('Diane'))
print(is_friend('Fred'))


# is_friend 2 exercise:
print("# is_friend 2 exercise:")

def is_friend(name):
    if name[0] == 'D':
        return True
    elif name[0] == 'N':
        return True
    return False
# or:
def is_friend(name):
    if name[0] == 'D':
        return True
    else:
        if name[0] == 'N':
            return True
        else:
            return False
# or:
def is_friend(name):
    return name[0] == 'D' or name[0] == 'N'

print(is_friend('Diane'))
print(is_friend('Ned'))
print(is_friend('Moe'))


# 'or' keyword:
print("# 'or' keyword:")

print(True or False)
print(False or True)
print(True or True)
print(False or False)

# 'or' biggest of 3 test (moj):
print("# 'or' biggest of 3 test (moj):")

def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= b and c >= a:
        return c
# or:
def biggest(a, b, c):
    if a > b:
        if a > c:
            return a
        else:           # c >= a > b
            return c
    else:               # b >= a
        if b > c:
            return b
        else:           # c >= b >= a
            return c
# or using already defined procedure def bigger(a, b)
def biggest(a, b, c):
    return bigger(bigger(a, b), c)

print(biggest(3, 6, 9))
print(biggest(6, 9, 3))
print(biggest(9, 3, 6))
print(biggest(3, 3, 9))
print(biggest(9, 3, 9))

# or using built-in operator 'max' directly:
a = 5
b = 7
c = 12

print(max(a, b, c))


# while loop:
print("# while loop:")

# example 1:
i = 0
while i< 10:
    print(i)
    i = i + 1

# example 2:
i = 0
while i != 10:
    i = i + 1
    print(i)

# example 3:
# i = 1
# while i != 10:
#     i = i + 2
#     print(i) # it runs forever

# example 4:
def print_numbers(n):
    i = 1
    while i <= n:
        print(i)
        i = i + 1
print_numbers(3)

# example 5 (factorial):
print("# example 5 (factorial):")

def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result
print(factorial(4))

# moj
def factorial(n):
    i = 0
    k = 1
    while i < n:
        k = k * (i + 1)
        i = i + 1
    return k
# moj:
def factorial(n):
    i = 1
    k = 1
    while i <= n:
        k = k * i
        i = i + 1
    return k
print(factorial(5))


# break
# n = 6
# while n > 5:
#     print(n + n)

# while n > 5:  # the same
#     if False:
#         break
#     print(n + n)

# while n > 5:
#     print(n + n)
#     break

# while True:
#     if n > 5:  # it would be the same if we had: if not n > 5
#         break
#     print(n + n)

# while n > 5:  # the same
#     print(n + n)
#     if n > 5:
#         print(n + n)
#     else:
#         break

# Multiple Assignment
print("# Multiple Assignment")

s = 1
t = 2
s, t = t, s
print(s, t)

# L6.1 Udacify
print("# L6.1 Udacify")

def udacify(s):
    return 'U' + str(s)
print(udacify(54367))

# L6.3 Median
print("# L6.3 Median")
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

# moj:
def median(a,b,c):
    if biggest(a,b,c) == a:
        if b >= c:
            return b
        return c
    if biggest(a,b,c) == b:
        if a >= c:
            return a
        return c
    if biggest(a,b,c) == c:
        if a >= b:
            return a
        return b

#njihov:
def median(a,b,c):
    big = biggest(a, b, c)
    if big == a:
        return bigger(b, c)
    if big == b:
        return bigger(a, c)
    else:
        return bigger(a, b)
print(median(1,2,3))
print(median(9,3,6))
print(median(7,8,7))


# L6.4 Blastoff
print("# L6.4 Blastoff")

def countdown(n):
    while n >= 1:
        print(n)
        n = n - 1
    else:
        print("Blastoff!")

countdown(3)


# L6.5 Finish (Hint: 0 is not a positive integer)
print("# L6.5 Finish")

# 1 - it always finishes:
n = 6  # any positive integer
i = 0
while i <= n:
    i = i + 1

# 2 - it always finishes:
n = 4  # any positive integer
i = 1
while True:
    i = i * 2  # exponential
    n = n + 1  # linear
    if i > n:
        break

# 3 - unknown to anyone:
n = 77  # any positive integer
while n != 1:
    if n % 2 == 0: #n is even
        n = n/2
    else:
        n = 3 * n + 1
print(n)

# L6.6 Find Last
print("# L6.6 Find Last")

def find_last(s, t):
    last_pos = -1
    while True:
        pos = s.find(t, last_pos + 1)
        if pos == -1:
            return last_pos
        last_pos = pos
print(find_last('aaaa', 'a'))
print(find_last('aaaaa', 'aa'))
print(find_last('aaaa', 'b'))
print(find_last("111111111", "1"))
print(find_last("222222222", ""))
print(find_last("", "3"))
print(find_last("", ""))

# moj - nije dobar:
print("# moj")
def find_last(s, t):
    position = s.find(t)
    if position == -1:
        return position
    while position >= 0:
        position = position + 1
        position = s.find(t, position)
    return position
print(find_last('aaaa', 'a'))
#print(find_last('aaaaa', 'aa'))
#print(find_last('aaaa', 'b'))

# Ivo
def find_last(s, t):
    position = s.find(t)
    position2 = 0
    if position == -1:
        return position
    while position >= 0:
        if position2 == -1:
            return position -1
        position = position + 1
        position2 = s.find(t, position)

print(find_last('aaaa', 'a'))
print(find_last('aaaaa', 'aa'))
print(find_last('aaaa', 'b'))


# L7.1 Quiz: Weekend
print("# L7.1 Quiz: Weekend")

def weekend(day):
    # your code here
    if day == "Saturday":
        return True
    elif day == "Sunday":
        return True
    return False

# or:
def weekend(day):
    return day =="Sunday" or day == "Saturday"

print(weekend('Monday'))
print(weekend('Saturday'))
print(weekend('July'))


# L7.2 Quiz: Stamps
print("# L7.2 Quiz: Stamps")

def stamps(n):
    x = int(n/5)
    y = int((n % 5) / 2)
    z = int(n - int((n/5))*5 - int((n % 5) / 2) * 2)
    return (x, y, z)

# or:

def stamps(n):
    return int(n / 5), int(n % 5 / 2), int(n % 5 % 2)

print(stamps(8))
print(stamps(5))
print(stamps(29))
print(stamps(0))


# L7.3 Quiz: Range of a Set
print("# L7.3 Quiz: Range of a Set")
# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

def biggest(a, b, c):
    if a > b and a > c:
        return a
    if b > c and b > a:
        return b
    if c > a and c > b:
        return c


def smallest(a, b, c):
    if a < b and a < c:
        return a
    if b < c and b < a:
        return b
    if c < a and c < b:
        return c


def set_range(a, b, c):
    return biggest(a, b, c) - smallest(a, b, c)

# or:
def set_range(a, b, c):
    return max(a, b, c) - min(a, b, c)

print(set_range(10, 4, 7))
#>>> 6  # since 10 - 4 = 6

print(set_range(1.1, 7.4, 18.7))
#>>> 17.6 # since 18.7 - 1.1 = 17.6


# U8.1 Quiz: Superhero Nuisance
print("# U8.1 Quiz: Superhero Nuisance")
# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# moj:
def fix_machine(debris, product):
    i = len(product) - 1
    while i >= 0:
        debris.find(product[i])
        i = i - 1
    if debris.find(product[i]) < 0:
        return "Give me something that's not useless next time."
    else:
        return product

# 2(for loop):
def fix_machine(debris, product):
    for i in product:
        if i not in debris:
            return "Give me something that's not useless next time."
    return product

print("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity'))
print("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity'))
print("Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity'))
print("Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt'))
print("Test case 5: ", fix_machine('bruy me dat Unicornt', 'ertu'))
print("Test case 6: ", fix_machine('bruy me dat Unicornt', ''))
print(len(''))


# U8.2 Quiz: Days Old
print("# U8.2 Quiz: Days Old")

def leapYear(year):
    if year % 4 > 0:
        return "It is a common year"
    elif year % 100 > 0:
        return "It is a leap year"
    elif year % 400 > 0:
        return "It is a common year"
    else:
        return "It is a leap year"
print(leapYear(1977))

def daysPerYear(year):
    if year % 4 > 0:
        return 365
    elif year % 100 > 0:
        return 366
    elif year % 400 > 0:
        return 365
    else:
        return 366
print(daysPerYear(1980))

def daysBetweenYears(year1, year2):
    if year2 - year1 == 1:
        result = 0
        return result
    year = year2 - 1
    result = daysPerYear(year1 + 1)
    while year > year1 + 1:
        result = result + daysPerYear(year)
        year = year - 1
    return result
print(daysBetweenYears(1999, 2002))


def daysOfMonths1Sum(year1, month1):
    if month1 == 12:
        month1Sum = 0
        return month1Sum
    daysOfMonths1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysOfMonths2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if daysPerYear(year1) == 365:
        n = 11
        month1Sum = daysOfMonths1[month1]
        while n > month1:
            month1Sum = month1Sum + daysOfMonths1[n]
            n = n - 1
        return month1Sum
    if daysPerYear(year1) == 366:
        n = 11
        month1Sum = daysOfMonths2[month1]
        while n > month1:
            month1Sum = month1Sum + daysOfMonths2[n]
            n = n - 1
        return month1Sum
print(daysOfMonths1Sum(1977, 1))


def daysOfMonths2Sum(year2, month2):
    if month2 == 1:
        month2Sum = 0
        return month2Sum
    daysOfMonths1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysOfMonths2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if daysPerYear(year2) == 365:
        n = month2 - 2
        month2Sum = daysOfMonths1[0]
        while n > 0:
            month2Sum = month2Sum + daysOfMonths1[n]
            n = n - 1
        return month2Sum
    if daysPerYear(year2) == 366:
        n = month2 - 2
        month2Sum = daysOfMonths2[0]
        while n > 0:
            month2Sum = month2Sum + daysOfMonths2[n]
            n = n - 1
        return month2Sum
print(daysOfMonths2Sum(2020, 3))


def daysOfMonth1(year1, month1, day1):
    if month1 in (1, 3, 5, 7, 8, 10, 12):
        numOfDays1 = 31 - day1
        return numOfDays1
    if month1 in(4, 6, 9, 11):
        numOfDays1 = 30 - day1
        return numOfDays1
    if daysPerYear(year1) == 365 and month1 == 2:
        numOfDays1 = 28 - day1
        return numOfDays1
    if daysPerYear(year1) == 366 and month1 == 2:
        numOfDays1 = 29 - day1
        return numOfDays1
print(daysOfMonth1(1977, 7, 21))


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if month1 > 12 or month2 > 12:
        return "This is not a valid month input"
    if day1 > 31 or day2 > 31:
        return "This is not a valid day input"
    if month1 in (4, 6, 9, 11) and day1 > 30 or month2 in (4, 6, 9, 11) and day2 > 30:
        return "This is not a valid day input"
    if daysPerYear(year1) == 365 and month1 == 2 and day1 > 28 or \
       daysPerYear(year2) == 365 and month2 == 2 and day2 > 28:
        return "This is not a valid day input"
    if daysPerYear(year1) == 366 and month1 == 2 and day1 > 29 or \
       daysPerYear(year2) == 366 and month2 == 2 and day2 > 29:
        return "This is not a valid day input"
    if year1 > year2:
        year1, year2 = year2, year1
        month1, month2 = month2, month1
        day1, day2 = day2, day1

    if year1 == year2 and month1 == month2 and day1 == day2:
        return 0
    if year1 == year2 and month1 == month2 and day1 > day2:
        return day1 - day2
    if year1 == year2 and month1 == month2 and day2 > day1:
        return day2 - day1

    if year1 == year2 and month1 > month2:
        month1, month2 = month2, month1
        day1, day2 = day2, day1

    if year1 == year2 and month2 > month1:
        if month2 - month1 == 1:
            return day2 + daysOfMonth1(year1, month1, day1)
        return daysOfMonths2Sum(year2, month2) - daysOfMonths2Sum(year1, month1 + 1) + \
                   daysOfMonth1(year1, month1, day1) + day2

    return daysBetweenYears(year1, year2) + \
           daysOfMonths1Sum(year1, month1) + \
           daysOfMonths2Sum(year2, month2) + \
           daysOfMonth1(year1, month1, day1) + \
           day2

print(daysBetweenDates(2020, 1, 1, 2020, 1, 4))
print(daysBetweenDates(2012, 1, 1, 2012, 2, 28))
print(daysBetweenDates(2012, 1, 1, 2012, 3, 1))
print(daysBetweenDates(2011, 6, 30, 2012, 6, 30))
print(daysBetweenDates(2011, 1, 1, 2012, 8, 8))
print(daysBetweenDates(1900, 1, 1, 1999, 12, 31))


# U8.4 Quiz: Jungle Animal
print("# U8.4 Quiz: Jungle Animal")

def jungle_animal(animal, my_speed):
    if animal == 'zebra':
        print("Try to ride a zebra!")
    elif animal == "cheetah":
        if my_speed > 115:
            print('Run!')
        elif my_speed <= 115:
            print("Stay calm and wait!")
    else:
        print("Introduce yourself!")

jungle_animal('cheetah', 30)
jungle_animal('gorilla', 21)


# U10.21 Quiz: Define Simple nextDay
print("# U10.21 Quiz: Define Simple nextDay")
# (moj):
def isLeapYear(year):
    if year % 4 > 0:
        return False
    elif year % 100 > 0:
        return True
    elif year % 400 > 0:
        return False
    else:
        return True

# (njegov):
def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    return 30

# moj(ne resava greske ako je datum pogresan, e.g. month ==13, day == 31):
def nextDay(year, month, day):
    if month == 12 and day == 30:
        return year + 1, 1, 1
    if day == 30:
        return year, month + 1, 1
    return year, month, day + 1

# njihov:
def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    if month < 12:
        return year, month + 1, 1
    return year + 1, 1, 1

print(nextDay(1999, 12, 30))
print(nextDay(2013, 1, 30))
print(nextDay(2012, 12, 32))

# Helper Function (moj):
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2 and month1 < month2:
        return True
    if year1 == year2 and month1 == month2 and day1 <= day2:
        return True
    return False

# njihov:
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

print(dateIsBefore(2012,9,30,2012,10,30))
print(dateIsBefore(2012,1,1,2013,1,1))
print(dateIsBefore(2012,9,1,2012,9,4))

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days +=1
    return days

print(daysBetweenDates(2012,9,30,2012,10,30))
print(daysBetweenDates(2012,1,1,2013,1,1))
print(daysBetweenDates(2012,9,1,2012,9,4))




