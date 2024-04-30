import requests
from bs4 import BeautifulSoup

class DolarScrapper:
    def __init__(self,url) -> None:
        self.url = url

    def scrape_dolar_values(self) -> int:
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        dolar_values = soup.find_all("div", class_="val")
        compra = int(dolar_values[0].get_text()[1:])
        venta = int(dolar_values[1].get_text()[1:])
        return compra, venta

    def find_middle_number(self, number1:int, number2: int) -> int:
        promedio = (number1 + number2) // 2
        print(f'El promedio de compra ${number1} y venta ${number2} es: ${promedio}')
        return promedio

URL = "https://dolarhoy.com/"
scraper = DolarScrapper(URL)

compra,venta = scraper.scrape_dolar_values()

promedio = scraper.find_middle_number(compra, venta)

