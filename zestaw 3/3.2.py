
#1 funkcja list.sort() wykonuje sortowanie na liście i nie zwraca nowej listy,
# dlatego przypisanie wyniku sortowania do zmiennej L spowoduje, że L zwróci 'None
#poprawna wersja:
L = [3, 5, 4]
L.sort()


#2 nie można przypisać 3 wartości dwum zmiennym, poprawny sposob:
x, y, z = 1, 2, 3

#3 wartości krotki nie można zmienić po przypisaniu, w ten sposób
X = 1, 4, 3

#4 nie ma indeksu 3 w tej tablicy, indeksowanie zaczyna się od 0
X = [1, 2, 3]
X[2] = 4

#5 metoda append nie jest dostepna dla ciągu znaków
X = "abc"
X += "d"

#6 funkcja pow potrzebuje dwóch argumentó, brakuje jednego nawiasa
L = list(map(lambda x: pow(x, 2), range(8)))