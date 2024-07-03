import csv
import os

CSV_FILE = 'droidy.csv'

def zapisz_droida(droid):
    plik_istnieje = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as plik:
        pola = ['nazwa', 'ilosc', 'stan_magazynowy', 'umiejetnosc', 'wersja']
        writer = csv.DictWriter(plik, fieldnames=pola)
        if not plik_istnieje:
            writer.writeheader()
        writer.writerow(droid)

def raportowanie():
    if not os.path.isfile(CSV_FILE):
        print("Brak danych do wyświetlenia.")
        return

    print("Jakie wartości chcesz wyświetlić?")
    print("1. Nazwa")
    print("2. Stan magazynowy")
    wybor = int(input("Wybierz numer opcji: "))

    with open(CSV_FILE, mode='r', newline='') as plik:
        reader = csv.DictReader(plik)
        if wybor == 1:
            print("Nazwa droidów:")
            for wiersz in reader:
                print(wiersz['nazwa'])
        elif wybor == 2:
            print("Stany magazynowe droidów:")
            for wiersz in reader:
                print(f"{wiersz['nazwa']}: {wiersz['stan_magazynowy']}")
        else:
            print("Nieprawidłowa opcja.")