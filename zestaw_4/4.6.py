def sum_sequence(s):
    total = 0
    for item in s:
        if isinstance(item, (list, tuple)):
            total += sum_sequence(item)
        else:
            total += item
    return total

sequence = [6,[3, 4],  28, (5, [6, 1])]
print('suma w sekwencji:', sum_sequence(sequence))
