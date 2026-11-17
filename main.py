import tkinter as tk

from tkinter import ttk

import jsz_halozat


class JszEszkozNyilvantarto:
    def __init__(self, alapablak):
        alapablak.title("Informatikai eszköznyilvántartó")
        alapablak.geometry("900x700")

        self.gepnev_felirat = tk.Label(
            alapablak,
            text="A számítógép neve itt jelenik meg.",
        )
        self.gepnev_felirat.pack(pady=20)

        gepnev_gomb = tk.Button(
            alapablak,
            text="Saját gép nevének lekérése",
            command=self.jsz_gepnev_megjelenitese,
        )
        gepnev_gomb.pack()
        gepnev_utmutato = tk.Label(
            alapablak,
            text="Add meg a keresett számítógép nevét:",
        )
        gepnev_utmutato.pack(pady=(20, 5))

        self.gepnev_mezo = tk.Entry(alapablak, width=35)
        self.gepnev_mezo.pack()

        ip_kereso_gomb = tk.Button(
            alapablak,
            text="IPv4-cím lekérése",
            command=self.jsz_ip_cim_megjelenitese,
        )
        ip_kereso_gomb.pack(pady=10)

        self.ip_eredmeny_felirat = tk.Label(alapablak, text="")
        self.ip_eredmeny_felirat.pack()

        ip_utmutato = tk.Label(
            alapablak,
            text="Add meg a keresett eszköz IPv4 címét:",
        )
        ip_utmutato.pack(pady=(20, 5))

        self.ip_mezo = tk.Entry(alapablak, width=35)
        self.ip_mezo.pack()

        nev_kereso_gomb = tk.Button(
            alapablak,
            text="Gépnév lekérése IP cím alapján",
            command=self.jsz_ip_alapjan_gepnev_megjelenitese,
        )
        nev_kereso_gomb.pack(pady=10)

        self.nev_eredmeny_felirat = tk.Label(alapablak, text="")
        self.nev_eredmeny_felirat.pack()

        elerhetoseg_gomb = tk.Button(
            alapablak,
            text="Elérhetőség ellenőrzése",
            command=self.jsz_elerhetoseg_megjelenitese,
        )
        elerhetoseg_gomb.pack(pady=10)

        self.elerhetoseg_felirat = tk.Label(alapablak, text="")
        self.elerhetoseg_felirat.pack()
        hozzaadas_gomb = tk.Button(
            alapablak,
            text="Eszköz hozzáadása IP cím alapján",
            command=self.jsz_eszkoz_hozzaadasa,
        )
        hozzaadas_gomb.pack(pady=10)

        torles_gomb = tk.Button(
            alapablak,
            text="Kijelölt eszköz törlése.",
            command=self.jsz_eszkoz_torlese,
        )
        torles_gomb.pack(pady=5)

        self.eszkoz_tablazat = ttk.Treeview(
            alapablak,
            columns=("gepnev", "ip_cim", "allapot"),
            show="headings",
            height=5,
        )
        self.eszkoz_tablazat.heading("gepnev", text="Gépnév")
        self.eszkoz_tablazat.heading("ip_cim", text="IPv4 cím")
        self.eszkoz_tablazat.heading("allapot", text="Állapot")

        self.eszkoz_tablazat.column("gepnev", width=250)
        self.eszkoz_tablazat.column("ip_cim", width=180)
        self.eszkoz_tablazat.column("allapot", width=250)

        self.eszkoz_tablazat.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True,
        )

    def jsz_gepnev_megjelenitese(self):
        gep_neve = jsz_halozat.jsz_gepnev_lekerese()
        ip_cim = jsz_halozat.jsz_ip_cim_lekerese(gep_neve)

        self.gepnev_felirat.config(
            text=f"Gépnév: {gep_neve}\nIPv4-cím: {ip_cim}"
        )

    def jsz_ip_cim_megjelenitese(self):
        gep_neve = self.gepnev_mezo.get().strip()

        if not gep_neve:
            self.ip_eredmeny_felirat.config(
                text="Először, adj meg egy gépnevet!"
            )
            return

        ip_cim = jsz_halozat.jsz_ip_cim_lekerese(gep_neve)
        self.ip_eredmeny_felirat.config(text=f"IPv4 cím: {ip_cim}")

        self.ip_mezo.delete(0, tk.END)

        if jsz_halozat.jsz_ipv4_cim_ervenyes(ip_cim):
            self.ip_mezo.insert(0, ip_cim)

    def jsz_ip_alapjan_gepnev_megjelenitese(self):
        ip_cim = self.ip_mezo.get().strip()

        if not ip_cim:
            self.nev_eredmeny_felirat.config(
                text="Először, adj meg egy IP címet!"
            )
            return

        if not jsz_halozat.jsz_ipv4_cim_ervenyes(ip_cim):
            self.nev_eredmeny_felirat.config(
                text="Érvénytelen IPv4 cím!"
            )
            return

        gep_neve = jsz_halozat.jsz_gepnev_lekerese_ip_alapjan(ip_cim)
        self.nev_eredmeny_felirat.config(text=gep_neve)

    def jsz_elerhetoseg_megjelenitese(self):
        ip_cim = self.ip_mezo.get().strip()

        if not ip_cim:
            self.elerhetoseg_felirat.config(
                text="Először, adj meg egy IP címet!"
            )
            return

        if not jsz_halozat.jsz_ipv4_cim_ervenyes(ip_cim):
            self.elerhetoseg_felirat.config(
                text="Érvénytelen IPv4 cím!"
            )
            return

        elerheto = jsz_halozat.jsz_elerhetoseg_ellenorzese(ip_cim)

        if elerheto:
            self.elerhetoseg_felirat.config(
                text="Az eszköz válaszolt a pingre."
            )
        else:
            self.elerhetoseg_felirat.config(
                text="Nem érkezett válasz a pingre."
            )

    def jsz_eszkoz_hozzaadasa(self):
        ip_cim = self.ip_mezo.get().strip()

        if not ip_cim:
            self.elerhetoseg_felirat.config(
                text="Először, adj meg egy IP címet!"
            )
            return

        if not jsz_halozat.jsz_ipv4_cim_ervenyes(ip_cim):
            self.elerhetoseg_felirat.config(
                text="Érvénytelen IPv4 cím!"
            )
            return
        for sor_azonosito in self.eszkoz_tablazat.get_children():
            tarolt_ip_cim = self.eszkoz_tablazat.set(
                sor_azonosito,
                "ip_cim",
            )

            if tarolt_ip_cim == ip_cim:
                self.elerhetoseg_felirat.config(
                    text="Ez az IP cím már szerepel a táblázatban."
                )
                return

        gep_neve = jsz_halozat.jsz_gepnev_lekerese_ip_alapjan(ip_cim)
        elerheto = jsz_halozat.jsz_elerhetoseg_ellenorzese(ip_cim)

        if elerheto:
            allapot = "Válaszolt a pingre."
        else:
            allapot = "Nincs érkezett válasz a pingre."

        self.eszkoz_tablazat.insert(
            "",
            "end",
            values=(gep_neve, ip_cim, allapot),
        )

        self.elerhetoseg_felirat.config(
            text="Az eszközt hozzáadtuk a táblázathoz."
        )

    def jsz_eszkoz_torlese(self):
        kijelolt_sorok = self.eszkoz_tablazat.selection()

        if not kijelolt_sorok:
            self.elerhetoseg_felirat.config(
                text="Először, jelölj ki egy eszközt a táblázatban!"
            )
            return

        for sor_azonosito in kijelolt_sorok:
            self.eszkoz_tablazat.delete(sor_azonosito)

        self.elerhetoseg_felirat.config(
            text="A kijelölt sorokat töröltük a táblázatból!"
        )

root = tk.Tk()
app = JszEszkozNyilvantarto(root)

root.mainloop()