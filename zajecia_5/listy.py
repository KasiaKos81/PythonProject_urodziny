uczen_1 = "Adam A"
uczen_2 = "Bartek B"
uczen_3 = "Cezary C"
# uczen_4 = input("Podaj kolejnego ucznia: ")

lista_uczniow = ["Adam A", "Bartek B", "Cezary C"]
# print(type(lista_uczniow))
lista_uczniow_2 = [uczen_1, uczen_2, uczen_3]
# print(type(lista_uczniow_2))
lista_wartosci = ["Jablko", 1, True, 23.5, None]
# print(lista_wartosci)

lista_inny_sposob = list()
lista_na_pozniej = []

# print(lista_uczniow[0])
#
# for uczen in lista_uczniow:
#     if uczen == "Cezary C":
#         print("Znalazlem Cezarego")
#     print(uczen)

# for index, uczen in enumerate(lista_uczniow):
#     if uczen == "Cezary C":
#         print(f"Znalazlem Cezarego pod indeksem: {index}")

lista_uczniow.append("Dariusz D")
print(lista_uczniow)

lista_uczniow.insert(0, "Emil E")
print(lista_uczniow)
print(len(lista_uczniow))

#ZMIANA WARTOŚCI
lista_uczniow[0] = "Adam Górski"
print(lista_uczniow)

lista_adamow =["Adam A", "Adam A"]
for index, adam in enumerate(lista_adamow):
    lista_adamow[index] = "Adam G"
print(lista_adamow)

#USUWANIE

lista_uczniow.remove("Dariusz D")

# print od tylu
print(lista_uczniow[-1])

#slajsowanie

print(lista_uczniow[0:5])
# co drugi element
print(lista_uczniow[0:5:2])


