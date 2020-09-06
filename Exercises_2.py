# U11.3 Quiz: Days in a Month
print("# U11.3 Quiz: Days in a Month")

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def how_many_days(month):
    return days_in_month[month-1]

print(how_many_days(1))
print(how_many_days(9))

# U11.4 Quiz: Nested List
print("# U11.4 Quiz: Nested List")

beatles = [['John', 1940], ['Paul', 1942],
           ['George', 1943], ['Ringo', 1940]]

print(beatles[3])
print(beatles[3][0])

# U11.5 Quiz: Relative Size
print("# U11.5 Quiz: Relative Size")
# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

#             Name      Capital  Populations (millions)
countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1210],
             ['Romania', 'Bucharest', 21],
             ['United States', 'Washington', 307]]

print(countries[0][2]/countries[2][2])

# U11.9 Quiz: Different Stooges(Mutation)
print("# U11.9 Quiz: Different Stooges(Mutation)")

stooges = ['Moe','Larry','Curly']
stooges[2]='Shemp'

print(stooges)

# U11.10 Quiz: Yello Mutation + Aliasing
print("# U11.10 Quiz: Yello Mutation + Aliasing")

p = ['H', 'e', 'l', 'l', 'o']
q = p
p[0] = 'Y'
print(p, q)

p = [0, 0, 7]
print(p, q)

# U11.12 Quiz: Secret Agent Man
print("# U11.12 Quiz: Secret Agent Man")

spy = [0, 0, 7]
agent = spy
spy[2] = agent[2] + 1
print(agent, spy)

# U11.13 Quiz: replace Spy
print("# U11.13 Quiz: replace Spy")
spy = [0,0,7]
def replace_spy(p):
    p[2] += 1

replace_spy(spy)
print(spy)

# U11.16 Quiz: Len Quiz
print("# U11.16 Quiz: Len Quiz")

p = [1, 2]
p.append(3)
p = p + [4, 5]
print(len(p))

# U11.17 Quiz: Append Quiz
print("# U11.17 Quiz: Append Quiz")

p = [1, 2]
q = [3,4]
p.append(q)
print(p)
print(len(p))
q[1] = 5
print(p)
print(len(p))

# U11.22 Quiz: Loops on Lists
print("# U11.22 Quiz: Loops on Lists")

def print_all_elements(p):
    i=0
    while i < len(p):
        print(p[i])
        i = i + 1

panini_albums = [1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
print(print_all_elements(panini_albums))

# U11.23 Quiz: For Loops
print("# U11.23 Quiz: Loops on Lists")

def print_all_elements(p):
    for e in p:
        print(e)

mylist = [1, 2, [3, 4]]
print_all_elements(mylist)

# U11.24 Quiz: Sum List
print("# U11.24 Quiz: Sum List")

# for loop
def sum_list(p):
    result = 0
    for e in p:
        result = result + e
    return result

# while loop
def sum_list(p):
    i = 0
    result = 0
    while i < len(p):
        result = result + p[i]
        i = i+1
    return result

print(sum_list([1, 7, 4]))
print(sum_list([9, 4, 10]))
print(sum_list([44, 14, 76]))

# U11.25 Quiz: Measure Udacity
print("# U11.25 Quiz: Measure Udacity")

def measure_udacity(U):
    count = 0
    for e in U:
        if e[0] == 'U':
            count +=1
    return count


print(measure_udacity(['Dave','Sebastian','Katy']))
print(measure_udacity(['Umika','Umberto']))


# U11.26 Quiz: Find Element + U11.27 Quiz: Index
print("# U11.26 Quiz: Find element + U11.27 Quiz: Index")

# for loop(moj)
def find_element(p, f):
    count = 0
    for e in p:
        if f not in p:
            return -1
        count+=1
        if e == f:
            break
    return count-1

# for loop (njihov)
def find_element(p, t):
    i = 0
    for e in p:
        if e == t:
            return i
        i = i +1
    return -1

# while loop (njihov)
def find_element(p, f):
    i = 0
    while i < len(p):
        if p[i] == f:
            return i
        i = i +1
    return -1

# using index operator (moj)
def find_element(p,t):
    if t not in p:
        return -1
    return p.index(t)

# using index operator (njihov)
def find_element(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1

print(find_element([1,2,3],3))
print(find_element(['alpha','beta'],'gamma'))


# U11.29 Quiz: Union
print("# U11.29 Quiz: Union")

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)
    return a

a = [1,2,3]
b = [2,4,6]
print(union(a,b))

# U11.30 pop
print("# U11.30 pop")

a = [1, 2, 3]
b = a
x = a.pop()
print(a, b, x)

# U12.2 Quiz: Mutating Lists
print("# U12.2 Mutating Lists")

def proc1(p):
    p[0] = p[1]
    return p

def proc2(p): # it creates a new list because you concatenate list p with list [1] and get new list
    p = p + [1]
    return p

def proc3(p):
    q = p
    p.append(4)
    q.pop()
    return p
def proc4(p):
    q = []
    while p: # while p is not empty
        q.append(p.pop())
    while q:
        p.append(q.pop())
    return p

q = [2, 3, 4, 5]
print(proc1(q))
r = [2, 3, 4, 5]
print(proc2(r))
s = [2, 3, 4, 5]
print(proc3(s))
t = [2, 3, 4, 5]
print(proc4(t))

# U12.3 Quiz: Product List
print("# U12.3 Product List")

def product_list(list_of_numbers):
    result = 1
    for e in list_of_numbers:
        result = result *e
    return result

print(product_list([9]))
print(product_list([1,2,3,4]))
print(product_list([]))

# U12.4 Quiz: Greatest
print("# U12.4 Greatest")

#moj
def greatest(list_of_numbers):
    while list_of_numbers:
        return max(list_of_numbers)
    return 0

#njihov
def greatest(p):
    big = 0
    for i in p:
        if i > big:
            big = i
    return big

print(greatest([4,23,1]))
print(greatest([]))

# U12.5 Quiz: Lists of Lists
print("# U12.5 Lists of Lists")
# moj
def total_enrollment(unis):
    s = 0
    f = 0
    for e in unis:
        s = s + e[1]
        f = f + e[1]*e[2]
    return s, f

#njihov
def total_enrollment(p):
    total_students = 0
    total_tuition = 0
    for name, students, price in p: # for each value in the list you have the name which corresponds to each entry in the sublist
        total_students = total_students + students
        total_tuition = total_tuition + students*price
    return total_students, total_tuition

udacious_univs = [['Udacity',90000,0]]
usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

print(total_enrollment(udacious_univs))
print(total_enrollment(usa_univs))
print(len(usa_univs))

# U12.8 Quiz: Sudoku
print("# U12.8 Quiz: Sudoku")

# moj:
def check_sudoku(p):
    for e in p:
        for n in e:
            if n == str(n) or n != int(n) or n > len(e) or n <= 0:
                return False
            k = 0
            _i = e.index(n)
            while k < len(e):
                if k == _i:
                    k = k + 1
                    continue
                # if index for n == k: continue
                if n == e[k]:
                    return False
                k = k + 1
    j = 0
    l = []
    while j < len(p):
        for e in p:
            if e[j] not in l:
                l.append(e[j])
            else:
                return False
        j = j + 1
        l = []
    return True

#njihov
def check_sudoku(p):
    n = len(p)  # Extract size of grid
    digit = 1  # start with 1
    while digit <= n:  #Go through each digit
        i = 0
        while i < n:  # go through each row and column
            row_count = 0
            col_count = 0
            j = 0
            while j < n:  # for each entry in its row/column
                if p[i][j] == digit:  # check row count
                    row_count = row_count + 1
                if p[j][i] == digit:
                    col_count = col_count + 1
                j = j + 1
            if row_count != 1 or col_count != 1:
                return False
            i = i + 1 #next row/column
        digit = digit + 1  #next digit
    return True  # nothing was wrong!

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

print(check_sudoku(incorrect))
print(check_sudoku(correct))
print(check_sudoku(incorrect2))
print(check_sudoku(incorrect3))
print(check_sudoku(incorrect4))
print(check_sudoku(incorrect5))


# U13.2 Quiz: Symmetric Square
print("# U13.2 Quiz: Symmetric Square")
def symmetric(p):
    j = 0
    k = 0
    l = []
    while j < len(p):
        for e in p:
            l.append(e[j])
        if not p[k] == l:
            return False
        j = j + 1
        k = k + 1
        l = []
    return True


print(symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]]))
print(symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "fish"],
               ["fish", "fish", "cat"]]))
print(symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "dog"],
               ["fish","fish","cat"]]))
print(symmetric([[1, 2],
               [2, 1]]))
print(symmetric([[1, 2, 3, 4],
               [2, 3, 4, 5],
               [3, 4, 5, 6]]))
print(symmetric([[1,2,3],
                [2,3,1]]))


# U13.3 Quiz: Mean of a list
print("# U13.3 Quiz: Mean of a list")
def list_mean(p):
    sum = 0
    for e in p:
        sum = sum + e
    return sum / len(p)

print(list_mean([1,2,3,4]))
#>>> 2.5
print(list_mean([1,3,4,5,2]))
#>>> 3.0


# U14.1 Quiz: Antisymmetric Square
print("# U14.1 Quiz: Antisymmetric Square")
def antisymmetric(p):
    for e in p:
        if len(p) != len(e):
            return False
    j = 0
    m = []
    while j < len(p):
        for e in p:
            m.append(e[j])
        if not p[j][j] == 0 and m[j] == 0:
            return False
        s = 0
        while s < len(p):
            if not p[j][s] + m[s] == 0:
                return False
            s = s + 1
        j = j + 1
        m = []
    return True

print(antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]]))
# True
print(antisymmetric([[0, 4, 1],
                     [-4, 0, 0],
                     [-1, 0, 0]]))
# True

print(antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]]))
# False

print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
# False

# U14.2 Quiz: Recognize Identity Matrix
print("# U14.2 Quiz: Recognize Identity Matrix")

def is_identity_matrix(p):
    j = 0
    m = []
    while j < len(p):
        for e in p:
            m.append(e[j])
        if p[j][j] != 1 or m[j] != 1 or p[j] != m:
            return False
        k = 0
        _i = p[j].index(1)
        while k < len(m):
            if k == _i:
                k = k + 1
                continue
            if m[k] != 0:
                return False
            k = k + 1
        j = j + 1
        m = []
    return True

# Test Cases:
matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print(is_identity_matrix(matrix1))
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print(is_identity_matrix(matrix2))
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print(is_identity_matrix(matrix3))
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print(is_identity_matrix(matrix4))
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print(is_identity_matrix(matrix5))
#>>>False

matrix6 = [[1,0,0,0],
           [0,1,0,1],
           [0,0,1,0],
           [0,0,0,1]]

print(is_identity_matrix(matrix6))
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print(is_identity_matrix(matrix7))
#>>>False

# U14.3 Quiz: Numbers in lists
print("# U14.3 Quiz: Numbers in lists")

def numbers_in_lists(string):
    n = 0
    list = []
    sublist = []
    for e in string:
        e = int(e)
        list.append(e)
        if len(list) == 1:
            continue
        if e <= list[n]:
            sublist.append(list.pop())
        else:
            n = n + 1
            if sublist != []:
                y = list.pop()
                list.append(sublist)
                sublist = []
                list.append(y)
                n = n + 1
            continue
    if sublist != []:
        list.append(sublist)
    return list

#testcases
string = '543987'
#result = [5,[4,3],9,[8,7]]
print(numbers_in_lists(string))
string1 = '987654321'
#result = [9,[8,7,6,5,4,3,2,1]]
print(numbers_in_lists(string1))
string2 = '455532123266'
#result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print(numbers_in_lists(string2))
string3 = '123456789'
#result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers_in_lists(string3))

# U14.4 Quiz: Frequency Analysis
print("# U14.4 Quiz: Frequency Analysis")

def freq_analysis(message):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    freq_list = []
    for m in abc:
        freq_list.append(0.0)
    for e in message:
        p = abc.find(e)
        if freq_list[p] == 0.0:
            freq_list[p] = 1 / len(message)
        else:
            freq_list[p] = freq_list[p] + 1 / len(message)
    return freq_list

#Tests

print(freq_analysis("abcd"))
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]
print(freq_analysis("adca"))
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]
print(freq_analysis('bewarethebunnies'))
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]

