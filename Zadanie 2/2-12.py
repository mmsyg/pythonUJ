lines ="Litwo! Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie."

words = lines.split()

firstLetters =""
lastLetters =""
for word in words:
    firstLetters += word[0]
    lastLetters += word[len(word) - 1]
print(firstLetters)
print(lastLetters)