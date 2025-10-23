# Zadanie 2 — Porównanie cen owoców
"""
Poproś użytkownika o trzy ceny (liczby zmiennoprzecinkowe w zł): jabłka, pomarańczy i banana.
Wypisz:
1) czy jabłko jest tańsze od pomarańczy,
2) czy pomarańcza jest droższa od banana,
3) czy jabłko i banan kosztują tyle samo,
4) czy jabłko jest tańsze od pomarańczy lub równe bananowi,
5) czy pomarańcza jest droższa od jabłka i banana jednocześnie.
"""

cena_jablka = float(input("Podaj cene jablka: "))
cena_pomaranczy = float(input("Podej cene pomaranczy: "))
cena_banana = float(input("Podaj cene banana: "))

print(type(cena_jablka))
print(type(cena_pomaranczy))
print(type(cena_banana))
print(cena_jablka)
print(cena_pomaranczy)
print(cena_banana)

print(f"Czy jabłko jest tańsze od pomarańczy {cena_jablka < cena_pomaranczy}")
print(f"Czy pomarańcza jest droższa od banana {cena_pomaranczy > cena_banana}")
print(f"Czy jabłko i banan kosztują tyle samo {cena_jablka == cena_banana}")
print(f"Czy jabłko jest tańsze od pomarańczy lub równe bananowi {cena_jablka == cena_banana or cena_jablka < cena_pomaranczy}")
print(f"Czy pomarańcza jest droższa od jabłka i banana jednocześnie {cena_pomaranczy > cena_banana and cena_jablka < cena_pomaranczy}")