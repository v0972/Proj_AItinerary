#找到資料夾
import os
import pandas as pd
import re
from snownlp  import SnowNLP



def del_word(x):
  s = (x.replace("透過行動裝置", "").replace("[", "").replace("]", "").replace(",", "").replace("...更多", "")
       .replace("'", "").strip()).replace(' 由 Asia Online Language Studio 翻譯 評等翻譯', "").replace("TripAdvisor 會員", "")

  result = re.split('體驗日期\W\s\d+年\d+月', s)
  result2 = re.split('感謝\s+\w+', "".join(result))
  return result2


path = os.listdir("E:\\專題\\景點爬蟲\\tripadvisor\\tripadvisor\\情感分析\\tripadvisor")
# print(path)

print(len(path))



# a=[path,[]]#包含两个不同的子列表[1,2,3,4]和[5,6,7,8]


# print(path)
# for i in path:
#     # print(i)
#     df = pd.read_csv("E:/專題/景點爬蟲/tripadvisor/tripadvisor/情感分析/tripadvisor/" + i , encoding="utf-8")
# # print(df)
# #clear data
#     content = df["評論"]
#     comment = []
#     for j in content:
#       b = del_word(''.join(j))
#       comment.append(b)
#
#     df["comment"] = comment
#     df = df.drop(columns=["評論"])
#
#     star = df["評論星等"]
#     stars = []
#     for z in star:
#         a = z.replace("ui_bubble_rating bubble_", "")
#         stars.append(a)
#
#     df["Star"] = stars
#     df = df.drop(columns=["評論星等"])
#
#
#
#     #Define pos&neg
#     #
#     pos=''
#     neg=''
#     for w in range(df.shape[0]):
#         if df.loc[w,"Star"] in ["40","50"]:
#             pos+=(df.loc[w,'comment'][0]+'\n')
#         else:
#             neg+=(df.loc[w,'comment'][0]+'\n')
#
#     #Pos and Neg score
#     point = 0
#     for b in pos.split("\n"):
#         if b != '':
#             s = SnowNLP(b)
#             point += (s.sentiments)
#     score = point/len(pos.split("\n"))
#
#     print(i,score)

    # #寫到train_data裡面
    # with open('C:\\Users\\Big data\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\snownlp\\sentiment\\pos_test.txt',
    #           "a", encoding='utf-8') as f:
    #   f.write(pos)
    #
    # with open('C:\\Users\\Big data\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\snownlp\\sentiment\\neg_test.txt',
    #           "a", encoding='utf-8') as f:
    #   f.write(neg)





