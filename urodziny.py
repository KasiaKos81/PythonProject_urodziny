#### KARTKA URODZINOWA

import datetime

imie_odbiorcy = input("Podaj imię odbiorcy: ")
rok_urodzenia = int(input("Podaj rok urodzenia odbiorcy: "))
spersonalizowana_wiadomosc = input("Podaj spersonalizowana wiadomosc: ")
imie_nadawcy = input("Podaj swoje imie: ")

wiek_odbiorcy = datetime.datetime.now().year - rok_urodzenia

print(f"{imie_odbiorcy} wszystkiego najlepszego z okazji {wiek_odbiorcy} urodzin!")
print(spersonalizowana_wiadomosc)
print(imie_nadawcy)