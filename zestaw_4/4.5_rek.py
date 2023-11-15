def reverse_list_rec(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_list_rec(L, left + 1, right - 1)

list = [1, 2, 3, 4, 5]
reverse_list_rec(list, 0, 4)
print('Odwrócona lista: ',list)
