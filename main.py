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