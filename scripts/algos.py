"""Reference implementations (course version) used to generate AND to verify slide examples."""
import math

def binary_search_trace(a, x):
    """Course pseudo-code (ch2 p.24). Returns list of (i, m, j, a_j) steps and the result index (0 = fail)."""
    i, m, steps = 1, len(a), []
    while i <= m:
        j = (i + m) // 2
        steps.append({"i": i, "m": m, "j": j, "aj": a[j - 1]})
        if x == a[j - 1]:
            return steps, j
        if x < a[j - 1]: m = j - 1
        else: i = j + 1
    return steps, 0

def max_comparisons(n):
    return math.floor(math.log2(n)) + 1

def insertion_trace(a):
    a, rows = list(a), []
    for j in range(1, len(a)):
        temp, i = a[j], j - 1
        while i >= 0 and temp < a[i]:
            a[i + 1] = a[i]; i -= 1
        a[i + 1] = temp
        rows.append(list(a))
    return rows

def selection_trace(a):
    a, rows = list(a), []
    for j in range(len(a) - 1):
        f = j
        for k in range(j + 1, len(a)):
            if a[k] < a[f]: f = k
        a[j], a[f] = a[f], a[j]
        rows.append(list(a))
    return rows

def selection_comparisons(n):
    return n * (n - 1) // 2
