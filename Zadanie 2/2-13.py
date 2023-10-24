lines ="Litwo! Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie."

words = lines.split()
lengths = []

for word in words:
    lengths.append(len(word))

totalLength = sum(lengths)
print("Łączna długość wyrazów:", totalLength)
