print("Hello World")

######## ZMIENNE LICZBOWE

wiek = 30 # typ integer

wiek2 = 20 + 6
wiek3 = 120 /4 # zwraca typ float
modulo = 6 % 4 # reszta z dzielenia - czyli 2 :)
cena_jablka = 2.99
ilosc_jablek = 0.66

print(wiek)
print(wiek2)
print(wiek3)
print(modulo)

wartosc_jablek = cena_jablka * ilosc_jablek * ilosc_jablek

print(round(wartosc_jablek,2)) # ta 2 informuje do ilu miejsc po przecinku zaookraglamy


############# ZMIENNE TESKTOWE

imie3 = "Katarzyna"

print(imie3)

print(f"my name is {imie3}")

nazwisko = "Kowlaski"
imie_i_nazwisko = imie3 + " " + nazwisko
print(f"my name and last name are {imie_i_nazwisko}")

nazwisko_1 = nazwisko.lower()
nazwisko_2 = nazwisko.upper()
nazwisko_3 = nazwisko.capitalize()

print(nazwisko_3)

# ZMIENNE BOOLEAN

czy_jestem_pelnoletni = True
czy_jestem_na_emeryturze = False

print(czy_jestem_pelnoletni and czy_jestem_na_emeryturze)
print(f"Sprawdzenie or {czy_jestem_pelnoletni or czy_jestem_na_emeryturze}")

cena_jablka1 = 2.99
cena_gruszki = 3.49
cena_pietruszki = 3.49

print(cena_jablka1 > cena_gruszki)
print(cena_jablka1 != cena_gruszki)
print(f"Czy obie ceny sa rowne {cena_jablka1 == cena_gruszki}")
print(f"Czy obie ceny sa rowne gruszka vs pietruszka {cena_pietruszki == cena_gruszki}")
print(not czy_jestem_pelnoletni)

dzielenie = 120 / 4
print(dzielenie)

print(type(dzielenie))


dzielenie_Integer = int(dzielenie)
print(dzielenie_Integer)
print(dzielenie_Integer.is_integer())
wiek_string ="30"
wiek_int = int(wiek_string)
print(f"checking if wiek_int is integer {wiek_int.is_integer()}")

print(bool(5))
print(bool(0))

#### ZMIENNA NONE

zmienna_niezdefiniowana = None
print(type(zmienna_niezdefiniowana))

### OPERACJA WEJSCIA

imie_uzytkownika = input("Podaj swoje imie: ")
nazwisko_uzytkownika = input("Podaj swoje nazwisko: ")
wiek_uzytkownika = input("Podaj swoj wiek: ")
is_wiek_a_number = (print(wiek_uzytkownika.isdigit))
print(f"utworzony user {imie_uzytkownika}{nazwisko_uzytkownika}, on ma lat {wiek_uzytkownika}")
print(type(imie_uzytkownika))
print(type(nazwisko_uzytkownika))
print(type(wiek_uzytkownika))

### ZMIENNE TE$KSTOWE

imie22222 = "Kacper\n" * 60
print(imie22222)
print(type(imie22222))

imie222223 = "Kacper\t" * 60
print(imie222223)

tekst_o_kacprze = "był sobie ktos o imieniu: 'Kacper' "
print(tekst_o_kacprze)

# ROK URODZENIA
import datetime
obecny_rok = datetime.datetime.now().year
print(obecny_rok)
rok_urodzenia = int(input("Podaj rok urodzenia: "))




