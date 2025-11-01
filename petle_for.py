ilosc_ocen = int(input("Podaj ilosc ocen do sredniej: "))
suma_ocen = 0

obecna_ocena=0

while obecna_ocena < ilosc_ocen:
    obecna_ocena = obecna_ocena + 1
    ocena = int(input("Podaj ocene: "))
    suma_ocen = suma_ocen + ocena
print(f"Srednia arytmetyczna z ocen to: {suma_ocen/ilosc_ocen}")

for ocena_lp in range(ilosc_ocen):
    ocena = int(input("Podaj ocene: "))
    suma_ocen = suma_ocen + ocena
print(f"Srednia arytmetyczna z ocen to: {suma_ocen/ilosc_ocen}")

for litera in "Kasia":
    print(f"litera: {litera}")

"""
while <tymczasowa_zmienna> in <obiekt, po ktorym bedziemy iterowac>:
    <kod do wykonania>
"""