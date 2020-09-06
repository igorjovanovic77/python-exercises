# U18.18 Quiz: Bad Hash
print("# U18.18 Quiz: Bad Hash")

def bad_hash_string(keyword, buckets):
    return ord(keyword[0]) % buckets

print(bad_hash_string('udacity', 21))
print(bad_hash_string('udac', 21))
print(bad_hash_string('kudacity', 21))
print(bad_hash_string('dudity', 21))
print(bad_hash_string('audacity', 21))
print(bad_hash_string('uber', 21))


# U18.19 Quiz: Better Hash Functions
print("# U18.19 Quiz: Better Hash Functions")

def hash_string(keyword, buckets):
    result = 0
    for c in keyword:
        result += (ord(c))
    return result % buckets

# njihov:
def hash_string(keyword, buckets):
    h = 0
    for c in keyword:
        h = (h + ord(c)) % buckets  # mislio da je ovaj brzi ali moj je brzi
    return h

print(hash_string('a',12))
#>>> 1
print(hash_string('b',12))
#>>> 2
print(hash_string('a',13))
#>>> 6
print(hash_string('au',12))
#>>> 10
print(hash_string('udacity',12))
#>>> 11


# exercise
# def symbolz(num):
#     list = []
#     while num >= 0:
#         list.append(chr(num))
#         num -= 1
#     return list
#
# broj = 255
# print(symbolz(broj))


# U18.23 Quiz: Empty Hashtable
print("# U18.23 Quiz: Empty Hashtable")

# moj
def make_hashtable(nbuckets):
    index = []
    while nbuckets > 0:
        index.append([])
        nbuckets -= 1
    return index

#njihov:
def make_hashtable(nbuckets):
    i = 0
    table = []
    while i < nbuckets:
        table.append([])
        i = i + 1
    return table

# for loop + range:
def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table

print(make_hashtable(5))
print(make_hashtable(1))
print(make_hashtable(0))

# # * on lists: not working properly
# def make_hashtable_NOT(nbuckets):
#     return [[]] * nbuckets
#
# print(make_hashtable_NOT(5))
# print(make_hashtable_NOT(3))
# print(make_hashtable_NOT(0))
#
# table = make_hashtable_NOT(3)
# table[1].append(['udacity', ['http://udacity.com']])
# print(table)

# U18.25 Quiz: Finding Buckets
print("# U18.25 Quiz: Finding Buckets")

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print(hashtable_get_bucket(table, "Zoe"))
#>>> [['Bill', 17], ['Zoe', 14]]
print(hashtable_get_bucket(table, "Brick"))
#>>> []
print(hashtable_get_bucket(table, "Lilith"))
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]


# U18.26 Quiz: Adding Keywords
print("# U18.26 Quiz: Adding Keywords")

def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable, key).append([key, value])
    return htable

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print(table)
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]


# U18.27 Quiz: Lookup
print("# U18.27 Quiz: Lookup")

def hashtable_lookup(htable,key):
    for e in hashtable_get_bucket(htable, key):
        if e[0] == key:
            return e[1]
    return None

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]
print(hashtable_lookup(table, 'Francis'))
#>>> 13
print(hashtable_lookup(table, 'Louis'))
#>>> 29
print(hashtable_lookup(table, 'Zoe'))
#>>> 14

# U18.28 Quiz: Update
print("# U18.28 Quiz: Update")

def hashtable_update(htable,key,value):
    p = hashtable_get_bucket(htable, key)
    for e in p:
        if e[0] == key:
            e[1] = value
            return
    p.append([key, value])
    return htable

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print(table)
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42],
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2],
#>>> ['Rochelle', 94]]]


# U18.31 Quiz: Population
print("# U18.31 Quiz: Population")

population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print(population)

# or:
population = {}
population['Shanghai'] = 17.8
population['Istanbul'] = 13.3
population['Karachi'] = 13.0
population['Mumbai'] = 12.5
population['Charlottesville'] = 0.043
print(population['Shanghai'])


# U18.32 Quiz: Noble Gas
print("# U18.32 Quiz: Noble Gas")

elements = {}  # empty dictionary
elements['H'] = {'name': 'Hydrogen', 'number': 1, 'weight': 1.00794}  # value of the element is a dictionary
elements['He'] = {'name': 'Helium', 'number': 2, 'weight': 4.002602, 'noble gas': True}  # value of the element is a dictionary
print(elements)
print(elements['H'])
print(elements['H']['name'])
print(elements['He']['weight'])
print(elements['He']['noble gas'])
# print(elements['H']['noble gas'])  # it will return error because that key not exist


# U19.1 Quiz: Growth
print("# U19.1 Growth")

def sum_list(p):  # it scales linearly with the number of items in the list p
    sum = 0
    for e in p:
        sum = sum + e
    return sum

def has_duplicate_element(p):
   res = []
   for i in range(0, len(p)):
       for j in range(0, len(p)):
           if i != j and p[i] == p[j]:
               return True
   return False

def mystery(p):
   i = 0
   while True:  # we will continue this while loop until i >= len(p)
       if i >= len(p):
           break
       if p[i] % 2:  # it means if p[i] % 2 != 0, meaning if p[i] is odd number than continue with the block code
           i = i + 2
       else:
           i = i + 1
   return i

p = [1, 2, 3]
print(sum_list(p))
print(has_duplicate_element(p))
print(mystery(p))


# U19.3 Quiz: Is Offered
print("# U19.3 Is Offered")

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253':
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262':
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }
# moj:
def is_offered(courses, course, hexamester):
    if course in courses[hexamester]:
        return True
    return False

#njihov:
def is_offered(courses, course, hexamester):
    return course in courses[hexamester]

print(is_offered(courses, 'cs101', 'apr2012'))
#>>> True
print(is_offered(courses, 'cs003', 'apr2012'))
#>>> False
print(is_offered(courses, 'cs001', 'jan2044'))
#>>> True
print(is_offered(courses, 'cs253', 'feb2012'))
#>>> False


# U19.4 Quiz: When Offered
print("# U19.4 Quiz: When Offered")

def when_offered(courses,course):
    offered = []
    for hexamester in courses:
        if course in courses[hexamester]:
            offered.append(hexamester)
    return offered

print(when_offered (courses, 'cs101'))
#>>> ['apr2012', 'feb2012']
print(when_offered(courses, 'bio893'))
#>>> []


# U19.5 Quiz: Involved
print("# U19.5 Quiz: Involved")

# moj:
def involved(courses, person):
    teaches = {}
    for hexamester in courses:
        for course in courses[hexamester]:
            p = courses[hexamester][course]
            if p['teacher'] == person or 'assistant' in p and p['assistant'] == person:
                if hexamester in teaches:
                    teaches[hexamester].append(course)
                else:
                    teaches[hexamester] = [course]
    return teaches

#njihov:
def involved(courses, person):
    output = {}
    for hexamester in courses:
        for course in courses[hexamester]:
            for key in courses[hexamester][course]:
                if courses[hexamester][course][key] == person:
                    if hexamester in output:
                        output[hexamester].append(course)
                    else:
                        output[hexamester] = [course]
    return output

print(involved(courses, 'Dave'))
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}
print(involved(courses, 'Peter C.'))
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}
print(involved(courses, 'Dorina'))
#>>> {'jan2044': ['cs001']}
print(involved(courses,'Peter'))
#>>> {}
print(involved(courses,'Robotic'))
#>>> {}
print(involved(courses, ''))
#>>> {}


# U19.6 Quiz: Refactoring
print("# U19.6 Quiz: Refactoring")

def bucket_find(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_find(bucket, key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])
    return htable

def hashtable_lookup(htable, key):
    entry = bucket_find(hashtable_get_bucket(htable, key), key)
    if entry:
        return entry[1]
    else:
        return None

table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print(hashtable_lookup(table, 'Python'))
#>>> Guido van Rossum


# U19.7 Quiz: Memoization
print("# U19.7 Quiz: Memoization")

def cached_execution(cache, proc, proc_input):
    # format of cache { proc_input1:proc_output1, proc_input2:proc_output2, ...}
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]


# Here is an example showing the desired behavior of cached_execution:

def factorial(n):
    print("Running factorial")
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

cache = {} # start cache as an empty dictionary
### first execution (should print out Running factorial and the result)
print(cached_execution(cache, factorial, 50))

print("Second time:")
### second execution (should only print out the result)
print(cached_execution(cache, factorial, 50))


def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return (cached_execution(cache, cached_fibo, n - 1)
                + cached_execution(cache, cached_fibo, n - 2))


cache = {}  # new cache for this procedure
# do not try this at home...at least without a cache!
print(cached_execution(cache, cached_fibo, 100))


# U20.1 Quiz: Shift a Letter
print("# U20.1 Quiz: Shift a Letter")

# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

# moj:
def shift(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyza'
    return alphabet[alphabet.find(letter) + 1]


# sa foruma:
def shift(letter):
    if letter is 'z':
        return 'a'
    else:
        return chr(ord(letter)+1)


print(shift('a'))
#>>> b
print(shift('n'))
#>>> o
print(shift('z'))
#>>> a


# U20.2 Quiz: Shift n Letters
print("# U20.2 Quiz: Shift n Letters")

# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

# moj:
def shift_n_letters(letter, n):
    return chr(97 + (((ord(letter) + n) - 97) % 26))

# forum:
def shift_n_letters(letter, n):
    return chr(ord('a') + (((ord(letter) + n) - ord('a')) % 26))


print(shift_n_letters('s', 1))
#>>> t
print(shift_n_letters('s', 2))
#>>> u
print(shift_n_letters('s', 10))
#>>> c
print(shift_n_letters('s', -10))
#>>> i
print(shift_n_letters('a', -1))
#>>> z


# U20.3 Quiz: Rotate
print("# U20.3 Quiz: Rotate")


# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string, n):
    result = ''
    for e in string:
        if e == ' ':
            result += ' '
        else:
            result += shift_n_letters(e, n)
    return result


print(rotate ('sarah', 13))
#>>> 'fnenu'
print(rotate('fnenu',13))
#>>> 'sarah'
print(rotate('dave',5))
#>>>'ifaj'
print(rotate('ifaj',-5))
#>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
#>>> ???
