# Dragon Find Quotes 🐉

![PYTHON-3.x](https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTTP-requests](https://img.shields.io/badge/HTTP-requests-FF6C37?style=for-the-badge)
![PARSING-BeautifulSoup](https://img.shields.io/badge/PARSING-BeautifulSoup-4B8BBE?style=for-the-badge)
![CLI_UX-Colorama](https://img.shields.io/badge/CLI_UX-Colorama-e01e5a?style=for-the-badge)

Este projeto é uma ferramenta interativa de linha de comando (CLI) que faz scraping de citações do site `http://quotes.toscrape.com/`.  
Ele combina lógica de web scraping com um tema estilizado de "Dragão", oferecendo paginação e tratamento de erros. [web:1]

## Arquivos

- `dragon_quotes.py`  
  Script Python principal. Ele lida com as requisições HTTP, parsing do HTML e o loop interativo que exibe o menu, trata a entrada do usuário e gerencia a navegação entre páginas.

## `dragon_quotes.py` (lógica central)

def main_scraper(url):
global NEXT_PAGE
try:
response = requests.get(url, timeout=5)
response.raise_for_status()
parsed_html = BeautifulSoup(response.text, 'html.parser')

text
    all_quotes = parsed_html.find_all('div', class_='quote')
    next_button = parsed_html.find('li', class_='next')

    if next_button:
        NEXT_PAGE = next_button.find('a')['href']
    else:
        NEXT_PAGE = None
    
    return all_quotes
except Exception as e:
    sys.exit()
text

## O que o script faz

- Envia requisições GET para `http://quotes.toscrape.com/` usando a biblioteca `requests`.
- Faz o parsing da resposta HTML usando `BeautifulSoup` para extrair o texto das citações, autores e links de paginação. [web:5]
- Implementa um sistema de navegação paginada, permitindo que o usuário vá para a "Próxima Página" diretamente pelo terminal.
- Possui uma UX robusta no CLI usando `colorama` para cores, efeitos de digitação (função `p()`) e limpeza condicional da tela.
- Trata erros de forma graciosa, garantindo que a aplicação não quebre com entradas inválidas ou problemas de conexão.

## Possíveis extensões

Você pode estender este script para incluir, por exemplo:

- Salvamento de citações favoritas em um banco de dados (SQLite).
- Filtro de citações por tags específicas.

## Instalação

Se você está configurando este projeto pela primeira vez, instale as bibliotecas necessárias:

pip install requests beautifulsoup4 colorama

text

---

![Made_with_heart](https://img.shields.io/badge/Made_with❤️_by-Vitor_de_Padua-blueviolet?style=for-the-badge)
