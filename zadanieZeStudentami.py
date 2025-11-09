# Napisz program, który policzy statystyki dotyczące ocen studentów.
#
# Program działa tak:
#   1) Pyta użytkownika: "Ile ocen chcesz podać?"
#   2) Wczytuje kolejno oceny (każda w osobnej linii)
#
# ZASADY:
# - Ocena może być od 2 do 5 (włącznie).
# - Jeśli użytkownik poda ocenę spoza zakresu (np. 1 albo 6),
#     → program natychmiast kończy wczytywanie
#     → i liczy statystyki tylko z poprawnych ocen.
#
# PROGRAM MA WYPISAĆ:
#   1) Ile poprawnych ocen wczytano.
#   2) Ile było ocen niedostatecznych (2).
#   3) Ile było "dobrych" ocen: 4 lub 5.
#   4) Średnią arytmetyczną poprawnych ocen.
#
#
# Przykład:
#     Wejście:
#         5
#         3
#         4
#         5
#         1
#
#     Wynik:
#         Wczytano 3 poprawnych ocen
#         Niedostatecznych: 0
#         Dobrych (4 lub 5): 2
#         Średnia: 4.0
#
# ==========================================

ilosc_ocen = int(input("Podaj ilosc ocen: "))
suma_ocen = 0
ilosc_ocen_niedostatecznych = 0
suma_ocen_niedostateczych = 0
ilosc_dobrych_ocen = 0

for ocena_lp in range(ilosc_ocen):
    ocena = int(input("Podaj ocene: "))
    if ocena >= 2 and ocena <= 5:
        # ilosc_ocen += ocena
        suma_ocen = suma_ocen + ocena
        # print(f"Ilosc poprawnych ocen to: {ilosc_ocen}")
    else:
        break

    if ocena == 2:
        ilosc_ocen_niedostatecznych += 1

    if ocena == 5 or ocena == 4:
        ilosc_dobrych_ocen += 1

print(f"Ilosc poprawnych ocen to: {ilosc_ocen}")
print(f"Ilosc ocen niedostatecznych to: {ilosc_ocen_niedostatecznych}")
print(f"Srednia arytmetyczna z ocen to: {suma_ocen/ilosc_ocen}")
print(f"Ilosc dobrych ocena to: {ilosc_dobrych_ocen}")