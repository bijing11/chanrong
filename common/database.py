import pymysql
import requests
from common.chanrong.database_data import connect_string


def query_db_data(sql):
    con = pymysql.connect(**connect_string)
    cur = con.cursor()
    cur.execute(sql)
    dd = cur.fetchall()
    cur.close()
    con.close()
    return dd

if __name__ == '__main__':
    sql = "SELECT * FROM frisk_company_profile where id = 3"
    print(query_db_data(sql))