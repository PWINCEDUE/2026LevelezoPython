import socket


def jsz_gepnev_lekerese():
    gep_neve = socket.gethostname()
    return gep_neve


def jsz_ip_cim_lekerese(gep_neve):
    try:
        ip_cim = socket.gethostbyname(gep_neve)
        return ip_cim
    except socket.gaierror:
        return "Nem sikerült lekérni!"