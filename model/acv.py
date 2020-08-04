# -*- coding: utf-8 -*-


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

# 'id', 'jizhong', 'pinfan', 'gongdanhao', 'mianfan', 'piliang', 'kaishi_shijian', 'jieshu_shijian',
#     #             'biaozhun_ct', 'lilun_shijian', 'shiji_shijian', 'kedong_lv', 'duanzanting_shijian', 'duanzanting_huishu', 'guzhangting_shijian',
#     #             'guzhang_beizhu','huanxian_shijian','daoru_shijian',
#     #             'gen_line'


acv_tab = """
create table if not exists acv_tab (
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    typ varchar(50),
    jizhong varchar(50),
    pinfan varchar(50),
    gongdanhao varchar(50),
    mianfan varchar(50),
    piliang varchar(50),
    kaishi_shijian varchar(50),
    jieshu_shijian varchar(50),
    biaozhun_ct decimal,
    lilun_shijian varchar(50) DEFAULT '',
    shiji_shijian varchar(50) DEFAULT '',
    kedong_lv varchar(50) DEFAULT '',
    duanzanting_shijian varchar(50) default '',
    duanzanting_huishu varchar(50) default '',
    guzhangting_shijian varchar(50) default '',
    guzhang_beizhu varchar(50) default '',
    huanxian_shijian varchar(50) default '',
    daoru_shijian varchar(50) default '',
    shengchanxian varchar(20),
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""


def insert_acv(data, conn):
    cursor = conn.cursor()
    cursor.execute(acv_tab)
    conn.commit()
    sql = "insert into acv_tab (typ,jizhong,pinfan,gongdanhao,mianfan,piliang,kaishi_shijian,jieshu_shijian,biaozhun_ct,duanzanting_shijian,duanzanting_huishu,guzhangting_shijian,daoru_shijian,shengchanxian) values "

    for row in data:
        sql = sql + "('{typ}','{jizhong}','{pinfan}','{gongdanhao}','{mianfan}','{piliang}','{kaishi_shijian}','{jieshu_shijian}',{biaozhun_ct},'{duanzanting_shijian}','{duanzanting_huishu}','{guzhangting_shijian}','{daoru_shijian}','{shengchanxian}'),".format(
            **row)
    sql = sql.strip(",") + ';'

    print(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()


def insert_report(data, conn):
    cursor = conn.cursor()
    cursor.execute(acv_tab)
    conn.commit()
    sql = "insert into acv_tab (jizhong,pinfan,gongdanhao,mianfan,piliang,kaishi_shijian,jieshu_shijian,biaozhun_ct,lilun_shijian,shiji_shijian,kedong_lv,duanzanting_shijian,duanzanting_huishu,guzhangting_shijian,guzhang_beizhu,huanxian_shijian,daoru_shijian) values "

    for row in data:
        sql = sql + "('{jizhong}','{pinfan}','{gongdanhao}','{mianfan}','{piliang}','{kaishi_shijian}','{jieshu_shijian}',{biaozhun_ct},'{lilun_shijian}','{shiji_shijian}','{kedong_lv}','{duanzanting_shijian}','{duanzanting_huishu}','{guzhangting_shijian}','{guzhang_beizhu}','{huanxian_shijian}','{daoru_shijian}'),".format(
            **row)
    sql = sql.strip(",") + ';'

    print(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()


def get_acv(conn):
    cursor = conn.cursor()
    data = []
    cursor.execute(acv_tab)
    conn.commit()

    result = cursor.execute(
        "select id,jizhong,pinfan,gongdanhao,mianfan,piliang,kaishi_shijian,jieshu_shijian,biaozhun_ct,lilun_shijian,shiji_shijian,kedong_lv,duanzanting_shijian,duanzanting_huishu,guzhangting_shijian,guzhang_beizhu,huanxian_shijian,daoru_shijian from acv_tab;")
    for row in result:
        data.append(list(row))
    cursor.close()
    return data


def delete_acv_by_id(conn, id):
    cursor = conn.cursor()
    sql = "delete from acv_tab where id={id}".format(id=id)
    print(sql)
    result = cursor.execute(sql)
    conn.commit()
    cursor.close()


if __name__ == '__main__':
    # insert_acv("", "")
    pass
