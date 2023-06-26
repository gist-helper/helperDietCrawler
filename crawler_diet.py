import os
import requests
from bs4 import BeautifulSoup as bs

recentDietDivNumKor = 2
recentDietDivNumEng = 3

def getDietImg(url, bldgType, langType):
    webpage = requests.get(url)
    if(langType == 0):
        dietSrc = bs(webpage.content, "html.parser").select(".inner")[recentDietDivNumKor].img.get("src")
    else:
        dietSrc = bs(webpage.content, "html.parser").select(".inner")[recentDietDivNumEng].img.get("src")
    recentDietSrc = os.path.join(url, dietSrc)
    print(recentDietSrc)
    recentDietImg = requests.get(recentDietSrc).content
    imgPath = os.path.join("img", str(bldgType) + '_' + str(langType) + '.jpg')
    with open(imgPath, 'wb') as imgFile:
        imgFile.write(recentDietImg)

if __name__ == "__main__":
    bldg_0_0_url = "https://www.gist.ac.kr/kr/html/sub05/050601.html"
    getDietImg(bldg_0_0_url, 0, 0)
    bldg_1_0_url = "https://www.gist.ac.kr/kr/html/sub05/050603.html"
    getDietImg(bldg_1_0_url, 1, 0)
    bldg_2_0_url = "https://www.gist.ac.kr/kr/html/sub05/050602.html"
    getDietImg(bldg_2_0_url, 2, 0)
    bldg_0_1_url = "https://www.gist.ac.kr/en/html/sub05/051201.html"
    getDietImg(bldg_0_1_url, 0, 1)
    #bldg_1_1_url = "https://www.gist.ac.kr/en/html/sub05/051202.html"
    #getDietImg(bldg_1_1_url, 1, 1)
    bldg_2_1_url = "https://www.gist.ac.kr/en/html/sub05/051203.html"
    getDietImg(bldg_2_1_url, 2, 1)