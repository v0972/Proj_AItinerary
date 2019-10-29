from urllib.request import urlopen
from bs4 import BeautifulSoup
# #step0: import
import pandas as pd
import json
import os
import csv
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

# def isAlpha(word):
#     try:
#         return word.encode('ascii').isalpha()
#     except UnicodeEncodeError:
#         return False

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


df = pd.DataFrame(columns=["Comment", "Comment_Star"])

url = (("https://www.tripadvisor.com/Attraction_Review-g14129610-d4045009-Reviews"
        "-Namiyoke_Inari_Shrine-Tsukiji_Chuo_Tokyo_Tokyo_Prefecture_Kanto.html"))
response = urlopen(url)
html = BeautifulSoup(response)

en = html.find(class_="ui_header h1")
print(en.text)

# rating = html.find(class_="ui_bubble_rating")
# rank = html.find(class_="header_popularity")
# address = html.find("span", class_="detail")
# type = html.find("div", class_="detail")
title_ch = ''
title_en = ''

#Comment

options = webdriver.ChromeOptions()
options.add_argument("--headless")


# import the webdriver
driver = webdriver.Chrome("E:/pyETL/Tokyo/景點/tripadvisor/chromedriver", options=options)
# insert the tripadvisor's website of one attraction
driver.get(url)

# Comment
num = 0
# driver.get(("https://www.tripadvisor.com.tw/Attraction_Review-g1066456-d2311984-Reviews-or" + str(10) +
#             "-Tokyo_Camii_Turkish_Culture_Center-Shibuya_Tokyo_Tokyo_Prefecture_Kanto.html"))

try:
    end_page = driver.find_element_by_class_name("pageNumbers").find_element_by_class_name("last").text
    print(end_page)
except:
    print("一頁而已87")
    end_page = 1

for i in range(int(end_page)):
    url1 = url.split("-")[0] + "-or" + str(num) + "-" + '-'.join(url.split("-")[1:])
    print(url1)
    try:

        driver.get(url1)
        # driver.get(("https://www.tripadvisor.com.tw/Attraction_Review-g1066454-d1626639-Reviews-or" + str(num) +
        #           "-Jonanjima_SeasidePark-Ota_Tokyo_Tokyo_Prefecture_Kanto.html"))
        # 10-Tokyo_Camii_Turkish_Culture_Center-Shibuya_Tokyo_Tokyo_Prefecture_Kanto.html
        # s = driver.find_element_by_class_name("pageNum last taLnk")
        # print(s)
        # function to check if the button is on the page
        time.sleep(5)
        if (check_exists_by_xpath("//span[@class='taLnk ulBlueLinks']")):
            # to expand the review
            for item in driver.find_elements_by_class_name(
                    'taLnk ulBlueLinks'):  # driver.find_elements_by_xpath("//span[@class='taLnk ulBlueLinks']"):
                item.click()
                time.sleep(2)

        container = driver.find_elements_by_xpath("//div[@class='review-container']")


        # 評論星等
        # x = driver.find_elements_by_xpath("//div[@class='ui_column is-9']")

        for j in container:
            x = j.find_elements_by_xpath("//div[@class='ui_column is-9']")
        # print(x[1].find_element_by_class_name('ui_bubble_rating').get_attribute('class'))
        # for i in x:
            comment_star = (j.find_element_by_class_name('ui_bubble_rating').get_attribute('class'))
            comment = (j.text.split('\n')[5:7])
            print(comment)
            print(comment_star)


            data = {"Comment": comment,
                    "Comment_Star": comment_star
                    }
            df = df.append(data, ignore_index=True)
            dn = "tripadvisor_English/"
            if not os.path.exists(dn):
                os.makedirs(dn)

            df.to_csv(dn + en.text + ".csv", encoding="utf-8", index=False)
            print("*" * 50)

        # for j in container:
        #     comment.append(j.text.split('\n')[5:7])
        #     print(j.text)
            #print("********************")
    except:
        print("重跑")
        # break
    num += 10
driver.close()
#




#存資料
