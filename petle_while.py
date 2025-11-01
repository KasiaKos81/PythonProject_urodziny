wiek = int(input("Podaj wiek: "))

while wiek < 66:
    if wiek >= 65:
        print(f"juz jestes na emeryturze")
        break
    elif wiek == 18:
        print(f"nie myśl o emeryturze, idz do pracy")
        break
    else:
        print(f"nie masz jeszcze 65 lat, Twój wiek to {wiek}")
        wiek += 1

"""
while <warunek do spelnienia>: <- tutaj musimy mief prawdziwy warunek
    <kod do wykonania>
"""

liczba = 0
while True:
    liczba += 1
    if liczba == 2:
        pass
    if liczba == 5:
        continue
    print(liczba)
    if liczba == 10:
        break