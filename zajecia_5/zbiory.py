kolory = {"czerwony", "czarny", "niebieski"}
zbior = {True, "Adam", 2.0, "zielony"}
print(kolory)

for kolor in kolory:
    print(kolor)

if "czerwony" in kolory:
    print("Zbiór zawiera czerwony!")

kolory.add("zielony")
print(kolory)
kolory.remove("czerwony")
print(kolory)

kolory.remove("dupa")
