import json


def jsz_eszkozok_mentese(fajlnev, eszkozok):
    with open(fajlnev, "w", encoding="utf-8") as fajl:
        json.dump(eszkozok, fajl, ensure_ascii=False, indent=4)


def jsz_eszkozok_betoltese(fajlnev):
    with open(fajlnev, "r", encoding="utf-8") as fajl:
        eszkozok = json.load(fajl)

        return eszkozok
