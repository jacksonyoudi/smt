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
    end_time = data[-1][1]
    stop_ts = 0
    row = None
    cst_tz = timezone('Asia/Shanghai')
    insert_time = datetime.datetime.now().replace(tzinfo=cst_tz).strftime("%Y-%m-%d %H:%M:%S")

    ct_dict = get_ct(conn)
    model_name = ''
    ct_duration = 0

    guzhang_all_ts = 0

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
            ct_key = mianfan + 'F'
        ct_item = ct_dict.get(ct_key)

        jizhong = ''
        biaozhun_ct = 0
        if ct_item:
            jizhong = ct_item[1]
            biaozhun_ct = ct_item[line_index]
        if pre_time:
            if (cur_time - pre_time) <= 60 * 5 and (cur_time - pre_time) > 0:
                stops += 1
                stop_ts += (cur_time - pre_time)
            elif (cur_time - pre_time) > 5 * 60:
                guzhang_shijian = (cur_time - pre_time) - biaozhun_ct
                guzhang_all_ts += guzhang_shijian

                item = {
                    "typ": "detail",
                    "pinfan": pingfan,
                    "gongdanhao": row[0][22:30],
                    "mianfan": mianfan,
                    "kaishi_shijian": row[1],
                    "jieshu_shijian": end_time,
                    "piliang": '',
                    "jizhong": jizhong,
                    "biaozhun_ct": biaozhun_ct,
                    "duanzanting_shijian": '',
                    "duanzanting_huishu": '',
                    "guzhangting_shijian": "{min}:{sec}".format(min=guzhang_shijian // 60, sec=guzhang_shijian % 60),
                    "daoru_shijian": insert_time,
                    "shengchanxian": gen_line
                }
                result.append(item)
        ct_duration = biaozhun_ct
        model_name = jizhong
        pre_time = other_style_time
    # typ,model,product_number,wo_no,surface,cnt,start_time,end_time,ct_duration,stops,stop_ts

    print(model_name)
    item = {
        "pinfan": row[0][10:19],
        "gongdanhao": row[0][22:30],
        "mianfan": row[0][-1],
        "kaishi_shijian": row[1],
        "jieshu_shijian": end_time,
        "piliang": str(length),
        "jizhong": model_name,
        "biaozhun_ct": ct_duration,
        "duanzanting_shijian": "{min}:{sec}".format(min=stop_ts // 60, sec=stop_ts % 60),
        "duanzanting_huishu": str(stops),
        "guzhangting_shijian": "{min}:{sec}".format(min=guzhang_all_ts // 60, sec=guzhang_all_ts % 60),
        "daoru_shijian": insert_time,
        "shengchanxian": gen_line,
        "typ": "agg"
    }

    result.insert(0, item)

    insert_acv(result, conn)


def parse_report_data(file_path, conn):
    header, data = parse_csv(file_path)
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
