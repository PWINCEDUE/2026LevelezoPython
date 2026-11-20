import ipaddress
import socket
import subprocess


def jsz_gepnev_lekerese():
    gep_neve = socket.gethostname()
    return gep_neve


def jsz_ip_cim_lekerese(gep_neve):
    try:
        ip_cim = socket.gethostbyname(gep_neve)
        return ip_cim
    except socket.gaierror:
        return "Nem sikerült lekérni!"


def jsz_gepnev_lekerese_ip_alapjan(ip_cim):
    try:
        eredmeny = socket.gethostbyaddr(ip_cim)
        return eredmeny[0]
    except OSError:
        return "Nem sikerült a nevet lekérni!"


def jsz_elerhetoseg_ellenorzese(ip_cim):
    eredmeny = subprocess.run(
        ["ping", "-4", "-n", "1", "-w", "1000", ip_cim],
        capture_output=True,
        text=True,
        errors="replace",
    )

    return "ttl=" in eredmeny.stdout.lower()


def jsz_ipv4_cim_ervenyes(ip_cim):
    try:
        ipaddress.IPv4Address(ip_cim)
        return True
    except ipaddress.AddressValueError:
        return False


def jsz_ip_tartomany_letrehozasa(kezdo_ip, zaro_ip):
    kezdo_cim = ipaddress.IPv4Address(kezdo_ip)
    zaro_cim = ipaddress.IPv4Address(zaro_ip)

    if int(kezdo_cim) > int(zaro_cim):
        raise ValueError("A kezdő IP cím nem lehet nagyobb a zárónál!")

    cim_darabszam = int(zaro_cim) - int(kezdo_cim) + 1

    if cim_darabszam > 256:
        raise ValueError("Egyszerre legfeljebb 256 IP cím vizsgálható!")

    ip_cimek = []

    for cim_szama in range(int(kezdo_cim), int(zaro_cim) + 1):
        ip_cim = str(ipaddress.IPv4Address(cim_szama))
        ip_cimek.append(ip_cim)

    return ip_cimek


def jsz_tartomany_vizsgalata(ip_cimek):
    talalt_eszkozok = []

    for ip_cim in ip_cimek:
        elerheto = jsz_elerhetoseg_ellenorzese(ip_cim)

        if elerheto:
            gep_neve = jsz_gepnev_lekerese_ip_alapjan(ip_cim)

            eszkoz = (
                gep_neve,
                ip_cim,
                "Válaszolt a pingre!",
            )
            talalt_eszkozok.append(eszkoz)

    return talalt_eszkozok