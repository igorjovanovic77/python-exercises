# U27.1 Quiz: Pick One
print("# U27.1 Quiz: Pick One")
# Define a procedure, pick_one, that takes three inputs: a Boolean
# and two other values. If the first input is True, it should return
# the second input. If the first input is False, it should return the
# third input.

# For example, pick_one(True, 37, 'hello') should return 37, and
# pick_one(False, 37, 'hello') should return 'hello'.

# moj:
def pick_one(m, n, p):
    if m == True:
        return n
    else:
        return p

# njihov:
def pick_one(boolean, true_response, false_response):
    if boolean:
        return true_response
    else:
        return false_response

print(pick_one(True, 37, 'hello'))
#>>> 37
print(pick_one(False, 37, 'hello'))
#>>> hello
print(pick_one(True, 'red pill', 'blue pill'))
#>>> red pill
print(pick_one(False, 'sunny', 'rainy'))
#>>> rainy

# U27.2 Quiz: Triangular Numbers
print("# U27.2 Quiz: Triangular Numbers")
# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive
# integer n and returns the nth triangular number.

# moj sa izrazom sa foruma:
def triangular(n):
    return int((n*(n+1))/2)

# njihov:
def triangular(n):
    number = 0
    for i in range(1, n+1):
        number = number + i
    return number
print(triangular(1))
#>>>1
print(triangular(3))
#>>> 6
print(triangular(10))
#>>> 55
