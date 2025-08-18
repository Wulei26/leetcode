A = [1, 3, 5, 7, 9, 11, 13]
B = [1, 2, 3, 5, 7, 13, 15]
p = 0
q = 0
for x in A:
    p = p | 1 << x
for y in B:
    q = q | 1 << y
print((p & q).bit_count())
