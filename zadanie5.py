# Zadanie 5 — Cukierki dla dzieci
"""
Poproś użytkownika o liczbę cukierków i liczbę dzieci.
Policz i wypisz:
- ile cukierków dostanie każde dziecko (//),
- ile cukierków zostanie (%),
- czy cukierków wystarczy dla wszystkich dzieci (cukierki >= dzieci),
- czy cukierków jest mniej niż 10 lub więcej niż 100.
"""

ilosc_cukierkow = (int(input("Podaj ilość cukierków: ")))
liczba_dzieci = (int(input("Podaj ilość dzieci: ")))

ile_cukierkow_dostana = ilosc_cukierkow // liczba_dzieci
print(ile_cukierkow_dostana)
ile_cukierkow_zostanie = ilosc_cukierkow % liczba_dzieci
print(ile_cukierkow_zostanie)
czy_cukierkow_wystarczy = ilosc_cukierkow >= liczba_dzieci
print(czy_cukierkow_wystarczy)