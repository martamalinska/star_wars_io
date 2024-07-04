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

# Funkcja do tworzenia droida
def tworzenie_droida():
    nazwa = input("Podaj nazwę droida: ")
    ilosc = int(input("Podaj ilość do wyprodukowania: "))
    stan_magazynowy = int(input("Podaj stan magazynowy: "))
    
    print("Wybierz specjalną umiejętność:")
    umiejetnosci = ['Niewidzialność', 'Egzotyczny taniec', 'Nadludzka siła', 'Zbieranie grzybów']
    for idx, umiejetnosc in enumerate(umiejetnosci, 1):
        print(f"{idx}. {umiejetnosc}")
    umiejetnosc_wybrana = int(input("Wybierz numer umiejętności: "))
    umiejetnosc = umiejetnosci[umiejetnosc_wybrana - 1]

    print("Wybierz wersję oprogramowania:")
    wersje = ['1.0', '2.0', '3.0', '4.0', '5.0']
    for idx, wersja in enumerate(wersje, 1):
        print(f"{idx}. {wersja}")
    wersja_wybrana = int(input("Wybierz numer wersji: "))
    wersja = wersje[wersja_wybrana - 1]

    droid = {
        'nazwa': nazwa,
        'ilosc': ilosc,
        'stan_magazynowy': stan_magazynowy,
        'umiejetnosc': umiejetnosc,
        'wersja': wersja
    }
    
    zapisz_droida(droid)
    print("Droid został zapisany!")

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

# Główna funkcja aplikacji
def main():
    while True:
        print("Wybierz opcję:")
        print("1. Tworzenie droida")
        print("2. Raportowanie")
        print("3. Wyjście")
        
        opcja = int(input("Wybierz numer opcji: "))
        
        if opcja == 1:
            tworzenie_droida()
        elif opcja == 2:
            raportowanie()
        elif opcja == 3:
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()
