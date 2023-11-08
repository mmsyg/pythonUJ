
end = 'To niejest liczba rzeczywista!'
while end !='stop':
    try:
        word = input('podaj liczbe rzeczywista, wpisz "stop" aby zakończyć:')

        word_1 = float(word)
        print(word_1)
    except ValueError:
        if word == 'stop':
            end =word
        print(end)


