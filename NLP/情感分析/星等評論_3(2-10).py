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

def isAlpha(word):
    try:
        return word.encode('ascii').isalpha()
    except UnicodeEncodeError:
        return False

df = pd.DataFrame(columns=["評論", "評論星等"])

howmany = 9
n=0
try:
    for i in range(howmany):
        n += 1
        url = "https://www.tripadvisor.com.tw/Attractions-g298184-Activities-oa" + str(
            30 * n) + "-Tokyo_Tokyo_Prefecture_Kanto.html"
        response = urlopen(url)
        html = BeautifulSoup(response)
        total = []
        for t in html.find_all("div", class_="tracking_attraction_title"):
            if not t.find("a") == None:
                turl = "https://www.tripadvisor.com.tw" +  t.find("a")["href"]
                total.append(turl)
        print(total)
        print("what's page",n+1)

        number = 31
        for x in total:
            url1 = x
            response = urlopen(url1)
            html = BeautifulSoup(response)

            ch = html.find(class_="ui_header h1")
            title_ch = ''
            title_en = ''


        # print("---------------------------")
            if isAlpha(ch.text.split(' ')[1]):
                # print(ch.text.split(' ')[1])
                title_ch = None
                # print(title_ch)
                title_en = ' '.join(ch.text.split(' ')[1:])
                title_name = title_en
            else:
                title_ch = ch.text.split(' ')[1]
                title_en = (' '.join(ch.text.split(' ')[2:]))
                title_name = title_ch

            #print(title_ch)
            #print(title_en)

            # Comment
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")

            # import the webdriver
            driver = webdriver.Chrome("E:/pyETL/Tokyo/景點/tripadvisor/chromedriver", options=options)
            driver.get(url1)

            num = 0
            try:
                end_page = driver.find_element_by_class_name("pageNumbers").find_element_by_class_name("last").text
                print(end_page)
            except:
                print("一頁而已")
                end_page = 1

            for i in range(int(end_page)):
                url2 = url1.split("-")[0] + "-or" + str(num) + "-" + '-'.join(url1.split("-")[1:])
                # print(url2)
                try:
                    driver.get(url2)
                    time.sleep(2)
                    if (check_exists_by_xpath("//span[@class='taLnk ulBlueLinks']")):
                        # 找到"更多"的按鍵
                        for item in driver.find_elements_by_class_name(
                                'taLnk ulBlueLinks'):  # driver.find_elements_by_xpath("//span[@class='taLnk ulBlueLinks']"):
                            item.click()
                            time.sleep(4)

                    container = driver.find_elements_by_xpath("//div[@class='review-container']")


                    for i in container:
                        x = i.find_elements_by_xpath("//div[@class='ui_column is-9']")
                        comment_star = (i.find_element_by_class_name('ui_bubble_rating').get_attribute('class'))
                        comment = (i.text.split('\n')[5:7])
                        # print(comment)
                        # print(comment_star)
                        # print("***" * 5)


                        data = {"評論": comment,
                                "評論星等": comment_star
                                }
                        df = df.append(data, ignore_index=True)

                        dn = "tripadvisor/"
                        if not os.path.exists(dn):
                            os.makedirs(dn)
                        df.to_csv(dn + title_name, encoding="utf-8", index=False)


                except:
                    print("完美無缺的coding怎麼可能錯誤呢??????")
                    # break
                num += 10
            driver.close()


except:
    print("完美無缺的coding怎麼可能錯誤")



    #df.to_csv("第1頁.csv", encoding="utf-8", index=False)
    # 存資料



