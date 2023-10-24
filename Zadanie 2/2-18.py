number = 9000123472942301032340243842042340100

word = str(number)
counter =0

for letter in word:
    if letter == "0":
        counter += 1

print("W tej liczbie 0 wystepuje:", counter, "razy")