#抓超連結
import csv
with open ("E:/pyETL/Tokyo/景點/p2-10中文景點名字.csv", 'r') as f:
    data = f.read()

#print(data)

a = data.split("\n")
#print(a)

spot = []
for i in a:
    b = i.replace(",","")
    print(b)
    spot.append(b+'\n')
print(spot)

with open ("E:/pyETL/Tokyo/景點/p2-10中文景點名字.txt", "w", encoding= "utf-8") as f:
    f.writelines(spot)


