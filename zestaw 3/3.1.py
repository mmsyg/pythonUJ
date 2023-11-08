# 1 poprawny składniowo, ale niepotrzebne średniki:
x = 2
y = 1
if x > y:
    result = x
else:
    result = y

print(result)

# 2 składniowo powinno być "wcięcie" dla elementów należących dla for i if, warunek if nie może być umieszczony bezpośrednio w pętli for w ten sposób

for i in "axby":
    if ord(i) < 100:
        print(i)

# 3kod jest poprawny składniowo, lecz bardziej czytelnie, byłoby w ten sposób:

for i in "axby":
    print(ord(i) if ord(i) < 100 else i)
