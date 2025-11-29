import argparse
import requests
import colorama
from time import sleep

colorama.init(autoreset=False)

def p(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

print()
p(colorama.Fore.LIGHTMAGENTA_EX + '\n🐉=🐉=🐉=🐉 DRAGON VERIFICATION ON 🐉=🐉=🐉=🐉' + colorama.Style.RESET_ALL, delay=0.03)
p(colorama.Fore.LIGHTGREEN_EX + '"✅" = URL ONLINE' + colorama.Style.RESET_ALL, delay=0.03)
p(colorama.Fore.LIGHTRED_EX + '"❌" = URL OFFLINE\n' + colorama.Style.RESET_ALL, delay=0.03)
p(' ', delay=1.0)

parser = argparse.ArgumentParser(
    description=colorama.Fore.LIGHTBLUE_EX + '\n=🐉=🐉=🐉=🐉 Verificador de sites =🐉=🐉=🐉=🐉\n' + colorama.Style.RESET_ALL
)
parser.add_argument('--url', required=True)

try:
    args = parser.parse_args()
except SystemExit as e:
    if e.code != 0:
        p(colorama.Fore.LIGHTRED_EX + '\n=🐉=🐉=🐉=🐉 Erro: Você precisa informar uma URL após "--url". =🐉=🐉=🐉=🐉\n' + colorama.Style.RESET_ALL)
    exit()

loading_text = colorama.Fore.LIGHTYELLOW_EX + "..."
print(loading_text + colorama.Style.RESET_ALL, end='\r', flush=True)
sleep(2)
print()

try:
    response = requests.get(args.url, timeout=5)

    if response.status_code == 200:
        p(colorama.Fore.LIGHTGREEN_EX + f'\n=🐉=🐉=🐉=🐉 SITE -> "{args.url}", STATUS -> ✅ =🐉=🐉=🐉=🐉\n' + colorama.Style.RESET_ALL)
    else:
        p(colorama.Fore.LIGHTRED_EX + f'\n=🐉=🐉=🐉=🐉 SITE -> "{args.url}", STATUS -> ❌ =🐉=🐉=🐉=🐉\n' + colorama.Style.RESET_ALL)

except requests.exceptions.RequestException:
    p(colorama.Fore.LIGHTRED_EX + f'\n=🐉=🐉=🐉=🐉 SITE -> "{args.url}", STATUS -> ❌ =🐉=🐉=🐉=🐉\n' + colorama.Style.RESET_ALL)
