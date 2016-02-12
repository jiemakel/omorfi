import random

with open("data.txt", "r", encoding="utf-8") as f:
    data = [x for x in f]

res = random.sample(data, 100)

rs = ""

for r in res:
    rs += r+"\n"



with open("100.txt", "w", encoding = "utf-8") as f:
    f.write(rs)


