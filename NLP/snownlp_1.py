import pandas as pd
import re
from snownlp  import SnowNLP

def del_word(x):
  s = (x.replace("透過行動裝置", "").replace("[", "").replace("]", "").replace(",", "").replace("...更多", "")
       .replace("'", "").strip()).replace(' 由 Asia Online Language Studio 翻譯 評等翻譯', "").replace("TripAdvisor 會員", "")

  result = re.split('體驗日期\W\s\d+年\d+月', s)
  result2 = re.split('感謝\s+\w+', "".join(result))
  return result2


df = pd.read_csv("E:/專題/景點爬蟲/tripadvisor/tripadvisor/情感分析/tripadvisor/Tokyo Metropolitan Government Buildings Observatories",encoding="utf-8")


#clear data
content = df["評論"]
comment = []
for i in content:
  b = del_word(''.join(i))
  comment.append(b)

df["comment"] = comment
df = df.drop(columns=["評論"])

star = df["評論星等"]
stars = []
for i in star:
    a = i.replace("ui_bubble_rating bubble_", "")
    stars.append(a)

df["Star"] = stars
df = df.drop(columns=["評論星等"])



#Define pos&neg

pos=''
neg=''
for i in range(df.shape[0]):
    if df.loc[i,"Star"] in ["40","50"]:
        pos+=(df.loc[i,'comment'][0]+'\n')
    else:
        neg+=(df.loc[i,'comment'][0]+'\n')

#Pos score
point = 0
for i in pos.split("\n"):
    if i != '':
        s = SnowNLP(i)
        # print(i)
        # print(s.sentiments)
        point += (s.sentiments)
pos_score = point/len(pos.split("\n"))


#neg score
point = 0
for i in neg.split("\n"):
    if i != '':
        s = SnowNLP(i)
        # print(i)
        # print(s.sentiments)
        point += (s.sentiments)
neg_score = point/len(neg.split("\n"))

# pos + neg score
# sentences = ''
# for i in comment:
#     sentences += i[0] + "\n"
#
# for i in sentences.split("\n"):
#     if i != "":
#         s = SnowNLP(i)
#         print(i)
#         print(s.sentiments)
#         point += (s.sentiments)
# Score = point/len(pos.split("\n"))
# print(Score)


print("*******************")
print(pos_score)
print(neg_score)



#寫到train_data裡面
# with open(
#         'C:\\Users\\Big data\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\snownlp\\sentiment\\pos_test.txt',
#         "w", encoding='utf-8') as f:
#   f.write(pos)





