def zgadywanie2():
    print("Pomyśl o liczbie od 0 do 1000, a ja ją zgadnę w 10-ciu próbach.")
    min = 0
    max = 1000
    guessed = False
    yes = ["tak", "t", "yes", "y"]
    no = ["nie", "n", "no"]
    i = 0

    while i < 10 and not guessed:
        guess = int((max - min) / 2) + min
        print("Próba {}".format((i + 1)))
        print("Zgaduję: " + str(guess))

        answer = input("Zgadłem? t/n\t").lower()

        if answer in yes:
            print("Wygrałem!")
            guessed = True
        elif answer in no:
            answer = input("Za dużo? t/n\t").lower()
            if answer in yes:
                max = guess
            elif answer in no:
                answer = input("Za mało? t/n\t").lower()
                if answer in yes:
                    min = guess
                elif answer in no:
                    print("Nie oszukuj!")
                    i -= 1      # cofam licznik pętli
                else:
                    print("Odpowiedz 'tak' lub 'nie'")
                    i -= 1      # cofam licznik pętli
            else:
                print("Odpowiedz 'tak' lub 'nie'")
                i -= 1          # cofam licznik pętli
        else:
            print("Odpowiedz 'tak' lub 'nie'")
            i -= 1              # cofam licznik pętli

        i += 1

    if i == 10:
        print("Przegrałem :(")

    return


if __name__ == "__main__":
    zgadywanie2()
