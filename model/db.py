# -*- coding: utf-8 -*-

from controller.lib.csv_handle import parse_csv
from model.ct import insert_ct
from model.acv import insert_acv
import time
from controller.lib.pd_excel_handle import parse_excel_by_pd


def insert_ct_data(conn, file_path):
    data = parse_excel_by_pd(file_path)
    insert_ct(data, conn)
    print("ok")


def parse_acv_data(file_path, gen_line, conn):
    header, data = parse_csv(file_path)
    result = []
    length = len(data)
    stops = 0
    pre_time = None
    start_time = data[0][1]
    end_time = data[-1][1]
    stop_ts = 0
    row = None
    for i in range(0, length):
        row = data[i]
        time_array = time.strptime(row[1], "%Y/%m/%d %H:%M:%S")
        other_style_time = int(time.mktime(time_array))
        cur_time = other_style_time
        if pre_time:
            if (cur_time - pre_time) <= 60 * 5 and (cur_time - pre_time) > 0:
                stops += 1
                stop_ts += (cur_time - pre_time)
        pre_time = other_style_time
        item = {
            "typ": "detail",
            "product_number": row[0][10:19],
            "wo_no": row[0][22:30],
            "surface": row[0][-1],
            "start_time": row[1],
            "end_time": end_time,
            "cnt": '',
            "stops": '',
            "model": '',
            "ct_duration": 0,
            "stop_ts": 0,
            "gen_line": gen_line,
        }
        result.append(item)

    # typ,model,product_number,wo_no,surface,cnt,start_time,end_time,ct_duration,stops,stop_ts

    item = {
        "typ": "agg",
        "model": '',
        "ct_duration": 0,
        "product_number": row[0][10:19],
        "wo_no": row[0][22:30],
        "surface": row[0][-1],
        "start_time": start_time,
        "end_time": end_time,
        "cnt": length,
        "stops": stops,
        "stop_ts": stop_ts,
        "gen_line": gen_line
    }

    result.insert(0, item)

    insert_acv(result, conn)
