import numpy

neighbor =  [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
             [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
             [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]
transfer = numpy.zeros((9, 9))
for k in range(9):
    for neigh in range(4): transfer[neighbor[k][neigh], k] += 0.25
    #0.25-to chyba prawdopodobienstwo
    #neigbor[k]-ktoras z tablic, [neigh]-k-ty elemnt tablicy jako elementu macierzy
position = numpy.zeros(9)
#tworzy tablice z dziewieczioma 0
position[8] = 1.0
#Obecnie znajduje sie na pozycji 8-prawy gorny rog
#dla czasu od 0 do 100, czyli moze wykonac 100 roznych ruchow
for t in range(100):
    print t,'  ',["%0.5f" % abs(i- 1.0 / 9.0) for i in position]
    print i
    position = numpy.dot(transfer, position)
    print position