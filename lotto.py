from random import randint, sample


def lotto():
    typowane = []
    trafienia = 0

    i = 0
    while i < 6:
        try:
            num = int(input("Podaj typowaną liczbę: \t"))

            if num in typowane:                 # czy jest na liście
                raise IndexError
            if num not in range(1, 50):         # czy w zakresie 1-49
                raise ValueError

            typowane.append(num)                # dodaj do typowanych
            i += 1

        except ValueError:
            print("Tylko liczby z zakresu 1-49.")
        except IndexError:
            print("Już podałeś tę liczbę.")

    typowane.sort()
    print("Oto twoje liczby: \t\t" + "".join(str(typowane)))

    wylosowane = sample(range(1, 50), 6)        # losowanie 6 liczb

    for num in typowane:
        if num in wylosowane:
            trafienia += 1

    wylosowane.sort()
    print("Wylosowane numery to: \t" + "".join(str(wylosowane)))
    if trafienia < 3:
        print("Przykro mi, nie wygrałeś.")
    elif trafienia == 3:
        print("Brawo, trafiłeś trójkę!")
    elif trafienia == 4:
        print("Brawo, trafiłeś czwórkę!")
    elif trafienia == 5:
        print("Brawo, trafiłeś piątkę!")
    elif trafienia == 6:
        print("Gratulacje, trafiłeś szóstkę!")

    return


if __name__ == "__main__":
    lotto()
