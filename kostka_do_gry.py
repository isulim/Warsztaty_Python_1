from random import randint

class WrongDiceError(Exception):
    pass

def rpg_dice(dice):
    throw = 0
    dices = [3, 4, 6, 8, 10, 12, 20, 100]
    try:
        dice = dice.replace(" ", "")    # usuń spacje
        dice = dice.upper()

        # ustawianie wartości x
        if dice[0] == 'D':
            x = 1               # jeżeli na początku jest tylko D, x = 1
            dice = dice[1:]

        else:
            dice = dice.split("D")  # podziel względem D
            x = int(dice[0])        # ustaw x na pierwszy element
            dice = dice[1]          # zostaw resztę jako dice

        # ustawianie wartości y oraz z
        if '+' in dice:             # jeśli w dice jest plus
            dice = dice.split("+")  # podziel względem plusa
            y = int(dice[0])        # ustaw y na pierwszą wartosć
            z = int(dice[1])        # ustaw z na drugą wartosc

        elif '-' in dice:           # jeśli w dice jest y
            dice = dice.split("-")  # podziel względem minusa
            y = int(dice[0])
            z = -int(dice[1])

        else:                       # jeśli nie ma plusa ani minusa
            y = int(dice)           # ustaw y na wartość dice
            z = 0                   # z ustaw na 0


        # sprawdzanie czy y jest poprawne
        if y not in dices:
            raise WrongDiceError

        # wykonywanie rzutów
        for i in range(x):
            throw += randint(1, y)

        throw += z

        return throw
    except IndexError:
        print("Niewłaściwy kod rzutu!\nWpisz kod w formacie 'xDy+z'")
    except AttributeError:
        print("Niewłaściwy kod rzutu!\nWpisz kod w formacie 'xDy+z'")
    except ValueError:
        print("Niewłaściwy kod rzutu!\nWpisz kod w formacie 'xDy+z'")
    except WrongDiceError:
        print("Niewłaściwy kod kostki!\nDozwolone kostki to:\n"
              "D3, D4, D6, D8, D10, D12, D20, D100")

    return "Spróbuj jeszcze raz"

if __name__ == '__main__':
    kosc = input("Podaj kosć do gry.\nWpisz kod w formacie 'xDy+z:\n")
    rzut = rpg_dice(kosc)
    print(rzut)
