from fuzzy_relations import *
A = {"x": 0.7, "y": 0.4}
B = {"m": 0.5, "n": 0.8}
C = {"p": 0.6, "q": 0.3}
R1 = cartesian_product(A, B)
R2 = cartesian_product(B, C)
print("Fuzzy Relation R1 (A x B):")
for k, v in R1.items():
    print(f"{k}: {v}")
print("\nFuzzy Relation R2 (B x C):")
for k, v in R2.items():
    print(f"{k}: {v}")
print("\nMax-Min Composition (R1 o R2):")
R3 = max_min_composition(R1, R2)
for k, v in R3.items():
    print(f"{k}: {v}")
