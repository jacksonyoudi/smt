# -*- coding: utf-8 -*-

import csv
import datetime
import time


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
    return header, data


if __name__ == '__main__':
    f = "../../1HZ9011113-05_6433997B.csv"
    header, data = parse_csv(f)

    result = []

    print(header)

    length = len(data)

    stops = 0
    pre_time = None
    cur_time = None
    start_time = data[0][1]
    end_time = data[-1][1]
    row = None
    for i in range(0, length):
        row = data[i]

        time_array = time.strptime(row[1], "%Y/%m/%d %H:%M:%S")
        other_style_time = int(time.mktime(time_array))
        cur_time = other_style_time
        if pre_time:
            if (cur_time - pre_time) <= 60 * 5 and (cur_time - pre_time) > 0:
                stops += 1
        pre_time = other_style_time

        item = {
            "type": "detail",
            "品番": row[0][10:19],
            "工单号": row[0][22:30],
            "面番": row[0][-1],
            "开始时间": row[1],
            "结束时间": end_time,
            "批量": length,
            "导入成功时间": datetime.datetime.now()
        }

    item = {
        "type": "agg",
        "品番": row[0][10:19],
        "工单号": row[0][22:30],
        "面番": row[0][-1],
        "开始时间": start_time,
        "结束时间": end_time,
        "批量": length,
        "短暂停回数": stops,
        "导入成功时间": datetime.datetime.now()
    }

    result.insert(0, item)

    print(result[0])

    print(stops)
    # one = data[0]
    # table(one)
