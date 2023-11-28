import os
import datetime

def lue_muistikirjaa(tiedostonimi):
    try:
        with open(tiedostonimi, 'r') as tiedosto:
            sisalto = tiedosto.read()
            print(sisalto)
    except FileNotFoundError:
        print(f"Tiedostoa {tiedostonimi} ei löydy.")

def lisaa_merkinta(tiedostonimi, merkinta):
    aika = datetime.datetime.now().strftime("%H:%M:%S %d/%m/%y")
    try:
        with open(tiedostonimi, 'a') as tiedosto:
            tiedosto.write(f"{merkinta}::{aika}\n")
        print(f"Merkintä lisätty onnistuneesti.")
    except FileNotFoundError:
        print(f"Tiedostoa {tiedostonimi} ei löydy.")

def tyhjenna_muistikirja(tiedostonimi):
    try:
        with open(tiedostonimi, 'w') as tiedosto:
            tiedosto.write('')
        print("Muistikirja tyhjennetty.")
    except FileNotFoundError:
        print(f"Tiedostoa {tiedostonimi} ei löydy.")

def vaihda_muistiota():
    tiedostonimi = input("Anna tiedoston nimi: ")
    if not os.path.isfile(tiedostonimi):
        with open(tiedostonimi, 'w') as tiedosto:
            tiedosto.write('')
        print(f"Tiedostoa ei löydy, luodaan tiedosto.")
    return tiedostonimi

def main():
    tiedostonimi = "muistio.txt"
    if not os.path.isfile(tiedostonimi):
        with open(tiedostonimi, 'w') as tiedosto:
            tiedosto.write('')
        print("Oletusmuistiota ei löydy, luodaan tiedosto.")

    while True:
        print(f"Käytetään muistiota: {tiedostonimi}")
        print("(1) Lue muistikirjaa")
        print("(2) Lisää merkintä")
        print("(3) Tyhjennä muistikirja")
        print("(4) Vaihda muistiota")
        print("(5) Lopeta")

        valinta = input("Mitä haluat tehdä?: ")

        if valinta == '1':
            lue_muistikirjaa(tiedostonimi)
        elif valinta == '2':
            merkinta = input("Kirjoita uusi merkintä: ")
            lisaa_merkinta(tiedostonimi, merkinta)
        elif valinta == '3':
            tyhjenna_muistikirja(tiedostonimi)
        elif valinta == '4':
            tiedostonimi = vaihda_muistiota()
        elif valinta == '5':
            print("Lopetetaan.")
            break
        else:
            print("Virheellinen valinta. Valitse uudelleen.")

if __name__ == "__main__":
    main()