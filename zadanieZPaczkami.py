# Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać, a następnie wymaga podania wagi dla każdej z nich.
#
# Na koniec działania program powinien wyświetlić w podsumowaniu:
#
# Liczbę paczek wysłanych
# Liczbę kilogramów wysłanych
# Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
# Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
#
# Restrykcje:
#
# Waga elementów musi być z przedziału od 1 do 10 kg.
# Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
# W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
# W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.

calkowita_waga_paczek = 0
aktualna_ilosc_paczek = 1
waga_elementu_w_paczce = 0
waga_paczki = 0
waga_najlzejszej_paczki = 20
numer_najlzejszej_paczki = 0

liczba_elementow = int(input("Podaj liczba elementow: "))

for numer_paczki in range(liczba_elementow):
    waga_elementu_w_paczce = float(input(f"Podaj wage elementu {numer_paczki + 1} (w kg): "))
    if waga_elementu_w_paczce < 1 or waga_elementu_w_paczce > 10:
        print(f"Podana waga paczki jest spoza przedzialu 1 - 10 kg")
        break

    if waga_paczki + waga_elementu_w_paczce > 20:
        if waga_paczki < waga_najlzejszej_paczki:
            waga_najlzejszej_paczki = waga_paczki
            numer_najlzejszej_paczki = aktualna_ilosc_paczek
        aktualna_ilosc_paczek += 1
        waga_paczki = waga_elementu_w_paczce

    else:
        waga_paczki += waga_elementu_w_paczce

    calkowita_waga_paczek = calkowita_waga_paczek + waga_elementu_w_paczce

if calkowita_waga_paczek == 0:
    aktualna_ilosc_paczek = 0
    print("Nie dodałeś żadnej paczki!!")

if waga_paczki < waga_najlzejszej_paczki:
    waga_najlzejszej_paczki = waga_paczki
    numer_najlzejszej_paczki = aktualna_ilosc_paczek

waga_paczki = waga_elementu_w_paczce
suma_pustych = aktualna_ilosc_paczek * 20 - calkowita_waga_paczek
print(f"Suma pustych: {suma_pustych}")
print(f"Wysłano {aktualna_ilosc_paczek} paczek")
print(f"Waga paczek to {calkowita_waga_paczek} kg")
print(f"Numer najlzejszej paczki {numer_najlzejszej_paczki}")



