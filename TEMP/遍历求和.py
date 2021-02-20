# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 15:02
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


source = [4980,1343,43256,23928,4040,1860,310,2918,1323,136,41536,31470,58979.5,41489,38332.5]
residx = []
sss = 74165.5

def getRes(x,newres,flag):
    res = []
#     print(type(x))
    for b in x:
        for a in range(15):
            if flag==0:
                if source[a]+b ==newres:
                    res.append(b.append(source[a]))
            else:
                if source[a]+sum(b) ==newres:
                    res.append(b.append(source[a]))
    return res


for num in range(2,15):
    print("当前查找的每组数值数:%d",num)
    res1=source
    for count in range(num):
        newres = [sss-a for a in res1]
        res1 = getRes(res1,newres,count)

    print("可用数据为: ",res1)










