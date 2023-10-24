numbers = [1, 23, 456, 77, 9, 123]

lines = ""

for n in numbers:
    line_numbers = str(n)
    block = line_numbers.zfill(3)
    lines += block + " "

print(lines)