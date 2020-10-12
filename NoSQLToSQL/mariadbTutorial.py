from pprint import pprint
import pymysql
import time

try:
    db = pymysql.connect(host='localhost', port=13306, user='root', password='42maru',db='maru')
    pprint(db)
    cursor = db.cursor()
    sqls =[]
    for i in range(100000):
        sql = "insert into test (test_text) values ({0})".format(i)
        sqls.append(sql)
    print("Make the Query Ended")
    start = time.time()
    for sql in sqls:
        cursor.execute(sql)
    db.commit()
    print("total time: ", (time.time() - start))

except pymysql.DatabaseError as err:
    pprint(err)

"""
    10만건 데이터 입력 131s
"""