import requests
import pandas as pd
import csv

def pobierz_dane_kryptowalut():
    url = "https://api.coincap.io/v2/assets"
    parametry = {
        "ids": "bitcoin,ethereum",
        "convert": "USD"
    }

    odpowiedz = requests.get(url, params=parametry)
    dane_kryptowalut = odpowiedz.json()

    return dane_kryptowalut["data"]

def zapisz_do_csv(dane_kryptowalut, nazwa_pliku):
    pola = ["name", "symbol", "priceUsd", "marketCapUsd", "volumeUsd24Hr"]
    with open(nazwa_pliku, mode="w", newline="") as plik_csv:
        writer = csv.DictWriter(plik_csv, fieldnames=pola)
        writer.writeheader()
        for dane in dane_kryptowalut:
            writer.writerow(dane)

def main():
    try:
        dane_kryptowalut = pobierz_dane_kryptowalut()
        nazwa_pliku = "dane_kryptowalut.csv"
        zapisz_do_csv(dane_kryptowalut, nazwa_pliku)
        print(f"Dane kryptowalut zostały zapisane do pliku {nazwa_pliku}.")
    except requests.exceptions.RequestException as e:
        print(f"Wystąpił błąd podczas pobierania danych: {e}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()
