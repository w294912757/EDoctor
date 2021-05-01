import jieba
from collections import Counter
import csv
import pandas as pd
import pymysql


def analyse_words(prescriptions):
    count = Counter()
    for prescription in prescriptions:
        if prescription[8].year == 2019:
            result = jieba.cut(prescription[5], cut_all=False, HMM=False)
            for i in result:
                if len(i) > 1 and i != '\r\n':
                    count[i] += 1
    print(count.most_common())


db = pymysql.connect(host='112.124.56.37', port=3306, user='root', passwd='123456', db='edoctor', charset='utf8')
cursor = db.cursor()
# 分析
# sql = "select * from backend_prescription"
# cursor.execute(sql)
# data = cursor.fetchall()
# analyse_words(data)

# 建立疾病库
# dic = csv.reader(open("./MED_DIC.csv", "r", encoding='utf8'))
# dic_list = list(dic)
# disease = []
# for i in dic_list:
#     if i[1] == 'DIS':
#         # sql = "insert into backend_disease(name) values('%s')" % (i[0])
#         # cursor.execute(sql)
#         # db.commit()
#         disease.append(i[0])
# name =["name"]
# test =pd.DataFrame(columns=name,data=disease)
# test.to_csv('./disease.csv')

# 加入词典
dic = csv.reader(open("./disease.csv", "r", encoding='utf8'))
dic_list = list(dic)
print(dic_list)
for row in dic_list:
    jieba.add_word(row[1].strip())
    jieba.suggest_freq(row[1].strip(), tune=True)