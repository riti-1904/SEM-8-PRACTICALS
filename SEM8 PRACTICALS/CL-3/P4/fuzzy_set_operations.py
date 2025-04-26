# fuzzy_set_operations.py

def fuzzy_union(A, B):
    return {key: max(A.get(key, 0), B.get(key, 0)) for key in A}

def fuzzy_intersection(A, B):
    return {key: min(A.get(key, 0), B.get(key, 0)) for key in A}

def fuzzy_complement(A):
    return {key: 1 - val for key, val in A.items()}

def fuzzy_difference(A, B):
    return {key: min(A.get(key, 0), 1 - B.get(key, 0)) for key in A}
