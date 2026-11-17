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
        return  True
    except ipaddress.AddressValueError:
        return False