# phonefoga_0xgolip.py
import requests
from colorama import Fore, Style

def banner():
    print(Fore.RED + """
██████╗ ██╗      ██████╗ ██╗██████╗ 
██╔══██╗██║     ██╔═══██╗██║██╔══██╗
██████╔╝██║     ██║   ██║██║██║  ██║
██╔═══╝ ██║     ██║   ██║██║██║  ██║
██║     ███████╗╚██████╔╝██║██████╔╝
╚═╝     ╚══════╝ ╚═════╝ ╚═╝╚═════╝ 
        PhoneFoga OSINT v1.0
        by 0xGolip-Team
""" + Style.RESET_ALL)

def lookup_number(number):
    print(Fore.YELLOW + "[*] Mencari data nomor..." + Style.RESET_ALL)
    
    number = number.replace(" ", "").replace("-", "")
    api_key = "9f9d4b6196784ba185c6d7e9b5b03b3b"
    url = f"https://phonevalidation.abstractapi.com/v1/?api_key={api_key}&phone={number}"

    try:
        response = requests.get(url)
        data = response.json()

        if 'valid' in data:
            print(Fore.GREEN + f"""
[+] Nomor Valid: {data['valid']}
[+] Negara: {data['country']['name']}
[+] Lokasi: {data.get('location', 'Tidak diketahui')}
[+] Operator: {data.get('carrier', 'Tidak diketahui')}
[+] Jalur: {data.get('type', 'Tidak diketahui')}
[+] Format Internasional: {data['format']['international']}
""" + Style.RESET_ALL)
        else:
            print(Fore.RED + "[!] Gagal mengambil data. Cek API key atau format nomor." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"[!] Error: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    banner()
    number = input(Fore.CYAN + "[?] Masukkan Nomor HP (cth: +6281xxxxxx): " + Style.RESET_ALL)
    lookup_number(number)
