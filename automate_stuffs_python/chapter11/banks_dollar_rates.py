import requests
import bs4


def get_popular_dollar_rates():

    def extract_value(input_element):
        value = None
        if type(input_element) == list and len(input_element) > 0:
          value = input_element[0].get("value")
        return value

    main_page = requests.get("https://www.popularenlinea.com/personas/Paginas/Home.aspx")
    scapper = bs4.BeautifulSoup(main_page.text)

    purchase_input = scapper.select("#compra_peso_dolar_desktop")
    dollar_purchase_rate = extract_value(purchase_input)

    sell_input = scapper.select("#venta_peso_dolar_desktop")
    dollar_sell_rate = extract_value(sell_input)

    return dollar_purchase_rate,dollar_sell_rate


def get_reservas_dollar_rates():

    banreservas_main_page = requests.get("https://www.banreservas.com/")
    scrapper = bs4.BeautifulSoup(banreservas_main_page.text)

    purchase_element = scrapper.select(".currency-nav .first span")
    sell_element = scrapper.select(".currency-nav .last span")

    print(purchase_element)
    print(sell_element)

def get_bhd_dollar_rates():
    pass

def get_banco_central_dollar_rates():
    pass

if __name__ == "__main__":

    get_reservas_dollar_rates()