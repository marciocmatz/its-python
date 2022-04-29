# Sets -> Conjuntos

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

s3 = s1.union(s2)  # {1, 2, 3, 4, 5, 6, 7}
s3 = s1.intersection(s2)  # {3, 4, 5}
s3 = s1.difference(s2)  # {1, 2}

print(s3)