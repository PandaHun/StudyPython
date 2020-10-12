import pandas as pd
from pprint import pprint
import pymysql
import time

try:
    db = pymysql.connect(host='localhost', port=13306, user='root', password='42maru',db='maru')
    pprint(db)
    cursor = db.cursor()
    sql = 'select * from test'
    df = pd.read_sql(sql, db)
    file_path = "./temp.csv"
    start = time.time()
    df.to_csv(file_path, encoding='utf-8', header = True,\
         doublequote = True, sep=',', index=False)
    print("total time: ", (time.time() - start))
    db.close()

except pymysql.DatabaseError as err:
    pprint(err)


"""
    10만건 데이터 다운로드 0.15s
"""