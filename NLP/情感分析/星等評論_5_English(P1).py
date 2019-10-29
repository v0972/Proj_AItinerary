from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import json

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

df = pd.DataFrame(columns=["Comment", "Comment_Star"])


n=0
try:
    url = "https://www.tripadvisor.com/Attractions-g298184-Activities-Tokyo_Tokyo_Prefecture_Kanto.html"
    response = urlopen(url)
    html = BeautifulSoup(response)
    total = []
    for t in html.find_all("li", class_="attractions-attraction-overview-pois-PoiCard__item--3UzYK"):
        if not t.find("a") == None:
            turl = "https://www.tripadvisor.com" + t.find("a")["href"]
            total.append(turl)
    print(total)

    for x in total:
        url1 = x
        response = urlopen(url1)
        html = BeautifulSoup(response)

        en = html.find(class_="ui_header h1")


        # Comment
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        # import the webdriver
        driver = webdriver.Chrome("E:/pyETL/Tokyo/景點/tripadvisor/chromedriver", options=options)
        driver.get(url1)
        print("url1:",url1)
        num = 0


        try:
            end_page = driver.find_element_by_class_name("pageNumbers").find_element_by_class_name("last").text
            print(end_page)
        except:
            print("一頁而已")
            end_page = 1

        for i in range(int(end_page)):
            url2 = url1.split("-")[0] + "-or" + str(num) + "-" + '-'.join(url1.split("-")[1:])
                   # url1.split("-")[0] + "-or" + str(num) + "-" + '-'.join(url.split("-")[1:])
            print(url2)
            print("**********")
            try:

                driver.get(url2)
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

                for j in container:
                    x = j.find_elements_by_xpath("//div[@class='ui_column is-9']")
                    comment_star = (j.find_element_by_class_name('ui_bubble_rating').get_attribute('class'))
                    comment = (j.text.split('\n')[5:7])
                    # print(comment)
                    # print(comment_star)

                    data = {"Comment": comment,
                            "Comment_Star": comment_star
                            }
                    df = df.append(data, ignore_index=True)
                    dn = "tripadvisor_English/"
                    if not os.path.exists(dn):
                        os.makedirs(dn)

                    df.to_csv(dn + en.text + ".csv", encoding="utf-8", index=False)
                    # print("*" * 50)


            except:
                print("重跑")
                # break
            num += 10
        driver.close()


except:
    print("完美無缺的coding怎麼可能錯誤")



    #df.to_csv("第1頁.csv", encoding="utf-8", index=False)
    # 存資料



