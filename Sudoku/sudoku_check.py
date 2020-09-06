# U12.8 Quiz: Sudoku

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
                    continue  # if index for n == k: continue
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
