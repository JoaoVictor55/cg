alfabeto = ('A','B','C','D','E','F','G','H','I','J','K','L')


points = ((0, -1, -1.618),
(0, -1, 1.618),
(0, 1, -1.618),
(0, 1, 1.618),
(-1, -1.618, 0),
(-1, 1.618, 0),
(1, -1.618, 0),
(1, 1.618, 0),
(-1, 0, -1.618),
(-1, 0, 1.618),
(1, 0, -1.618),
(1, 0, 1.618))

#print(points)

coord = dict(zip(alfabeto, points))

#print(coord['B'],coord['G'],coord['L'],sep=" ",end="\n")
print(alfabeto.index("C"),alfabeto.index('J'),alfabeto.index('A'),sep=" ",end="\n")
