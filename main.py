from bs4 import BeautifulSoup
import requests
import readandwrite

class Scraper:
    def __init__(self):
        pass

    def scraping(self,url):
        page = requests.get(url).content
        soup = BeautifulSoup(page,features="html.parser")
        print(soup.title)
        try:
            price = soup.find(id='priceblock_ourprice', class_="a-size-medium a-color-price priceBlockBuyingPriceString").get_text().strip()

        except:
            price = ''
        
        print(price)





if __name__ == "__main__":
    scrap = Scraper()
    '''
    exe = readandwrite.Excel()  #creating instance of readandwrite Excel class for accessing urls
    url = exe.readlink()
    '''
    url1 ='https://www.amazon.in/Voltas-JetMax-54L-Desert-Cooler/dp/B084GSF7CD'
    url2 = 'https://www.amazon.in/Bajaj-PCF-25DLX-Cooler-White/dp/B01N6ZUGG6/ref=pd_sbs_79_4/257-8552006-8943651?_encoding=UTF8&pd_rd_i=B01N6ZUGG6&pd_rd_r=39ff52dc-625c-44fe-8c4f-c7084b51e7be&pd_rd_w=9dsw1&pd_rd_wg=syZI4&pf_rd_p=758bfbc8-a8f2-4456-bf65-ae5d502eac06&pf_rd_r=RQT1FGBFE6ZZTHAXAJYJ&psc=1&refRID=RQT1FGBFE6ZZTHAXAJYJ'
    
    scrap.scraping(url1)
    scrap.scraping(url2)



