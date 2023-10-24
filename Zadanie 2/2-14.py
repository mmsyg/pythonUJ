lines ="Litwo! Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie."

words = lines.split()
max = 0
maxWord =""

for word in words:
    if len(word)>max:
        max=len(word)
        maxWord=word


print("Najdłuższe słowo to:", maxWord,max)
