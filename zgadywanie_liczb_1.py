from random import randint


def main():
    guessed = False
    number = randint(1, 100)
    while not guessed:
        try:
            guess = round(float(input("Zgadnij liczbę od 1 do 100: \t")))
            if guess < number:
                print("Za mało!")
            elif guess > number:
                print("Za dużo!")
            else:
                guessed = True
                print("Zgadłeś!")

        except ValueError:
            print("To nie jest liczba")
        except UnboundLocalError:
            print("To nie jest liczba")


if __name__ == "__main__":
    main()
