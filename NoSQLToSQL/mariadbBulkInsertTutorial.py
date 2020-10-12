from pprint import pprint
import pymysql
import time
import sys

try:
    db = pymysql.connect(host='localhost', port=13306, user='root', password='42maru',db='maru')
    pprint(db)
    cursor = db.cursor()
    sqls = []
    for i in range(1000000):
        sql = "{0}".format(i)
        sqls.append(sql)
    # slqs_tuple = tuple(sqls)
    print("Make the Query Ended")
    start = time.time()
    sql = 'insert into test (test_text) values(%s)'
    cursor.executemany(sql, sqls)
    db.commit()
    print("total time: ", (time.time() - start))
    print(sys.maxsize)

except pymysql.DatabaseError as err:
    pprint(err)

"""
    10만건 데이터 입력 1s 각각의 insert 수행의 0.01속도
"""