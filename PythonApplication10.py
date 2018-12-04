# coding:utf-8
import pandas as pd
a =open(r"C:\Users\11202\Documents\WeChat Files\A1120225688\Files\Schoolkids.csv")
data = pd.read_csv(a)
data_1 = data.Age
use = []
use_1 = []
MAX = 0
Dn = {}
i = 0
for y in data_1:
    Dn[i] = y
    i += 1
for y in data_1:
    if y > MAX:
        MAX = y
for i in Dn.keys():
    if Dn[i] == MAX:
        use.append(i)
for cycle in use:
        g=data.loc[cycle][0]
        d=data.loc[cycle][1]
        e=data.loc[cycle][2]
        f=data.loc[cycle][3]
        a = (g,d,e,f)
        use_1.append(a)
print(use_1)


    



