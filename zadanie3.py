# Zadanie 3 — Logiczne fakty o pogodzie
"""
Poproś użytkownika o 3 wartości logiczne jako 0 lub 1:
- jest_cieplo
- pada_deszcz
- wieje_wiatr

Wypisz:
1) czy jest dobra pogoda na spacer (ciepło i nie pada),
2) czy lepiej zostać w domu (nie jest ciepło lub pada),
3) czy pada albo wieje,
4) czy nie pada,
5) czy jest ciepło, ale nie pada i nie wieje.
"""

jest_cieplo = bool(int(input("Czy jest cieplo: ")))
pada_deszcz = bool(int(input("Czy pada deszcz: ")))
wieje_wiatr = bool(int(input("Czy wieje wiatr: ")))

print(type(wieje_wiatr))
print(type(pada_deszcz))
print(type(wieje_wiatr))

print(f"Czy jest dobra pogoda na spacer (ciepło i nie pada)) {jest_cieplo and not pada_deszcz}")
print(f"czy lepiej zostać w domu (nie jest ciepło lub pada)) {not jest_cieplo or pada_deszcz}")
print(f"czy pada albo wieje {wieje_wiatr or pada_deszcz}")
print(f"czy nie pada {not pada_deszcz}")
print(f"czy jest ciepło, ale nie pada i nie wieje {jest_cieplo and not pada_deszcz and not wieje_wiatr}")