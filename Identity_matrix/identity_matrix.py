# U14.2 Quiz: Recognize Identity Matrix

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
