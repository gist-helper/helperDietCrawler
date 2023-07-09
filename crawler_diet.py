import os
from time import sleep
import requests
from bs4 import BeautifulSoup as bs

def sleepCrawler(msg):
    # for avoid block ip! 
    print("------------------------------------")
    print("for avoid block ip!")
    print(msg)
    sleep(10)
    print("------------------------------------")

def getDietImg(url, bldgType, langType):
    sleepCrawler("Initialize Crawler...")
    webpage = requests.get(url)
    webpageHtml = bs(webpage.content, "html.parser")
    mealDiv = webpageHtml.find('div', class_ = 'bd_item_box')
    mealHref = mealDiv.find('a').get("href")
    mealNum = mealHref.split("=")[-1]
    mealSrc = url + "?mode=IMG&no={}&file_id=".format(mealNum)
    
    print()
    print("Image Src: ")
    print(mealSrc)
    print()

    sleepCrawler("Request Image...")
    mealImg = requests.get(mealSrc).content
    imgPath = os.path.join("img", str(bldgType) + '_' + str(langType) + '.jpg')
    with open(imgPath, 'wb') as imgFile:
        imgFile.write(mealImg)
        print()
        print("Saved Image at: ")
        print(imgPath)
        print()

if __name__ == "__main__":
    bldg_0_0_url = "https://www.gist.ac.kr/kr/html/sub05/050601.html"
    getDietImg(bldg_0_0_url, 0, 0)
    bldg_1_0_url = "https://www.gist.ac.kr/kr/html/sub05/050603.html"
    getDietImg(bldg_1_0_url, 1, 0)
    bldg_2_0_url = "https://www.gist.ac.kr/kr/html/sub05/050602.html"
    getDietImg(bldg_2_0_url, 2, 0)
    bldg_0_1_url = "https://www.gist.ac.kr/en/html/sub05/051201.html"
    getDietImg(bldg_0_1_url, 0, 1)
    #TODO no thumbnail
    #bldg_1_1_url = "https://www.gist.ac.kr/en/html/sub05/051202.html"
    #getDietImg(bldg_1_1_url, 1, 1)
    bldg_2_1_url = "https://www.gist.ac.kr/en/html/sub05/051203.html"
    getDietImg(bldg_2_1_url, 2, 1)