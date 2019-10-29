import pandas as pd
import re
from textblob import TextBlob
import os

def del_word(x):
  s = (x.replace("透過行動裝置", "").replace("[", "").replace("]", "").replace(",", "").replace("...More", "")
       .replace("'", "").strip()).replace("TripAdvisor 會員", "")

  result = re.split('Date\s+of\s+experience\W\s\w+\s\d+', s)
  result2 = re.split('Thank\s+\w+', "".join(result))
  return result2




path = os.listdir("E:\\專題\\資料\\tripadvisor_English_1")



# print(path)
for i in path:
    print(i)
    df = pd.read_csv("E:\\專題\\資料\\tripadvisor_English_1\\" + i , encoding="utf-8")
    #
    #Data clear Comment
    # content = df["Comment"]
    # comment = []
    # for j in content:
    #     b = del_word(j)
    #     comment.append(b)
    #
    # df = df.drop(columns=["Comment"])
    # df["Comment"] = comment
    #
    # # data clear Star
    # star = df["Comment_Star"]
    # stars = []
    # for z in star:
    #     a = z.replace("ui_bubble_rating bubble_", "")
    #     stars.append(a)
    #
    # df["Star"] = stars
    # df = df.drop(columns=["Comment_Star"])
    #
    #
    # # # Define pos&neg
    # # pos = ''
    # # neg = ''
    # # for w in range(df.shape[0]):
    # #     if df.loc[w, "Star"] in ["40", "50"]:
    # #         pos += (df.loc[w, 'Comment'][0] + '\n')
    # #     elif df.loc[w, "Star"] in ["10", "20"]:
    # #         neg += (df.loc[w, 'Comment'][0] + '\n')
    # #
    # #
    #
    # #
    # #Score
    # # print(i)
    # # text = pos
    # # blob = TextBlob(text)
    # # print("pos:", len(pos), blob.sentiment)
    # #
    # # text = neg
    # # blob = TextBlob(text)
    # # print("neg:", len(neg), blob.sentiment)
    #
    # print(i)
    # text = ''
    # for w in range(df.shape[0]):
    #     text += (df.loc[w, 'Comment'][0] + '\n')
    #
    # blob = TextBlob(text)
    # print(blob.sentiment[0])
    #
    #
    # df["Score"] = blob.sentiment[0]
    # print(df)
    #
    #
    # # df.to_csv("E:/專題/景點爬蟲/tripadvisor/tripadvisor/情感分析/tripadvisor_English_2/" + i , encoding="utf-8")
    #
    #
    #
    # print("***************")