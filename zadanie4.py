# Zadanie 4
# Zadanie 4 — Typy i konwersje z wejścia
"""
Poproś użytkownika o wiek (tekst) i wagę (tekst, np. '72.5').
Następnie:
- skonwertuj wiek na int, wagę na float,
- dodaj 5 do wieku,
- dodaj 2.3 do wagi,
- wypisz nowe wartości oraz ich typy.
"""

wiek = (input("Podaj wiek: "))
waga = (input("Podaj wage: "))
wiek1 =int(wiek)
waga1 =float(waga)

print(type(wiek1))
print(type(waga1))

wiek_plus = wiek1 + 5
#wiek_plus += 5
waga_plus = waga1 + 2.3

print(wiek_plus)
print(waga_plus)
