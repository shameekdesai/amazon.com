import BeautifulSoup
import requests


class Crawler:
    def __int__(self):
        pass

    def scraping(self,urll):
        page = requests.get(urll).content
        soup = BeautifulSoup(page,features="html.parser")
        print(soup.title)

        price=soup.find(id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
        price_val = price.get_text()
        print(price_val)


with open("links.txt",'r') as f:
    li=f.readlines()
    for i in li:
        scraping(i)


