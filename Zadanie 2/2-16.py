lines = "Wczoraj GvR zjadł zupę"

words = lines.split()
maxWord =""
shortCut = "GvR"
newWord = "Guido van Rossum"
newSentence =[]

for word in words:
    if word==shortCut:
        word = newWord
    newSentence.append(word)
finalSentence =" ".join(newSentence)
print(finalSentence)