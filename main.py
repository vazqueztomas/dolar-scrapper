import requests
from bs4 import BeautifulSoup
from termcolor import colored
import typer

URL = "https://dolarhoy.com/"


class DolarScrapper:
    def __init__(self, url) -> None:
        self.url = url

    def scrape_dolar_values(self) -> int:
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        dolar_values = soup.find_all("div", class_="val")
        compra = int(dolar_values[0].get_text()[1:])
        venta = int(dolar_values[1].get_text()[1:])
        return compra, venta

    def print_dolar_message(self, number1: int, number2: int) -> str:
        return f"""
            Gracias por utilizar este scrapper.
            Los valores actuales del dolar blue son:
            Compra: ${colored(number1, "green", "on_black")}
            Venta: ${colored(number2, "red", "on_black")}

            El {colored("promedio", "blue", "on_black")} de estos valores es: {colored(f"${(number1 + number2) / 2}", "blue", "on_black")}
        """


def welcome_message() -> str:
    return f"""
        {colored("Bienvenido!", "yellow", "on_black", attrs=["bold"])}
        Este programa te permite obtener los valores actuales de varias monedas en Argentina
    """


def main() -> None:
    print(welcome_message())
    scraper = DolarScrapper(URL)
    compra, venta = scraper.scrape_dolar_values()
    print(scraper.print_dolar_message(compra, venta))


if __name__ == "__main__":
    typer.run(main)
