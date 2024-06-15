import requests
from bs4 import BeautifulSoup
import time
import csv
from random import randint

index = 1
file = open("wine.csv", "w",encoding='utf-8_sig', newline="\n")
write = csv.writer(file)
write.writerow(["Title", "release_date", "Manufacturer"])


while index < 10:
    
    url = f"https://winegallery.ge/ka/production?page={index}"
    resp = requests.get(url)
    print("Status code: ", resp.status_code)
    html = resp.text
    full_soup = BeautifulSoup(html, "html.parser")
    wine_section = full_soup.find("div", class_="row products-list-inner shop-gallery-carousel")
    all_wines = wine_section.find_all("div", class_="col-md-6 col-sm-6 col-xs-12 shop-product-2-wrapper")
    for wine in all_wines:
        info = wine.find("div", class_="info")
        title = info.find("a").text
        release_date = info.find("span").text
        manufacturer = info.find("p", class_="product-manufacturer-newd").text
        write.writerow([title, release_date, manufacturer])
        print(title, release_date, manufacturer)
    index += 1
    time.sleep(randint(15, 20))
    
    
    
    