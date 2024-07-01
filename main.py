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