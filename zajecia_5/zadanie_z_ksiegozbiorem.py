"""
Stwórz system zarządzania księgozbiorem bibliotecznym, który pozwoli na monitorowanie przepływu książek oraz śledzenie budżetu biblioteki.
Po uruchomieniu systemu użytkownik otrzymuje listę komend do wyboru:
- doładowanie
- wypożycz
- zakup
- bieżący_stan
- zestawienie
- szczegóły_książki
- dziennik
- zakończ
Funkcje po wywołaniu danych komend są następujące:
1. doładowanie - Umożliwia dodanie środków do budżetu biblioteki lub ich odjęcie.
2. wypożycz - Rejestruje wypożyczenie książki przez czytelnika. System żąda podania numeru ISBN. Koszt wypożyczenia jest dodawany do budżetu.
3. zakup - Rejestruje zakup nowych książek dla biblioteki. System pyta o tytuł książki, koszt zakupu i liczbę egzemplarzy. Zakupione książki są dodawane do zbioru, a środki są odprowadzane z budżetu, który nie może być negatywny po transakcji.
4. bieżący_stan - Wyświetla aktualny stan środków finansowych.
5. zestawienie - Podsumowuje cały księgozbiór biblioteki wraz z cenami zakupu i ich ilością.
6. szczegóły_książki - Wyświetla dostępność i dane dotyczące pojedynczej książki po wpisaniu numeru ISBN.
7. dziennik - Przegląd historii transakcji. Podając wartości "od" i "do", system wyświetla zapisane działania w podanym zakresie. W przypadku pustych pól lub wartości spoza zakresu, użytkownik jest informowany o błędzie i wyświetlana jest liczba wszystkich zarejestrowanych transakcji.
8. zakończ - Kończy działanie programu.
**Inne wymagania:**
- System działa do momentu wybrania komendy zakończ.
- Operacje doładowanie, wypożycz oraz zakup są zapisywane dla późniejszej referencji przy użyciu komendy dziennik.
- Po każdej komendzie system wyświetla ponownie listę dostępnych opcji i prosi o wybór kolejnej.
- Ochrona przed błędami użytkownika, takimi jak wpisywanie błędnych danych czy żądanie zakupu na wartości ujemne.
"""

saldo_ksiegarni = 10000.0
ksiegozbior = [
    {
        "autor": "Adam Mickiewicz",
        "tytul": "Nuda",
        "rok_wydania" : 1780,
        "cena" : 30.0,
        "ISBN" : "12345"
    }
]
