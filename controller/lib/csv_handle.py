# -*- coding: utf-8 -*-

import csv


def table(data):
    import sqlite3
    con = sqlite3.connect('/Users/changyouliang/project/others/smt/first.db')
    cur = con.cursor()

    sql = "insert into acv_tab (wo_no,time,c3 ,c4 ,R70 ,c6 ,C158 ,c8 ,R69 ,c10 ,R3 ,c12 ,IC8 ,c14 ,IC3 ,c16 ,D11 ,c18 ,L5 ,c20 ,C150 ,c22 ,C100 ,C24) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
        *data)

    try:
        cur.execute(sql)
    except Exception as e:
        print(e)
    finally:
        con.commit()
        cur.close()
        con.close()


def parse_csv(csv_file):
    """
    读取数据返回列表的数据
    :param csv_file:
    :return:
    """
    data = []
    with open(csv_file) as f:
        f_csv = csv.reader(f)
        # 去除头部数据
        header = next(f_csv)
        for row in f_csv:
            data.append(row)
    return data


if __name__ == '__main__':
    f = "../1HZ9011113-05_6433997B.csv"
    data = parse_csv(f)

    one = data[0]
    table(one)
