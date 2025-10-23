# Zadanie 1 — Porównanie wieku
"""
Ask user about age (even numbers): age of Michal and age of Ania.
Print:
1) is Michal older than Ania,
2) is Ania younger or same age as Michal,
3) is Ania same age as Michal.
use: >, <=, ==.
"""

michal_age = int(input("Michal, please pass an info about your age: "))
ania_age = int(input("Ania, please pass an info about your age: "))
print(type(michal_age))
print(type(ania_age))
print(michal_age)
print(ania_age)

print(f"Is Michal older than Ania {michal_age > ania_age}")
print(f"Is Ania younger or same age as Michal")
print(michal_age >= ania_age)
print(f"is Ania same age as Michal")
print(michal_age == ania_age)
