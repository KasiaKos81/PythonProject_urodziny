# Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.
#
# Program po uruchomieniu wyświetla informację o dostępnych komendach:
#
# saldo
#  sprzedaż
# zakup
# konto
# lista
# magazyn
# przegląd
# koniec
#
# Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:
#
# saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
# sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
# zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
# konto - Program wyświetla stan konta.
# lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
# magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
# przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
# koniec - Aplikacja kończy działanie.
#
# Dodatkowe wymagania:
#
# Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
# Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
# Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
# Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.

stan_konta_magazynu = 20000.0
# saldo = 0

magazyn = [
    {
        "produkt": "czekolada",
        "cena": 15.0,
        "ilosc_na_stanie": 10,
        "kod_produktu": "112233"
    },
    {
        "produkt": "chalwa",
        "cena": 8.0,
        "ilosc_na_stanie": 5,
        "kod_produktu": "223344"
    },
    {
        "produkt": "lizak",
        "cena": 2.0,
        "ilosc_na_stanie": 100,
        "kod_produktu": "334455"
    },
    {
        "produkt": "piernik",
        "cena": 40.0,
        "ilosc_na_stanie": 8,
        "kod_produktu": "556677"
    },
    {
        "produkt": "wafelek",
        "cena": 6.0,
        "ilosc_na_stanie": 50,
        "kod_produktu": "667788"
    }
]

while True:
    komenda = input("""
        dostepne komendy:
        1. saldo
        2. sprzedaz
        3. zakup
        4. konto
        5. lista
        6. magazym
        7. przeglad
        8.koniec
        Podaj nr komendy: """)

    match komenda:
        case "1":
            saldo = float(input("Podaj kwotę do dodania lub odjęcia z konta (ujemna)"))
            if stan_konta_magazynu + saldo < 0:
                print("Nie można ustawic saldo na wartosc ujemna")
            else:
                stan_konta_magazynu += saldo
                print(f"Aktualny stan konta magazynu wynosi: {stan_konta_magazynu} PLN")
        case "2":
            kod_produktu = input("Podaj nr produktu")
            znaleziono_produkt = False
            for p in magazyn:
                if p.get("kod_produktu") == kod_produktu:
                    znaleziono_produkt = True
                    ilosc_do_sprzedazy = int(input("Podaj ilosc do sprzedazy: "))
                    if ilosc_do_sprzedazy < p.get("ilosc_na_stanie"):
                        p["ilosc_na_stanie"] -= ilosc_do_sprzedazy
            if not znaleziono_produkt:
                    print("Nie znaleziono produktu o podanym numerze")
        case "3":
            produkt = input("Podaj nazwe produktu: ")
            cena = float(input("Podaj cene produktu: "))
            ilosc_na_stanie = int(input("Podaj ilosc do zakupu: "))
            kod_produktu = input("Podaj kod produktu: ")
            if stan_konta_magazynu - (cena * ilosc_na_stanie) < 0:
                print("Produkt jest za drogi, nie mozna go kupic")
                continue
            else:
                stan_konta_magazynu -= cena * ilosc_na_stanie
            magazyn.append({
                "produkt": produkt,
                "cena": cena,
                "ilosc_na_stanie": ilosc_na_stanie,
                "kod_produktu": kod_produktu,
            })
        case "4":
            print(f"Aktualny stan konta magazynu to: {stan_konta_magazynu} PLN")
        case "5":
            print("Całkowity stan magazynu")
            print(magazyn)
        case "6":
            kod_produktu = input("Podaj nr produktu")
            znaleziono_produkt = False
            for p in magazyn:
                if p.get("kod_produktu") == kod_produktu:
                    znaleziono_produkt = True
                    print(f"Znaleziony produkt to {p}")
                    break
            if not znaleziono_produkt:
                print("Nie ma takiego produktu")
        case "8":
            print("Koniec programu")
            break
