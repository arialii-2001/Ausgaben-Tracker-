import csv
import os
from datetime import date

DATEI_NAME = "ausgaben.csv"


def sicherstellen_kopfzeile():
    if not os.path.exists(DATEI_NAME) or os.path.getsize(DATEI_NAME) == 0:
        with open(DATEI_NAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["datum", "kategorie", "beschreibung", "betrag"])


def betrag_eingeben():
    while True:
        text = input("Betrag eingeben: ").strip()
        try:
            betrag = float(text)
            if betrag <= 0:
                print("Betrag muss größer als 0 sein.")
                continue
            return betrag
        except ValueError:
            print("Bitte eine Zahl eingeben (z. B. 12.50)")


def ausgabe_hinzufuegen():
    sicherstellen_kopfzeile()
    heute = date.today().isoformat()

    kategorie = input("Kategorie (essen/transport/sonstiges): ").strip().lower()
    beschreibung = input("Beschreibung: ").strip()
    betrag = betrag_eingeben()

    with open(DATEI_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([heute, kategorie, beschreibung, betrag])

    print("Ausgabe gespeichert ✅")


def zusammenfassung_anzeigen():
    try:
        with open(DATEI_NAME, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            ausgaben = list(reader)
    except FileNotFoundError:
        print("Noch keine Daten vorhanden.")
        return

    if not ausgaben:
        print("Noch keine Daten vorhanden.")
        return

    gesamt = 0.0
    nach_kategorie = {}

    for zeile in ausgaben:
        betrag = float(zeile["betrag"])
        kat = zeile["kategorie"].strip().lower()
        gesamt += betrag
        nach_kategorie[kat] = nach_kategorie.get(kat, 0) + betrag

    print("\n--- Ausgabenübersicht ---")
    print(f"Gesamtausgaben: {gesamt:.2f} €")
    print("Nach Kategorien:")
    for kat, betrag in sorted(nach_kategorie.items(), key=lambda x: x[1], reverse=True):
        print(f"  {kat}: {betrag:.2f} €")


def hauptmenue():
    while True:
        print("\n1) Ausgabe hinzufügen")
        print("2) Zusammenfassung anzeigen")
        print("q) Beenden")
        auswahl = input("Auswahl: ").strip().lower()

        if auswahl == "1":
            ausgabe_hinzufuegen()
        elif auswahl == "2":
            zusammenfassung_anzeigen()
        elif auswahl == "q":
            break
        else:
            print("Ungültige Eingabe.")


if __name__ == "__main__":
    hauptmenue()