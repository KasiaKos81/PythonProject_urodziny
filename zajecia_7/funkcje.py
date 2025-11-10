# def przywitaj_sie():
#     print("Hello World")
#
# przywitaj_sie()

def sprawdz_wiek(wiek):
    if wiek < 18:
        print("Gówniarz")
    else:
        print("Możesz kupic alkohol")

def sprawdz_wiek_i_przywitaj_sie(wiek, imie):
    if wiek < 18:
        print("Gówniarz")
    else:
        print("Możesz kupic alkohol")
    print(f"Witaj {imie}")

wiek1 = int(input("Podaj wiek: "))
imie1 = int(input("Podaj imie: "))
# sprawdz_wiek(wiek)

sprawdz_wiek_i_przywitaj_sie(wiek1,imie1)
sprawdz_wiek_i_przywitaj_sie(wiek=wiek1,imie=imie1)

miasta =[("Warszawa", 20, 67.6), ("Szczecin", 30, 84.8)]

def obliczanie_temp_w_F(temp_w_celsjuszach):
    temp_F = temp_w_celsjuszach * 9/5 + 32
    print(f"Temperatura w F {temp_F}")

obliczanie_temp_w_F(-20)