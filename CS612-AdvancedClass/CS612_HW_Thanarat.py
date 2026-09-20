# 1. Modulo Exponentiation

def mod_expo(a, n, k):
    """คำนวณ (a ** n) % k ด้วย divide & conquer เป้น O(log n)"""
    if n == 1:
        return a % k

    if n % 2 == 0:                       # n เป็นเลขคู่
        tmp = mod_expo(a, n // 2, k)
        return (tmp * tmp) % k
    else:                                # n เป็นเลขคี่
        tmp = mod_expo(a, n // 2, k)     # หารปัดลง
        tmp = (tmp * tmp) % k
        return (tmp * (a % k)) % k

# 2. Maximum Subarray แบบใช้ Devide & Conquer
def build_prefix(A):
    S = [0] * len(A)
    for i in range(1, len(A)):
        S[i] = S[i - 1] + A[i]
    return S


def get_sum(S, a, b):
    return S[b] - S[a - 1]


def better(x, y):
    if x[0] != y[0]:
        return x if x[0] > y[0] else y
    return x if (x[1], x[2]) <= (y[1], y[2]) else y


def mss(A, start, stop, S):
    if start == stop:
        return (A[start], start, start)

    m = (start + stop) // 2

    r1 = mss(A, start, m, S)
    r2 = mss(A, m + 1, stop, S)

    max_sum_left, best_i = get_sum(S, m, m), m
    for i in range(start, m):
        s = get_sum(S, i, m)
        if s > max_sum_left or (s == max_sum_left and i < best_i):
            max_sum_left, best_i = s, i

    max_sum_right, best_j = get_sum(S, m + 1, m + 1), m + 1
    for j in range(m + 2, stop + 1):
        s = get_sum(S, m + 1, j)
        if s > max_sum_right:
            max_sum_right, best_j = s, j

    r3 = (max_sum_left + max_sum_right, best_i, best_j)

    return better(better(r1, r2), r3)


def max_subarray(arr):
    A = [None] + list(arr)
    S = build_prefix(A)
    total, a, b = mss(A, 1, len(arr), S)
    return a, b

#เทส
''''
A = [2, 3, -6, 4, -2, 3, -5, -4, 8] 
start, stop = max_subarray(A)
print(start, "and", stop)
'''

# 3. Celebrity Problem
def celeb(B, start, stop, n):
    if start == stop:
        for j in range(1, n + 1):
            if B[start][j]:                        # start รู้จักคนอื่น -> ไม่ใช่คนดัง
                return -1
            if j != start and not B[j][start]:     # มีคนไม่รู้จัก start -> ไม่ใช่คนดัง
                return -1
        return start

    if B[start][stop]:
        return celeb(B, start + 1, stop, n)
    else:
        return celeb(B, start, stop - 1, n)


def find_celebrity(knows):
    n = len(knows)
    B = [[False] * (n + 1)]          
    for row in knows:
        B.append([False] + list(row))
    return celeb(B, 1, n, n)


#เทส
'''
knows = [
        [0, 1, 1, 0],      # คนที่ 1 รู้จัก 2, 3
        [0, 0, 1, 1],      # คนที่ 2 รู้จัก 3, 4
        [0, 0, 0, 0],      # คนที่ 3 ไม่รู้จักใคร
        [0, 1, 1, 0],      # คนที่ 4 รู้จัก 2, 3
    ]
print(find_celebrity(knows)) 
'''    