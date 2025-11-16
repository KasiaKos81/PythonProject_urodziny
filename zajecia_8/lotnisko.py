# Jesteś szefem firmy technologicznej tworzącej system zarządzania dla międzynarodowego lotniska. System ten ma obsługiwać dane związane z lotami, liniami lotniczymi, pasażerami oraz stewardessami. Każdy lot może mieć przypisanych wielu pasażerów i jedną stewardessę, natomiast linie lotnicze mogą obsługiwać nieograniczoną liczbę lotów. Celem jest stworzenie programu, który pozwoli na efektywne zarządzanie i dostarczanie właściwych informacji na potrzeby logistyki i obsługi klienta lotniska.
#
# **Program do zarządzania danymi lotów na międzynarodowym lotnisku**
# Program powinien umożliwić:
# 1. Dodanie nowych danych do systemu:
#    - Pasażera z przypisanym numerem lotu.
#    - Stewardessy z przypisanym numerem lotu.
#    - Linii lotniczej, która może obsługiwać wiele różnych lotów.
# 2. Przeglądanie i zarządzanie istniejącymi informacjami:
#    - Pobranie listy pasażerów danego lotu.
#    - Znalezienie przypisanej linii lotniczej dla wybranego pasażera.
#    - Wyświetlenie listy lotów danej linii lotniczej.
#    - Otrzymanie listy wszystkich pasażerów dla lotu, którego stewardessą jest wybrana osoba.
# **Polecenia programu**
# Po uruchomieniu, program powinien wyświetlić menu z następującymi komendami:
# - dodaj - przechodzi do menu dodawania nowych danych.
# - przeglądaj - przechodzi do menu przeglądania i zarządzania danymi.
# - zakończ - kończy działanie programu.
# **Menu dodawania danych (dodaj):**
# Użytkownik może wybrać:
# - pasażer - dodanie pasażera wymaga wprowadzenia imienia i nazwiska, numeru lotu.
# - stewardessa - dodanie stewardessy wymaga wprowadzenia imienia i nazwiska, numeru lotu, do którego jest przypisana.
# - linia_lotnicza - dodanie linii lotniczej wymaga wprowadzenia jej nazwy.
# - zakończ_dodawanie - powrót do głównego menu.
# **Menu przeglądania i zarządzania danymi (przeglądaj):**
# Użytkownik może wybrać:
# - lot - wprowadzenie numeru lotu wyświetla listę pasażerów tego lotu.
# - pasażer - wprowadzenie imienia i nazwiska pasażera wyświetla nazwę linii lotniczej.
# - linia_lotnicza - wprowadzenie nazwy linii lotniczej wyświetla listę lotów obsługiwanych przez linię.
# - stewardessa - wprowadzenie imienia i nazwiska stewardessy wyświetla listę pasażerów jej lotu.
# - zakończ_przeglądanie - powrót do głównego menu.
# **Zakończenie pracy programu**
# Polecenie zakończ powoduje zamknięcie aplikacji.

class Pasazer:
    def __init__(self, imie, nazwisko, numer_lotu, numer_miejsca_w_samolocie=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_lotu = numer_lotu
        self.numer_miejsca_w_samolocie = numer_miejsca_w_samolocie

    def __str__(self):
        return f" Pasazer {self.imie} {self.nazwisko} z lotu {self.numer_lotu} i miejscu {self.numer_miejsca_w_samolocie}"

class LiniaLotnicza
    def __init__(self, nazwa_linii, lista_lotow):
        self.nazwa_linii = nazwa_linii
        self.lista_lotow = lista_lotow

    def __str__(self):
        return f"linia lotnicza {self.nazwa_linii} z lotami {self.lista_lotow}"
