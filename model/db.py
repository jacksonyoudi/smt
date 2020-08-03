# -*- coding: utf-8 -*-

from controller.lib.csv_handle import parse_csv
import time


def parse_data(file_path, gen_line, conn):
    header, data = parse_csv(file_path)
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
            "typ": "detail",
            "product_number": row[0][10:19],
            "wo_no": row[0][22:30],
            "surface": row[0][-1],
            "start_time": row[1],
            "end_time": end_time,
            "cnt": '',
            "stops": ''
        }

    item = {
        "typ": "agg",
        "product_number": row[0][10:19],
        "wo_no": row[0][22:30],
        "surface": row[0][-1],
        "start_time": start_time,
        "end_time": end_time,
        "cnt": length,
        "stops": stops,
    }

    result.insert(0, item)

    print(result[0])

    print(stops)
