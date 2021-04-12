import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://www.openrice.com/en/hongkong/restaurants?cuisineId=2009&districtId=1999"
html = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(html.text,"html.parser")

dictionary = {
    "res_id": [],
    "address": [],
    "likes": [],
    "dislikes": [],
    "bookmarks": [],
    "price_range": [],
    "cuisine": [],
    "review": []
}

# loop pages
while True:
    # find id
    items = soup.select(".content-wrapper")

    for i in items:
        dictionary["res_id"].append(i.find(class_="openrice-bookmark")["data-poi-id"])
        dictionary["address"].append(i.find(class_='icon-info address').text.strip("\n\r"))
        dictionary["likes"].append(i.find(class_='score score-big highlight').text)
        dictionary["dislikes"].append(i.find(class_='score highlight').text)
        dictionary["bookmarks"].append(i.find(class_="bookmarkedUserCount").attrs['data-count'])
        dictionary["price_range"].append(i.find(class_="icon-info-food-price").span.text)
        dictionary["cuisine"].append(i.select(".condition_tag_40x40_desktop ~ li")[1].text if len(i.select(".condition_tag_40x40_desktop ~ li")) > 1 else "Not Specified")
        dictionary["review"].append(re.search("\d+",i.find(class_="counters-container").text).group())
    
    nextbtn = soup.find(class_="common_pagination_more_r_desktop")

    if nextbtn:
        nextlink = nextbtn.parent["href"]
        subhtml = requests.get("https://www.openrice.com" + nextlink,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(subhtml.text, "html.parser")
    else:
        break
    
df = pd.DataFrame(dictionary)
df.to_csv("openrice.csv",index=False)