from urllib.request import urlopen
from bs4 import BeautifulSoup
# #step0: import
import pandas as pd
import json
import os
def isAlpha(word):
    try:
        return word.encode('ascii').isalpha()
    except UnicodeEncodeError:
        return False


df = pd.DataFrame(columns=["中文", "英文", "評分", "排名","地址"])

url = "https://www.tripadvisor.com.tw/Attraction_Review-g1066461-d320869-Reviews-National_Museum_of_Nature_and_Science-Taito_Tokyo_Tokyo_Prefecture_Kanto.html"
response = urlopen(url)
html = BeautifulSoup(response)

ch = html.find(class_ = "ui_header h1" )
rating = html.find(class_="ui_bubble_rating")
rank = html.find(class_="header_popularity")
address = html.find("span", class_="detail")
title_ch=''
title_en=''

#只有英文
if isAlpha(ch.text.split(' ')[1]):
        # print(ch.text.split(' ')[1])
        title_ch = None
        #print(title_ch)
        title_en = ' '.join(ch.text.split(' ')[1: ])
        title_name = title_en
#有中文
else:
        title_ch = ch.text.split(' ')[1]
        title_en = (' '.join(ch.text.split(' ')[2:]))
        title_name = title_ch

# print(rating["alt"])
# print(rank.text)
# print(address.text)

# print(ch.text.split(' ')[1])
# print(' '.join(ch.text.split(' ')[2:]))
print(ch.text.split(' '))
print(title_ch)
print(title_en)


data = {"中文":title_ch,
        "英文":title_en,
        "評分":rating["alt"],
        "排名":rank.text,
        "地址":address.text}
df = df.append(data, ignore_index=True)






#存資料
dn = "tripadvisor/" + title_name
if not os.path.exists(dn):
    os.makedirs(dn)
df.to_csv(dn + "/" + title_name, encoding="utf-8", index=False)
print("*"*50)


# # #抓評論
# number = 10
# page = 0
# while True:
#     page+=1
#     print("what's the page now?", page)
#     url1 = "https://www.tripadvisor.com.tw/Attraction_Review-g1066459-d1872416-Reviews-or" + str(number*(page-1)) + "-Tokyo_Skytree-Sumida_Tokyo_Tokyo_Prefecture_Kanto.html"
#     try:
#         response1 = urlopen(url1)
#         html1 = BeautifulSoup(response1)
#
#         comment_title = html1.find_all("span", class_="noQuotes")
#         comment_context = html1.find_all("div", class_="entry")
#         i_list = []
#         j_list = []
#         print(url1)
#         for i in comment_title:
#             i_list.append(i.text)
#         for j in comment_context:
#             j_list.append(j.text)
#         for num in range(len(i_list)):
#             print(i_list[num])
#             print(j_list[num])
#             print("*" * 50)
#
#             data1 = {"評論標題:": i_list[num],
#                      "評論內容": j_list[num]}
#
#
#     except:
#         print("到底了吧")
#         f = open(dn + "/" + title_name + "/meta.json", "w", encoding="utf-8")
#         json.dump(data1, f)
#         f.close()
#         break
#
#
#
# # 儲存內文(JSON
#
# # f = open(dn + "/meta.json", "w", encoding="utf-8")
# #
# # if not os.path.exists(dn):
# #     os.makedirs(dn)
# # f = open(fn, "wb")
# # json.dump(data, f)
# # f.close()
# # #
# #
# # # load: 檔案 -> Dict/List
# # # loads: 字串 -> Dict/List
# # #info = json.load(response)
# # # pics: List p: Dict
