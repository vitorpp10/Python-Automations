import requests
from bs4 import BeautifulSoup
from time import sleep
import sys
from colorama import Fore, Style
import os

URL = 'http://quotes.toscrape.com/'
NEXT_PAGE = None

def p(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_scraper(url):
    global NEXT_PAGE
    try:
        print()
        p(f'Acessando página {Fore.LIGHTGREEN_EX}{Style.BRIGHT}{url}{Style.RESET_ALL}', delay=0.02)
        p('...', delay=1.0)
        
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        parsed_html = BeautifulSoup(response.text, 'html.parser')

        all_quotes = parsed_html.find_all('div', class_='quote')
        next_button = parsed_html.find('li', class_='next')

        if next_button:
            NEXT_PAGE = next_button.find('a')['href']
        else:
            NEXT_PAGE = None
        
        return all_quotes

    except requests.exceptions.RequestException as e:
        p(f'{Fore.LIGHTRED_EX}{Style.BRIGHT}🐉=🐉=🐉= ERRO: {Style.RESET_ALL}{Style.BRIGHT}Não foi possivel acessar o site {Style.RESET_ALL}{Fore.LIGHTRED_EX}{Style.BRIGHT}🐉=🐉=🐉={Style.RESET_ALL}')
        print(f'{Fore.LIGHTBLACK_EX}\nDetalhes >>> {e}\n{Style.RESET_ALL}')
        sys.exit()
    except Exception as e:
        p(f'{Fore.LIGHTRED_EX}{Style.BRIGHT}🐉=🐉=🐉 ERRO: {Style.RESET_ALL}{Style.BRIGHT}Erro inesperado. {Style.RESET_ALL}{Fore.LIGHTRED_EX}{Style.BRIGHT}🐉=🐉=🐉{Style.RESET_ALL}')
        sys.exit()

clear()
p(f'{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}🐉=🐉=🐉= DRAGON FIND QUOTES 🐉=🐉=🐉={Style.RESET_ALL}', delay=0.015)
p(f'{Fore.LIGHTMAGENTA_EX}find quotes in {Style.RESET_ALL}{Style.BRIGHT}"http://quotes.toscrape.com/"{Style.RESET_ALL}', delay=0.015)
p('\n ', delay=1.0)

all_ = main_scraper(URL)

if not all_:
    p(f'{Fore.LIGHTRED_EX}{Style.BRIGHT}🐉=🐉=🐉= ERRO: {Style.RESET_ALL}{Style.BRIGHT}Nenhuma citação encontrada em {Fore.LIGHTGREEN_EX}{URL}{Style.RESET_ALL}. {Fore.LIGHTRED_EX}{Style.BRIGHT}🐉=🐉=🐉={Style.RESET_ALL}')
    sys.exit()

should_refresh = True

while True:
    if should_refresh:
        clear()
        p(f'{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}🐉=🐉=🐉 CITAÇÕES DA PÁGINA: {Style.RESET_ALL}{Style.BRIGHT}{URL}{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT} 🐉=🐉=🐉{Style.RESET_ALL}', delay=0.01)
        p(f'Foram encontrados {Fore.LIGHTGREEN_EX}{Style.BRIGHT}{len(all_)}{Style.RESET_ALL} citações.\n', delay=0.01)

        for i, bloco in enumerate(all_):
            text_quote = bloco.find('span', class_='text').text
            text_menu = text_quote.strip().replace('“', '').replace('”', '')[:120] + '...'
            p(f'{Fore.LIGHTGREEN_EX}{i + 1}{Style.RESET_ALL} - {text_menu}', delay=0.005)

        menu_options = [
            f'{Fore.LIGHTCYAN_EX}{Style.BRIGHT}Digite o número da citação{Style.RESET_ALL} ({Fore.LIGHTGREEN_EX}{Style.BRIGHT}1 a {len(all_)}{Style.RESET_ALL})',
            f'{Fore.LIGHTCYAN_EX}{Style.BRIGHT}N {Style.RESET_ALL}({Fore.LIGHTGREEN_EX}{Style.BRIGHT}ou Próximo{Style.RESET_ALL}) {Fore.LIGHTCYAN_EX}{Style.BRIGHT}para a próxima página. {Style.RESET_ALL}' if NEXT_PAGE else f'{Fore.YELLOW}{Style.BRIGHT}Fim: Última página alcançada.{Style.RESET_ALL}',
            f'{Fore.LIGHTCYAN_EX}{Style.BRIGHT}0: Sair do programa. {Style.RESET_ALL}'
        ]
        
        print()
        print(f'{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}🐉=🐉=🐉 MENU: 🐉=🐉=🐉{Style.RESET_ALL}')
        for option in menu_options:
            p(f'{Fore.LIGHTGREEN_EX}{Style.BRIGHT}> {Style.RESET_ALL}{Style.BRIGHT}{option}{Style.RESET_ALL}', delay=0.01)

    should_refresh = False

    try:
        print()
        p(f'{Fore.LIGHTGREEN_EX}{Style.BRIGHT}👇 {Style.RESET_ALL}', delay=0.01)
        choice_input = sys.stdin.readline().strip().lower()
    except:
        sys.exit()
    
    if choice_input == '0':
        print()
        p(f'{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}🐉=🐉=🐉= Obrigado por usar o Dragon Quotes! 🐉=🐉=🐉={Style.RESET_ALL}')
        p('\n...', delay=2)
        
        break
    
    elif choice_input in ['n', 'proximo', 'proxima', 'próximo', 'próxima']:
        if NEXT_PAGE:
            print()
            p(f'{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}🐉=🐉=🐉= PRÓXIMA PÁGINA 🐉=🐉=🐉={Style.RESET_ALL}', delay=0.02)
            URL = 'http://quotes.toscrape.com' + NEXT_PAGE
            all_ = main_scraper(URL)
            should_refresh = True
            continue
        else:
            p(f'{Fore.LIGHTRED_EX}{Style.BRIGHT}🐉=🐉=🐉= {Style.RESET_ALL}FIM DAS PÁGINAS. {Fore.LIGHTRED_EX}{Style.BRIGHT}🐉=🐉=🐉={Style.RESET_ALL}')
            continue
            
    else:
        try:
            choice_num = int(choice_input)
            
            if 1 <= choice_num <= len(all_):
                clear()
                quote_chosen = all_[choice_num - 1]

                final_text = quote_chosen.find('span', class_='text').text
                final_author = quote_chosen.find('small', class_='author').text

                print(f'\n{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}🐉=🐉=🐉= CITAÇÃO ESCOLHIDA {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}({choice_num}) {Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}🐉=🐉=🐉={Style.RESET_ALL}')
                print()
                print(f'{Style.BRIGHT}{final_text}{Style.RESET_ALL}')
                print(f'\n{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Autor: {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}{final_author}{Style.RESET_ALL}')
                print(f'\n{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}🐉=🐉=🐉= ------------------------------------------- 🐉=🐉=🐉={Style.RESET_ALL}')

                print()
                p(f'{Fore.LIGHTBLACK_EX}{Style.BRIGHT}Pressione ENTER para voltar ao menu...{Style.RESET_ALL}')
                sys.stdin.readline()
                should_refresh = True
            else:
                p(f'{Fore.LIGHTRED_EX}{Style.BRIGHT}🐉=🐉=🐉= ERRO: {Style.RESET_ALL}{Style.BRIGHT}Número inválido. Escolha entre 1 e {len(all_)}. {Style.RESET_ALL}{Fore.LIGHTRED_EX}{Style.BRIGHT}🐉=🐉=🐉={Style.RESET_ALL}')
                
        except ValueError:
            p(f'{Fore.LIGHTRED_EX}{Style.BRIGHT}ERRO: {Style.RESET_ALL}{Style.BRIGHT}Entrada inválida, digite uma opção válida.{Style.RESET_ALL}')
