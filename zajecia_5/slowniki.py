uczen = ["Ada", "Ad", 30, True, [1,2,3]]

uczen_slownik = {
    "imie" : "Ada",
    "nazwisko" : "Ad",
    "czy_studiuje" : True,
    "oceny" : [1,2,3]
}

print(uczen_slownik)

# znajdowanie po kluczu

print(uczen_slownik["imie"])
print(uczen_slownik.get("nazwisko"))
print(uczen_slownik.get("dupa"))
# if uczen_slownik.keys().__contains__("czy_studiuje"):
#     print(uczen_slownik.get("czy_studiuje"))
# else: print("no such key")

# dodawanie
uczen_slownik["klasa"] = "2A"
print(uczen_slownik)

# usuwanie
del uczen_slownik["czy_studiuje"]
print(uczen_slownik)

# iteracja po slowniku
for element in uczen_slownik:
    print(element)

for element in uczen_slownik.keys():
    print(element)
for element in uczen_slownik.values():
    print(element)

for klucz, wartosc in uczen_slownik.items():
    print(f"{klucz}: {wartosc}")



