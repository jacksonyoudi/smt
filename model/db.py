# -*- coding: utf-8 -*-

from controller.lib.csv_handle import parse_csv
from model.ct import insert_ct
from model.acv import insert_acv, insert_report
import time
import datetime
from pytz import timezone
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
    cst_tz = timezone('Asia/Shanghai')
    insert_time = datetime.datetime.now().replace(tzinfo=cst_tz).strftime("%Y-%m-%d %H:%M:%S")

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
        # typ,jizhong,pinfan,gongdanhao,mianfan,piliang,kaishi_shijian,jieshu_shijian,biaozhun_ct," \
        #           "duanzanting_shijian,duanzanting_huishu,guzhangting_shijian,daoru_shijian,shengchanxian

        item = {
            "typ": "detail",
            "pinfan": row[0][10:19],
            "gongdanhao": row[0][22:30],
            "mianfan": row[0][-1],
            "kaishi_shijian": row[1],
            "jieshu_shijian": end_time,
            "piliang": '',
            "jizhong": '',
            "biaozhun_ct": 0,
            "duanzanting_shijian": '',
            "duanzanting_huishu": '',
            "guzhangting_shijian": '',
            "daoru_shijian": insert_time,
            "shengchanxian": gen_line
        }
        result.append(item)

    # typ,model,product_number,wo_no,surface,cnt,start_time,end_time,ct_duration,stops,stop_ts

    item = {
        "pinfan": row[0][10:19],
        "gongdanhao": row[0][22:30],
        "mianfan": row[0][-1],
        "kaishi_shijian": row[1],
        "jieshu_shijian": end_time,
        "piliang": str(length),
        "jizhong": '',
        "biaozhun_ct": 0,
        "duanzanting_shijian": '',
        "duanzanting_huishu": '',
        "guzhangting_shijian": '',
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
