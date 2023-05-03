
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
    









        




