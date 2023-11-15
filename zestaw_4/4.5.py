def reverse_list(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

list = [1, 2, 3, 4, 5, 6]
reverse_list(list, 0, 5)
print('Odwrócona lista:' , list)
