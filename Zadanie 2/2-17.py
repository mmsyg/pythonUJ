lines ="Litwo! Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie."

words = lines.split()

sortedWordsAlphabet = sorted(words, key=str.lower)
sortedWordsLength = sorted(words, key=len)
print(sortedWordsAlphabet)
print(sortedWordsLength)