"""
import requests
from bs4 import BeautifulSoup

url = 'https://www.vatanbilgisayar.com/cep-telefonu-modelleri/'

def check_price():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    # fiyatı sayfadan çek!

    price = soup.find(id = 'list__price')

    if price is not None:
        converted_price = float(price.get_text()[1:])
        print(f"ürün fiyatı: {converted_price}")
    else:
        print("fiyat bilgisi mevcut değildir...")
    

check_price
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.vatanbilgisayar.com/cep-telefonu-modelleri/'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

phone_prices = soup.find_all('span', {'class': 'product-list__price'})



with open('telefon_fiyatlari.txt', 'w', encoding='utf-8') as f:
    for price in phone_prices:
        f.write(price.text.strip() + '\n')
        converted_price = float(price.get_text()[1:].replace(".", "").replace(",", "."))
        print(f"ürün fiyatı: {converted_price}")
    if price is not None:
        converted_price = float(price.get_text()[1:])
        print(f"ürün fiyatı: {converted_price}")
    else:
        print("fiyat bilgisi mevcut değildir...")
    









        




