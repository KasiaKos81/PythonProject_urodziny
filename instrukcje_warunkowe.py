print("Witaj w żabce: ")

nazwa_produktu = input("Podaj nazwe produktu: ")
cena_produktu = float(input("Podaj cene produktu: "))

if nazwa_produktu == "papierosy" or nazwa_produktu == "wodka":
    wiek = int(input("Podaj wiek: "))
    if wiek >= 18:
        print(f"Zakupiles {nazwa_produktu} w cenie {cena_produktu}. Masz {wiek} lat")
    else:
        print(f"jestes za mlody, nie mozesz kupic {nazwa_produktu}.")

else:
    print(f"zakupiles {nazwa_produktu} w cenie {cena_produktu}.")
print(f"zegnamy, do zobaczenia ponownie w zabce!")

"""
if <warunek>:
    <kod do wykonania>
"""

zawod = input("Podaj zawod: ")
wiek1 = int(input("Podaj wiek1: "))

if zawod == "policjant":
    print(f"do emerytury zostalo ci {50 - wiek1}")
elif zawod == "zolnierz":
    print(f"do emerytury zostalo ci {45 - wiek1}")
elif zawod == "nauczyciel":
    print(f"do emerytury zostalo ci {40 - wiek1}")
elif zawod == "developer":
    print(f"nie dozyjesz emerytury")
else:
    print(f"nie znam takiego zawodu")

