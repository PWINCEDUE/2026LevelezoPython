# 2026LevelezoPython
# Informatikai eszköznyilvántartó

## Név: Juhász Szabolcs, PWINCE

## Feladat rövid leírása:

A program grafikus felületen segíti a hálózati eszközök nyilvántartását
és elérhetőségük ellenőrzését.

## Indításhoz szükséges:
- Windows operációs rendszer, mert a ping parancs kapcsolói erre készültek.
- Telepített Python 3, Tkinter támogatással.
- A main.py, jsz_halozat.py és jsz_fajlkezeles.py fájlok azonos mappában legyenek.
- Hálózati kapcsolat a hálózati eszközök vizsgálatához.

- Indítófájl: main.py
- Alapablak: root
- Alkalmazáspéldány: app

## Fontosabb funkciók:
- Saját számítógép nevének és névhez tartozó IPv4-címének lekérése.
- IPv4 cím keresése gépnév alapján, illetve gépnév keresése IP cím alapján.
- Eszközök elérhetőségének ellenőrzése ping paranccsal.
- IP tartomány vizsgálata, legfeljebb 256 címes megkötéssel.
- A ping kérésre válaszoló eszközök hozzáadása a táblázathoz.
- A kijelölt eszközök törlése.
- A nyilvántartás mentése és betöltése JSON fájlból.
A tartalomkeresés háttérszálon fut, illetve az eseménykezelés is biztosított.

## Felhasznált modulok:

### tkinter és tkinter.ttk  (tanult) grafikai modul

Az ablak, a gombok, a beviteli mezők és a táblázat létrehozása.

Használt osztályok:
- Tk, Style, Frame, LabelFrame, Label, Button, Entry,
  Treeview, Scrollbar.

Fontosabb metódusok:
- title(), geometry(), minsize(): Ablakbeállítások.
- pack(), grid(), columnconfigure(), rowconfigure(): Elrendezés.
- configure(), config(): Megjelenés és tartalom módosítása.
- get(), insert(), delete(): Adatok kiolvasása és módosítása.
- heading(), column(): Táblázatoszlopok beállítása.
- get_children(), selection(), item(), set(): Táblázat kezelése.
- yview(), set(): Görgetés kezelése.
- after(): Az eredmény időzített ellenőrzése.
- mainloop(): Az eseménykezelés futtatása.

### socket -(bemutatandó) modul

- gethostname(): A saját számítógép nevének lekérése.
- gethostbyname(): IPv4 cím lekérése gépnév alapján.
- gethostbyaddr(): Gépnév lekérése IP cím alapján.

### ipaddress

- IPv4Address(): IPv4 címek ellenőrzése és átalakítása a tartomány összeállításához.

### subprocess

- run(): A Windows ping parancsának futtatása.

### json

- dump(): Az eszközlista mentése JSON-formátumban.
- load(): A mentett eszközlista betöltése.

### threading

- Thread(): Háttérszál létrehozása a tartománykereséshez.
- start(): A háttérszál elindítása.

### queue

- Queue(): Az eredmény átadására szolgáló várakozási sor létrehozása.
- put(): Eredmény elhelyezése a sorban.
- get_nowait(): Eredmény kiolvasása várakozás nélkül.

## Saját modulok és függvények:

### jsz_halozat.py

- jsz_gepnev_lekerese(): Saját gépnév lekérése.
- jsz_ip_cim_lekerese(): IPv4 cím lekérése gépnév alapján.
- jsz_gepnev_lekerese_ip_alapjan(): Gépnév keresése IP cím alapján.
- jsz_elerhetoseg_ellenorzese(): Ping válasz ellenőrzése.
- jsz_ipv4_cim_ervenyes(): IPv4 cím érvényességének ellenőrzése.
- jsz_ip_tartomany_letrehozasa(): A vizsgálandó címek összeállítása.
- jsz_tartomany_vizsgalata(): A pingre válaszoló eszközök összegyűjtése.

### jsz_fajlkezeles.py

- jsz_eszkozok_mentese(): Az eszközlista mentése fájlba.
- jsz_eszkozok_betoltese(): Az eszközlista betöltése és alapvető szerkezeti ellenőrzése.

## Saját osztály:

A main.py fájlban található JszEszkozNyilvantarto osztály létrehozza a kezelőfelületet
és kezeli a felhasználói műveleteket.

### Metódusai:
- __init__(): A kezelőfelület létrehozása.
- jsz_visszajelzes(): Színes állapotüzenetek megjelenítése.
- jsz_gepnev_megjelenitese(): A saját gép adatainak megjelenítése.
- jsz_ip_cim_megjelenitese(): Gépnévhez tartozó IPv4 cím megjelenítése.
- jsz_ip_mezo_ellenorzese(): A megadott IP cím ellenőrzése.
- jsz_ip_alapjan_gepnev_megjelenitese(): Névlekérés eredményének kiírása.
- jsz_elerhetoseg_megjelenitese(): Pingelés eredményének kiírása.
- jsz_tartomany_ellenorzese(): Tartomány ellenőrzése és keresés indítása.
- jsz_eszkoz_hozzaadasa(): Eszköz felvétele a táblázatba.
- jsz_eszkoz_torlese(): Kijelölt sorok törlése.
- jsz_mentes_inditasa(): Mentés indítása.
- jsz_betoltes_inditasa(): Mentett adatok betöltése a táblázatba.
- jsz_kereses_hatterben(): Tartománykeresés végrehajtása háttérszálon.
- jsz_kereses_eredmenyenek_atvetele(): Találatok átvétele és megjelenítése.

