import csv

import jieba
from collections import Counter


def analyse_words(prescriptions):
    count = Counter()
    for prescription in prescriptions:
        if prescription[8].year == 2019:
            result = jieba.cut(prescription[5], cut_all=False, HMM=False)
            for i in result:
                if len(i) > 1 and i != '\r\n':
                    count[i] += 1
    print(count.most_common())


# 链接数据库
# db = pymysql.connect(host='112.124.56.37', port=3306, user='root', passwd='123456', db='edoctor', charset='utf8')
# cursor = db.cursor()

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
# try:
#     fp = open('./disease.txt', "w+", encoding="utf-8")
#     for item in disease:
#         fp.write(str(item) + "\n")
#     fp.close()
# except IOError:
#     print("fail to open file")

#加入词典
# dic = open("./disease.txt", "r", encoding='utf8')
# dic_list = list(dic)
# for row in dic_list:
#     print(row)
#     jieba.add_word(row.strip())
#     jieba.suggest_freq(row.strip(), tune=True)
