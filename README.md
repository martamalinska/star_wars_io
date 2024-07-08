# Droid Management System

Droid Management System to prosty program do zarządzania danymi droidów. Program umożliwia tworzenie nowych droidów oraz generowanie raportów na temat istniejących droidów zapisanych w pliku CSV.

## Wymagania

- Python 3.x
- Biblioteka `csv` (wbudowana w Pythonie)
- Biblioteka `os` (wbudowana w Pythonie)

## Użycie

1. Uruchom skrypt `main.py`:

    ```bash
    python main.py
    ```

2. Wybierz jedną z dostępnych opcji z menu:

    - **Tworzenie droida**: Umożliwia dodanie nowego droida do systemu.
    - **Raportowanie**: Umożliwia wygenerowanie raportu o droidach zapisanych w systemie.
    - **Wyjście**: Zakończenie działania programu.

### Tworzenie droida

1. Wybierz opcję `1` z menu głównego.
2. Podaj nazwę droida.
3. Podaj ilość do wyprodukowania.
4. Podaj stan magazynowy.
5. Wybierz specjalną umiejętność droida z listy:
    - Niewidzialność
    - Egzotyczny taniec
    - Nadludzka siła
    - Zbieranie grzybów
6. Wybierz wersję oprogramowania droida z listy:
    - 1.0
    - 2.0
    - 3.0
    - 4.0
    - 5.0

Po wprowadzeniu wszystkich danych, droid zostanie zapisany do pliku `droidy.csv`.

### Raportowanie

1. Wybierz opcję `2` z menu głównego.
2. Wybierz typ raportu:
    - `1`: Wyświetlenie nazw wszystkich droidów.
    - `2`: Wyświetlenie stanów magazynowych wszystkich droidów.

Raport zostanie wygenerowany na podstawie danych zapisanych w pliku `droidy.csv`.

## Struktura pliku CSV

Plik `droidy.csv` przechowuje dane droidów w następującym formacie:

| nazwa  | ilosc | stan_magazynowy | umiejetnosc | wersja |
|--------|-------|-----------------|-------------|--------|
| Droid1 | 10    | 5               |             | 1.0    |
| Droid2 | 20    | 10              |             | 2.0    |

## Licencja

Ten projekt jest licencjonowany na warunkach licencji MIT.
