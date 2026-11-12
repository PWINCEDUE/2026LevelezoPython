import tkinter as tk

import jsz_halozat


class JszEszkozNyilvantarto:
    def __init__(self, alapablak):
        alapablak.title("Informatikai eszköznyilvántartó")
        alapablak.geometry("900x500")

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
                text="Először adj meg egy gépnevet!"
            )
            return

        ip_cim = jsz_halozat.jsz_ip_cim_lekerese(gep_neve)
        self.ip_eredmeny_felirat.config(text=f"IPv4-cím: {ip_cim}")

root = tk.Tk()
app = JszEszkozNyilvantarto(root)

root.mainloop()