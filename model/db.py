# -*- coding: utf-8 -*-

from controller.lib.csv_handle import parse_csv
from model.ct import insert_ct, get_ct
from model.acv import insert_acv, insert_report
import time
import datetime
from pytz import timezone
from controller.lib.pd_excel_handle import parse_excel_by_pd

lines = {
    "EPS 1#": 6,
    "EPS 2#": 7,
    "EPS 3#": 8,
    "EPS 4#": 9,
    "EPS 5#": 10,
    "EPS 6#": 11,
    "ECU 7#": 12,
    "ECU 8#": 13,
    "ECU 9#": 14,
    "ECU 10#": 15,
    "ECU 11#": 16,
    "ECU 12#": 17,
    "ECU 13#": 18,
    "ECU 14#": 19,
    "ECU 15#": 20,
    "ECU 16#": 21

}


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
    pre_time_str = ''
    start_time = data[0][1]
    end_time = data[-1][1]
    stop_ts = 0
    row = None
    cst_tz = timezone('Asia/Shanghai')
    insert_time = datetime.datetime.now().replace(tzinfo=cst_tz).strftime("%Y-%m-%d %H:%M:%S")

    ct_dict = get_ct(conn)

    guzhang_all_ts = 0

    pingfan = data[0][0][10:19]
    mianfan = data[0][0][-1]

    ct_key = pingfan + mianfan
    line_index = lines.get(gen_line) - 1

    if mianfan == 'A':
        ct_key = pingfan + 'F'
    ct_item = ct_dict.get(ct_key)
    ct_duration = 0
    model_name = ''
    if ct_item:
        model_name = ct_item[1]
        ct_duration = ct_item[line_index]

    for i in range(0, length):
        row = data[i]

        if len(row[1]) == 18:
            time_array = time.strptime(row[1], "%Y/%m/%d %H:%M:%S")
        elif len(row[1]) == 15:
            time_array = time.strptime(row[1], "%Y/%m/%d %H:%M")
        else:
            continue
        other_style_time = int(time.mktime(time_array))
        cur_time = other_style_time

        pingfan = row[0][10:19]
        mianfan = row[0][-1]

        ct_key = pingfan + mianfan
        line_index = lines.get(gen_line) - 1

        if mianfan == 'A':
            ct_key = pingfan + 'F'
        ct_item = ct_dict.get(ct_key)

        jizhong = ''
        biaozhun_ct = 0
        if ct_item:
            jizhong = ct_item[1]
            biaozhun_ct = ct_item[line_index]
        if pre_time:
            if (cur_time - pre_time - ct_duration) <= 60 * 5 and (cur_time - pre_time - ct_duration) > 0:
                stops += 1
                stop_ts += (cur_time - pre_time - ct_duration)
            elif (cur_time - pre_time-biaozhun_ct) > 5 * 60:
                guzhang_shijian = (cur_time - pre_time) - biaozhun_ct
                guzhang_all_ts += guzhang_shijian

                item = {
                    "typ": "detail",
                    "pinfan": pingfan,
                    "gongdanhao": row[0][22:29],
                    "mianfan": mianfan,
                    "kaishi_shijian": pre_time_str,
                    "jieshu_shijian": row[1],
                    "piliang": '',
                    "jizhong": jizhong,
                    "biaozhun_ct": biaozhun_ct,
                    "duanzanting_shijian": '',
                    "duanzanting_huishu": '',
                    "guzhangting_shijian": "00:{min}:{sec}".format(min=int(guzhang_shijian // 60),
                                                                sec=int(guzhang_shijian % 60)),
                    "daoru_shijian": insert_time,
                    "shengchanxian": gen_line
                }
                result.append(item)
        pre_time = other_style_time
        pre_time_str = row[1]

    item = {
        "pinfan": row[0][10:19],
        "gongdanhao": row[0][22:29],
        "mianfan": row[0][-1],
        "kaishi_shijian": start_time,
        "jieshu_shijian": end_time,
        "piliang": str(length),
        "jizhong": model_name,
        "biaozhun_ct": ct_duration,
        "duanzanting_shijian": "00:{min}:{sec}".format(min=int(stop_ts // 60), sec=int(stop_ts % 60)),
        "duanzanting_huishu": str(stops),
        "guzhangting_shijian": "00:{min}:{sec}".format(min=int(guzhang_all_ts // 60), sec=int(guzhang_all_ts % 60)),
        "daoru_shijian": insert_time,
        "shengchanxian": gen_line,
        "typ": "agg"
    }

    result.insert(0, item)

    insert_acv(result, conn)


def parse_report_data(file_path, conn):
    header, data = parse_csv(file_path, 'utf-8')
    result = []
    for row in data:
        item = {
            "jizhong": row[0],
            "pinfan": row[1],
            "gongdanhao": row[2],
            "mianfan": row[3],
            "piliang": row[4],
            "kaishi_shijian": row[5],
            "jieshu_shijian": row[6],
            "biaozhun_ct": row[7],
            "lilun_shijian": row[8],
            "shiji_shijian": row[9],
            "kedong_lv": row[10],
            "duanzanting_shijian": row[11],
            "duanzanting_huishu": row[12],
            "guzhangting_shijian": row[13],
            "guzhang_beizhu": row[14],
            "huanxian_shijian": row[15],
            "daoru_shijian": row[16]
        }
        result.append(item)
    insert_report(result, conn)
