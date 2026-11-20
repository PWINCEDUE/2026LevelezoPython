import queue
import threading
import tkinter as tk
from tkinter import ttk

import jsz_fajlkezeles
import jsz_halozat


class JszEszkozNyilvantarto:
    def __init__(self, alapablak):
        alapablak.title("Informatikai eszköznyilvántartó")
        alapablak.geometry("950x700")
        alapablak.minsize(850, 650)

        stilus = ttk.Style()
        stilus.configure("TButton", padding=(10, 6))
        stilus.configure("Treeview", rowheight=28)

        fo_keret = ttk.Frame(alapablak, padding=15)
        fo_keret.pack(fill="both", expand=True)

        cim_felirat = ttk.Label(
            fo_keret,
            text="Informatikai eszköznyilvántartó",
            font=("Segoe UI", 18, "bold"),
        )
        cim_felirat.pack(anchor="w", pady=(0, 15))

        sajat_keret = ttk.LabelFrame(
            fo_keret,
            text="Saját gép adatai",
            padding=10,
        )
        sajat_keret.pack(fill="x", pady=(0, 10))

        gepnev_gomb = ttk.Button(
            sajat_keret,
            text="Saját gép adatai",
            width=22,
            command=self.jsz_gepnev_megjelenitese,
        )
        gepnev_gomb.pack(side="left", padx=(0, 15))

        self.gepnev_felirat = ttk.Label(
            sajat_keret,
            text="A számítógép adatai itt jelennek meg.",
        )
        self.gepnev_felirat.pack(side="left")

        nev_keret = ttk.LabelFrame(
            fo_keret,
            text="Keresés gépnév alapján",
            padding=10,
        )
        nev_keret.pack(fill="x", pady=(0, 10))
        nev_keret.columnconfigure(1, weight=1)

        gepnev_utmutato = ttk.Label(nev_keret, text="Gépnév:")
        gepnev_utmutato.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="w",
        )

        self.gepnev_mezo = ttk.Entry(nev_keret)
        self.gepnev_mezo.grid(
            row=0,
            column=1,
            padx=(0, 10),
            sticky="ew",
        )

        ip_kereso_gomb = ttk.Button(
            nev_keret,
            text="IPv4 cím lekérése",
            width=22,
            command=self.jsz_ip_cim_megjelenitese,
        )
        ip_kereso_gomb.grid(row=0, column=2)

        self.ip_eredmeny_felirat = ttk.Label(nev_keret, text="")
        self.ip_eredmeny_felirat.grid(
            row=1,
            column=0,
            columnspan=3,
            pady=(8, 0),
            sticky="w",
        )

        ip_keret = ttk.LabelFrame(
            fo_keret,
            text="Eszköz vizsgálata és hozzáadása",
            padding=10,
        )
        ip_keret.pack(fill="x", pady=(0, 10))
        ip_keret.columnconfigure(1, weight=1)

        ip_utmutato = ttk.Label(ip_keret, text="IPv4 cím:")
        ip_utmutato.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="w",
        )

        self.ip_mezo = ttk.Entry(ip_keret)
        self.ip_mezo.grid(row=0, column=1, sticky="ew")

        vizsgalat_gombok = ttk.Frame(ip_keret)
        vizsgalat_gombok.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(10, 0),
            sticky="w",
        )

        nev_kereso_gomb = ttk.Button(
            vizsgalat_gombok,
            text="Gépnév lekérése",
            width=22,
            command=self.jsz_ip_alapjan_gepnev_megjelenitese,
        )
        nev_kereso_gomb.pack(side="left", padx=(0, 8))

        elerhetoseg_gomb = ttk.Button(
            vizsgalat_gombok,
            text="Ping ellenőrzés",
            width=22,
            command=self.jsz_elerhetoseg_megjelenitese,
        )
        elerhetoseg_gomb.pack(side="left", padx=(0, 8))

        hozzaadas_gomb = ttk.Button(
            vizsgalat_gombok,
            text="Hozzáadás a táblázathoz",
            width=22,
            command=self.jsz_eszkoz_hozzaadasa,
        )
        hozzaadas_gomb.pack(side="left")

        self.nev_eredmeny_felirat = ttk.Label(ip_keret, text="")
        self.nev_eredmeny_felirat.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=(8, 0),
            sticky="w",
        )

        tartomany_keret = ttk.LabelFrame(
            fo_keret,
            text="Keresés IP tartományban",
            padding=10,
        )
        tartomany_keret.pack(fill="x", pady=(0, 10))
        tartomany_keret.columnconfigure(1, weight=1)
        tartomany_keret.columnconfigure(3, weight=1)

        kezdo_ip_felirat = ttk.Label(
            tartomany_keret,
            text="Kezdő IPv4 cím:",
        )
        kezdo_ip_felirat.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="w",
        )

        self.kezdo_ip_mezo = ttk.Entry(tartomany_keret)
        self.kezdo_ip_mezo.grid(
            row=0,
            column=1,
            padx=(0, 20),
            sticky="ew",
        )

        zaro_ip_felirat = ttk.Label(
            tartomany_keret,
            text="Záró IPv4 cím:",
        )
        zaro_ip_felirat.grid(
            row=0,
            column=2,
            padx=(0, 10),
            sticky="w",
        )

        self.zaro_ip_mezo = ttk.Entry(tartomany_keret)
        self.zaro_ip_mezo.grid(
            row=0,
            column=3,
            sticky="ew",
        )

        self.tartomany_gomb = ttk.Button(
            tartomany_keret,
            text="Tartomány keresése",
            width=22,
            command=self.jsz_tartomany_ellenorzese,
        )
        self.tartomany_gomb.grid(
            row=1,
            column=0,
            columnspan=4,
            pady=(10, 0),
            sticky="w",
        )

        self.elerhetoseg_felirat = ttk.Label(
            fo_keret,
            text="Adj hozzá egy eszközt vagy tölts be egy mentést!",
            anchor="w",
            font=("Segoe UI", 10, "bold"),
        )
        self.elerhetoseg_felirat.pack(
            side="bottom",
            fill="x",
            pady=(10, 0),
        )

        muvelet_keret = ttk.Frame(fo_keret)
        muvelet_keret.pack(
            side="bottom",
            fill="x",
            pady=(10, 0),
        )

        torles_gomb = ttk.Button(
            muvelet_keret,
            text="Kijelöltek törlése",
            width=22,
            command=self.jsz_eszkoz_torlese,
        )
        torles_gomb.pack(side="left", padx=(0, 8))

        mentes_gomb = ttk.Button(
            muvelet_keret,
            text="Mentés",
            width=22,
            command=self.jsz_mentes_inditasa,
        )
        mentes_gomb.pack(side="left", padx=(0, 8))

        betoltes_gomb = ttk.Button(
            muvelet_keret,
            text="Betöltés",
            width=22,
            command=self.jsz_betoltes_inditasa,
        )
        betoltes_gomb.pack(side="left")

        tablazat_keret = ttk.Frame(fo_keret)
        tablazat_keret.pack(fill="both", expand=True)
        tablazat_keret.columnconfigure(0, weight=1)
        tablazat_keret.rowconfigure(0, weight=1)

        self.eszkoz_tablazat = ttk.Treeview(
            tablazat_keret,
            columns=("gepnev", "ip_cim", "allapot"),
            show="headings",
            height=6,
        )
        self.eszkoz_tablazat.heading("gepnev", text="Gépnév")
        self.eszkoz_tablazat.heading("ip_cim", text="IPv4 cím")
        self.eszkoz_tablazat.heading("allapot", text="Állapot")

        self.eszkoz_tablazat.column("gepnev", width=300)
        self.eszkoz_tablazat.column("ip_cim", width=180)
        self.eszkoz_tablazat.column("allapot", width=280)

        self.eszkoz_tablazat.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        gorditosav = ttk.Scrollbar(
            tablazat_keret,
            orient="vertical",
            command=self.eszkoz_tablazat.yview,
        )
        gorditosav.grid(row=0, column=1, sticky="ns")

        self.eszkoz_tablazat.configure(
            yscrollcommand=gorditosav.set
        )

    def jsz_visszajelzes(self, szoveg, tipus="info"):
        szinek = {
            "siker": "#166534",
            "hiba": "#B91C1C",
            "info": "#1D4ED8",
        }

        self.elerhetoseg_felirat.config(
            text=szoveg,
            foreground=szinek[tipus],
        )

    def jsz_gepnev_megjelenitese(self):
        gep_neve = jsz_halozat.jsz_gepnev_lekerese()
        ip_cim = jsz_halozat.jsz_ip_cim_lekerese(gep_neve)

        self.gepnev_felirat.config(
            text=f"Gépnév: {gep_neve}\nNévhez feloldott IPv4: {ip_cim}"
        )

    def jsz_ip_cim_megjelenitese(self):
        gep_neve = self.gepnev_mezo.get().strip()
        self.ip_mezo.delete(0, tk.END)

        if not gep_neve:
            self.ip_eredmeny_felirat.config(
                text="Először, adj meg egy gépnevet!"
            )
            return

        ip_cim = jsz_halozat.jsz_ip_cim_lekerese(gep_neve)
        self.ip_eredmeny_felirat.config(text=f"IPv4 cim: {ip_cim}")

        if jsz_halozat.jsz_ipv4_cim_ervenyes(ip_cim):
            self.ip_mezo.insert(0, ip_cim)

    def jsz_ip_mezo_ellenorzese(self):
        ip_cim = self.ip_mezo.get().strip()

        if not ip_cim:
            self.jsz_visszajelzes(
                "Először, adj meg egy IP címet!",
                "hiba",
            )
            return None

        if not jsz_halozat.jsz_ipv4_cim_ervenyes(ip_cim):
            self.jsz_visszajelzes(
                "Érvénytelen IPv4 cím!",
                "hiba",
            )
            return None

        return ip_cim

    def jsz_ip_alapjan_gepnev_megjelenitese(self):
        self.nev_eredmeny_felirat.config(text="")
        ip_cim = self.jsz_ip_mezo_ellenorzese()

        if ip_cim is None:
            return

        gep_neve = jsz_halozat.jsz_gepnev_lekerese_ip_alapjan(ip_cim)
        self.nev_eredmeny_felirat.config(text=gep_neve)
        self.jsz_visszajelzes(
            "A névlekérés befejeződött!"
        )

    def jsz_elerhetoseg_megjelenitese(self):
        ip_cim = self.jsz_ip_mezo_ellenorzese()

        if ip_cim is None:
            return

        try:
            elerheto = jsz_halozat.jsz_elerhetoseg_ellenorzese(ip_cim)
        except OSError:
            self.jsz_visszajelzes(
                "Nem sikerült elindítani a ping parancsot!",
                "hiba",
            )
            return

        if elerheto:
            self.jsz_visszajelzes(
                "Az eszköz válaszolt a pingre.",
                "siker",
            )
        else:
            self.jsz_visszajelzes(
                "Nem érkezett válasz a pingre.",
                "hiba",
            )

    def jsz_tartomany_ellenorzese(self):
        kezdo_ip = self.kezdo_ip_mezo.get().strip()
        zaro_ip = self.zaro_ip_mezo.get().strip()

        if not kezdo_ip or not zaro_ip:
            self.jsz_visszajelzes(
                "Add meg a kezdő és záró IP címet!",
                "hiba",
            )
            return

        if (
            not jsz_halozat.jsz_ipv4_cim_ervenyes(kezdo_ip)
            or not jsz_halozat.jsz_ipv4_cim_ervenyes(zaro_ip)
        ):
            self.jsz_visszajelzes(
                "Mindkét mezőbe érvényes IPv4 címet írj!",
                "hiba",
            )
            return

        try:
            ip_cimek = jsz_halozat.jsz_ip_tartomany_letrehozasa(
                kezdo_ip,
                zaro_ip,
            )
        except ValueError as hiba:
            self.jsz_visszajelzes(str(hiba), "hiba")
            return

        self.jsz_visszajelzes(
            f"Keresés folyamatban, {len(ip_cimek)} cím vizsgálata..."
        )
        self.tartomany_gomb.config(state="disabled")
        self.kereses_eredmenye = queue.Queue()

        kereso_szal = threading.Thread(
            target=self.jsz_kereses_hatterben,
            args=(ip_cimek,),
            daemon=True,
        )
        kereso_szal.start()

        self.elerhetoseg_felirat.after(
            100,
            self.jsz_kereses_eredmenyenek_atvetele,
        )

    def jsz_eszkoz_hozzaadasa(self):
        ip_cim = self.jsz_ip_mezo_ellenorzese()

        if ip_cim is None:
            return

        for sor_azonosito in self.eszkoz_tablazat.get_children():
            tarolt_ip_cim = self.eszkoz_tablazat.set(
                sor_azonosito,
                "ip_cim",
            )

            if tarolt_ip_cim == ip_cim:
                self.jsz_visszajelzes(
                    "Ez az eszköz már szerepel a táblázatban!"
                )
                return

        gep_neve = jsz_halozat.jsz_gepnev_lekerese_ip_alapjan(ip_cim)

        try:
            elerheto = jsz_halozat.jsz_elerhetoseg_ellenorzese(ip_cim)
        except OSError:
            self.jsz_visszajelzes(
                "Nem sikerült elindítani a ping parancsot!",
                "hiba",
            )
            return

        if elerheto:
            allapot = "Válaszolt a pingre."
        else:
            allapot = "Nem érkezett válasz a pingre!"

        self.eszkoz_tablazat.insert(
            "",
            "end",
            values=(gep_neve, ip_cim, allapot),
        )

        self.jsz_visszajelzes(
            "Az eszközt hozzáadtuk a táblázathoz.",
            "siker",
        )

    def jsz_eszkoz_torlese(self):
        kijelolt_sorok = self.eszkoz_tablazat.selection()

        if not kijelolt_sorok:
            self.jsz_visszajelzes(
                "Először, jelölj ki egy eszközt a táblázatban!",
                "hiba",
            )
            return

        for sor_azonosito in kijelolt_sorok:
            self.eszkoz_tablazat.delete(sor_azonosito)

        self.jsz_visszajelzes(
            "A kijelölt sorokat töröltük a táblázatból!",
            "siker",
        )

    def jsz_mentes_inditasa(self):
        eszkozok = []

        for sor_azonosito in self.eszkoz_tablazat.get_children():
            sor_adatai = self.eszkoz_tablazat.item(
                sor_azonosito,
                "values",
            )
            eszkozok.append(sor_adatai)

        try:
            jsz_fajlkezeles.jsz_eszkozok_mentese(
                "eszkozok.json",
                eszkozok,
            )
        except OSError:
            self.jsz_visszajelzes(
                "Nem sikerült menteni a fájlt!",
                "hiba",
            )
            return

        self.jsz_visszajelzes(
            "Az eszközöket az eszkozok.json fájlba mentettük!",
            "siker",
        )

    def jsz_betoltes_inditasa(self):
        try:
            eszkozok = jsz_fajlkezeles.jsz_eszkozok_betoltese(
                "eszkozok.json",
            )
        except FileNotFoundError:
            self.jsz_visszajelzes(
                "Még nincs mentett eszkozok.json fájl.",
                "hiba",
            )
            return
        except OSError:
            self.jsz_visszajelzes(
                "Nem sikerül megnyitni a fájlt!",
                "hiba",
            )
            return
        except ValueError:
            self.jsz_visszajelzes(
                "A fájl tartalma nem olvasható JSON adatként!",
                "hiba",
            )
            return

        for sor_azonosito in self.eszkoz_tablazat.get_children():
            self.eszkoz_tablazat.delete(sor_azonosito)

        for sor_adatai in eszkozok:
            self.eszkoz_tablazat.insert(
                "",
                "end",
                values=sor_adatai,
            )

        self.jsz_visszajelzes(
            "Betöltöttük a mentett adatokat és korábbi állapotokat!",
            "siker",
        )

    def jsz_kereses_hatterben(self, ip_cimek):
        try:
            eszkozok = jsz_halozat.jsz_tartomany_vizsgalata(ip_cimek)
        except OSError as hiba:
            self.kereses_eredmenye.put((None, str(hiba)))
        else:
            self.kereses_eredmenye.put((eszkozok, None))

    def jsz_kereses_eredmenyenek_atvetele(self):
        try:
            eszkozok, hiba = self.kereses_eredmenye.get_nowait()
        except queue.Empty:
            self.elerhetoseg_felirat.after(
                100,
                self.jsz_kereses_eredmenyenek_atvetele,
            )
            return

        self.tartomany_gomb.config(state="normal")

        if hiba is not None:
            self.jsz_visszajelzes(
                f"A keresés nem sikerült: {hiba}",
                "hiba",
            )
            return

        tarolt_ip_cimek = []

        for sor_azonosito in self.eszkoz_tablazat.get_children():
            ip_cim = self.eszkoz_tablazat.set(
                sor_azonosito,
                "ip_cim",
            )
            tarolt_ip_cimek.append(ip_cim)

        uj_eszkozok_szama = 0

        for eszkoz in eszkozok:
            ip_cim = eszkoz[1]

            if ip_cim not in tarolt_ip_cimek:
                self.eszkoz_tablazat.insert(
                    "",
                    "end",
                    values=eszkoz,
                )
                tarolt_ip_cimek.append(ip_cim)
                uj_eszkozok_szama += 1

        self.jsz_visszajelzes(
            f"Keresés kész! Válaszoló eszközök: {len(eszkozok)}  "
            f"Újonnan hozzáadva: {uj_eszkozok_szama}",
            "siker",
        )


root = tk.Tk()
app = JszEszkozNyilvantarto(root)

root.mainloop()