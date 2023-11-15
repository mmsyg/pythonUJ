
def ruler(length):

    line = "|"
    numbers = "0"

    for i in range(1, n+1):
        line += '....|'
        numbers += f'{i:5}'
    final = line + '\n' + numbers
    print(final)

n = 11
ruler(n);