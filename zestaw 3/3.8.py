sequence1 = ['a', 2, 3, 4, 5]
sequence2 = [3, 3, 4, 'a', 7, 7, 'h']

common_elements = list(set(sequence1) & set(sequence2))
all_elements = list(set(sequence1) | set(sequence2))

print("Wspólne elementy:", common_elements)
print("Wszystkie elementy:", all_elements)
