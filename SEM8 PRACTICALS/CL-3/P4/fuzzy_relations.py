def cartesian_product(A, B):
    relation = dict()
    for a_key, a_val in A.items():
        for b_key, b_val in B.items():
            relation[(a_key, b_key)] = min(a_val, b_val)
    return relation

def max_min_composition(R1, R2):
    result = dict()
    for (a, b1), val1 in R1.items():
        for (b2, c), val2 in R2.items():
            if b1 == b2:
                key = (a, c)
                min_val = min(val1, val2)
                if key in result:
                    result[key] = max(result[key], min_val)
                else:
                    result[key] = min_val
    return result
