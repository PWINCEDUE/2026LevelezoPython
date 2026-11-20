import json


def jsz_eszkozok_mentese(fajlnev, eszkozok):
    with open(fajlnev, "w", encoding="utf-8") as fajl:
        json.dump(eszkozok, fajl, ensure_ascii=False, indent=4)


def jsz_eszkozok_betoltese(fajlnev):
    with open(fajlnev, "r", encoding="utf-8") as fajl:
        eszkozok = json.load(fajl)

    if not isinstance(eszkozok, list):
        raise ValueError("A fájlnak egy eszközlistát kell tartalmaznia!")

    for sor_adatai in eszkozok:
        if not isinstance(sor_adatai, list) or len(sor_adatai) != 3:
            raise ValueError("Minden eszközhöz három adat szükséges!")

    return eszkozok

