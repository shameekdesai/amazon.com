from bs4 import BeautifulSoup
import requests


def scraping(urll):
    page = requests.get(urll).content
    soup = BeautifulSoup(page,features="html.parser")
    print(soup.title)

    price=soup.find(id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
    price_val = price.get_text()
    print(price_val)

url1='https://www.amazon.in/Kenstar-Little-Dx-12-Litre-Cooler/dp/B00ILEAER6/ref=sr_1_1?dchild=1&keywords=kenstar+little+cooler&qid=1608318980&sr=8-'
url2='https://www.amazon.in/Symphony-Diet-12-Litre-Cooler/dp/B00IYD419Q/ref=pd_vtp_1?pd_rd_w=Aol9Z&pf_rd_p=ae892142-84f6-4198-a069-93775ca49eb0&pf_rd_r=AZFX0D07T0Q7JKTHBSN9&pd_rd_r=b0d40a94-090f-4589-bd8f-4c4032a99838&pd_rd_wg=4OYn9&pd_rd_i=B00IYD419Q&psc=1'

scraping(url1)
scraping(url2)


