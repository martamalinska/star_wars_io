import csv
import os

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