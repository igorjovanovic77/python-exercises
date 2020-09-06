# U22.9 Quiz: Recursive Factorial
print("# U22.9 Quiz: Recursive Factorial")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)

print(factorial(0))
#>>> 1
print(factorial(5))
#>>> 120
print(factorial(10))
#>>> 3628800


# U22.10 Quiz: Palindromes
print("# U22.10 Quiz: Palindromes")

def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] != s[-1]:
            return False
        else:
            return is_palindrome(s[1:-1])

print(is_palindrome(''))
#>>> True
print(is_palindrome('abab'))
#>>> False
print(is_palindrome('abcba'))
#>>> True


# U22.11 Quiz: Recursive Vs Iterative
print("# U22.11 Quiz: Recursive Vs Iterative")

def iter_palindrome(s):
    for i in range(0, int(len(s) / 2)):
        if s[i] != s[-(i + 1)]:
            return False
    return True

print(iter_palindrome(''))
#>>> True
print(iter_palindrome('abab'))
#>>> False
print(iter_palindrome('abcba'))
#>>> True


# U22.12 Quiz: Bunnies (Fibonacci)
print("# U22.12 Quiz: Bunnies (Fibonacci)")

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(0))
#>>> 0
print(fibonacci(1))
#>>> 1
print(fibonacci(15))
#>>> 610


# U22.15 Quiz: Faster Fibonacci
print("# U22.15 Quiz: Faster Fibonacci")

#moj:
def fibonacci(n):
    a = 0
    b = 1
    result = 0
    k = 0
    while k < n - 1:
        result = a + b
        a = b
        b = result
        k += 1
    return result

# njihov:
def fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

print(fibonacci(5))
print(fibonacci(36))
#>>> 14930352


# U23.2 Quiz: Rabbits Multiplying
print("# U23.2 Quiz: Rabbits Multiplying")
# Define a procedure rabbits that takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.
# For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)

# moj:
def rabbits(n):
    if n == 0 or n == 1:
        return n
    if n in range(2, 5):
        return rabbits(n-1) + rabbits(n - 2)
    else:
        return rabbits(n-1) + rabbits(n - 2) - rabbits(n - 5)

# njihov:
def rabbits(n):
    if n < 1:  # no rabbits dead yet
        return 0
    else:
        if n == 1 or n == 2:  # base case defined in problem statement
            return 1
        else:
            return rabbits(n-1) + rabbits(n - 2) - rabbits(n - 5)  # formula from problem statement

print(rabbits(10))
#>>> 35
s = ""
for i in range(1, 12):
    s = s + str(rabbits(i)) + " "
print(s)
#>>> 1 1 2 3 5 7 11 16 24 35 52


# U23.3 Quiz: Spreading Udaciousness
print("# U23.3 Quiz: Spreading Udaciousness")
# One of our modest goals is to teach everyone in the world to program and
# understand computer science. To estimate how long this will take we have
# developed a (very flawed!) model:

# Everyone answering this question will convince a number, spread, (input to
# the model) of their friends to take the course next offering. This will
# continue, so that all of the newly recruited students, as well as the original
# students, will convince spread of their
# friends to take the following offering of the course.
# recruited friends are unique, so there is no duplication among the newly
# recruited students. Define a procedure, hexes_to_udaciousness(n, spread,
# target), that takes three inputs: the starting number of Udacians, the spread
# rate (how many new friends each Udacian convinces to join each hexamester),
# and the target number, and outputs the number of hexamesters needed to reach
# (or exceed) the target.

# For credit, your procedure must not use: while, for, or import math.

def hexes_to_udaciousness(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + hexes_to_udaciousness(n + n * spread, spread, target)  # ili n * (1 + spread)


# 0 more needed, since n already exceeds target
print(hexes_to_udaciousness(100000, 2, 36230))
#>>> 0

# after 1 hexamester, there will be 50000 + (50000 * 2) Udacians
print(hexes_to_udaciousness(50000, 2, 150000))
#>>> 1

# need to match or exceed the target
print(hexes_to_udaciousness(50000, 2, 150001))
#>>> 2

# only 12 hexamesters (2 years) to world domination!
print(hexes_to_udaciousness(20000, 2, 7 * 10 ** 9))
#>>> 12

# more friends means faster world domination!
print(hexes_to_udaciousness(15000, 3, 7 * 10 ** 9))
#>>> 10


# U23.4 Quiz: Deep Count
print("# U23.4 Quiz: Deep Count")
# Deep Count

# The built-in len operator outputs the number of top-level elements in a List,
# but not the total number of elements. For this question, your goal is to count
# the total number of elements in a list, including all of the inner lists.

# Define a procedure, deep_count, that takes as input a list, and outputs the
# total number of elements in the list, including all elements in lists that it
# contains.


# For this procedure, you will need a way to test if a value is a list. We have
# provided a procedure, is_list(p) that does this:

def is_list(p):
    return isinstance(p, list)

# It is not necessary to understand how is_list works. It returns True if the
# input is a List, and returns False otherwise.

def deep_count(p):
    sum = 0
    for e in p:
        sum = sum + 1
        if is_list(e):
            sum = sum + deep_count(e)
    return sum

print(deep_count([1, 2, 3]))
#>>> 3
# The empty list still counts as an element of the outer list
print(deep_count([1, [], 3]))
#>>> 3
print(deep_count([1, [1, 2, [3, 4]]]))
#>>> 7
print(deep_count([[[[[[[[1, 2, 3]]]]]]]]))
#>>> 10


# U24.1 Quiz: Family Trees
print("# U24.1 Quiz: Family Trees")
# Single Gold Star

# Family Trees

# In the lecture, we showed a recursive definition for your ancestors. For this
# question, your goal is to define a procedure that finds someone's ancestors,
# given a Dictionary that provides the parent relationships.

# Here's an example of an input Dictionary:

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

# Define a procedure, ancestors(genealogy, person), that takes as its first input
# a Dictionary in the form given above, and as its second input the name of a
# person. It should return a list giving all the known ancestors of the input
# person (this should be the empty list if there are none). The order of the list
# does not matter and duplicates will be ignored.

# moj:
def ancestors(genealogy, person):
    ancestor_list = []
    if person in genealogy:
        for e in genealogy[person]:
            ancestor_list.append(e)
            if e in genealogy:
                ancestor_list.extend(ancestors(genealogy, e))  # isto sto i: ancestor_list = ancestor_list + ancestors(genealogy, e)
    return ancestor_list

# njihov:
def ancestors(genealogy, person):
    if person in genealogy:
        parents = genealogy[person]
        result = parents  # parents are ancestors
        for parent in parents:
            result = result + ancestors(genealogy, parent)  # Add ancestors of parents to result list
        return result
    return []  #no ancestors known

# Here are some examples:

print(ancestors(ada_family, 'Augusta Ada King'))
#>>> ['Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon','Captain John Byron']

print(ancestors(ada_family, 'Judith Blunt-Lytton'))
#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King',
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron']

print(ancestors(ada_family, 'Dave'))
#>>> []


# U24.2 Quiz: Khayyam Triangle
print("# U24.2 Quiz: Khayyam Triangle")
# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

# moj:
def triangle(n):
    output = []
    for i in range(0, n):
        output.append([1])
        while len(output[i]) <= i:
            output[i].append(1)
        if len(output) > 2:
            for e in range(i, len(output)):
                p = 1
                while p < len(output[e]) - 1:
                    output[e][p] = output[e-1][p-1] + output[e - 1][p]
                    p = p + 1
    return output

#njihov:
def make_next_row(row):
    result = []
    prev = 0
    for e in row:
        result.append(e + prev)
        prev = e
    result.append(prev)
    return result

def triangle(n):
    result = []
    current = [1]
    for unused in range(0, n):
        result.append(current)
        current = make_next_row(current)
    return result

# recursive, a student's solution
def triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    result = triangle(n - 1)
    newrow = [1]
    for i in range(0, len(result[-1]) - 1):
        newrow.append(result[-1][i] + result[-1][i + 1])
    newrow.append(1)
    result.append(newrow)
    return result

#For example:
print(triangle(0))
# #>>> []
print(triangle(1))
# #>>> [[1]]
print(triangle(2))
# #>> [[1], [1, 1]]
print(triangle(3))
# #>>> [[1], [1, 1], [1, 2, 1]]
print(triangle(6))
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

def triangular(n):
    return int((n*(n+1))/2)
print(triangular(0))
# #>>> []
print(triangular(1))
# #>>> [[1]]
print(triangular(2))
# #>> [[1], [1, 1]]
print(triangular(3))
# #>>> [[1], [1, 1], [1, 2, 1]]

