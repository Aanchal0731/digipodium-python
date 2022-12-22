import requests
import pandas as pd
from bs4 import BeautifulSoup

def get(url):
    page = request.get(url)
    if page.status_code == 200:
        return BeautifulSoup(page.text, 'lxml')
    else:
        print('Error:' , page.status_code)
        return None
    
def extract(soup):
    target = soup.find('div', class_='_1YokD2 _eMn1Gg')
    products = target.find_all('div', class_='_1AtVbE col-12-12')
    print("products: ", len(products))
    info = []
    for item in product

def save(data):
    if len(data) > 0:
        pd.DataFrame(data).to_csv('flipcart.csv' , index = False)
    else:
        print('No data to save')
    pass

def main()
pass
