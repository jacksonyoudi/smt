# -*- coding: utf-8 -*-

import sqlite3

acv_tab = """
create table if not exists acv_tab (
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    typ varchar(50),
    model varchar(50),
    product_number varchar(50),
    wo_no varchar(50),
    surface varchar(50),
    cnt varchar(50),
    start_time varchar(50),
    end_time varchar(50),
    ct_duration decimal,
    theory_ts varchar(50) DEFAULT '',
    actual_ts varchar(50) DEFAULT '',
    movable_rate varchar(50) DEFAULT '',
    stop_ts int(10) default 0,
    fault_note varchar(50) default '',
    change_ts varchar(50) default '',
    gen_line varchar(20),
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""


def insert_acv(data, conn):
    conn = sqlite3.connect("../../smt/first.db")
    cursor = conn.cursor()
    cursor.execute(acv_tab)
    conn.commit()
    sql = "insert into acv_tab (typ,model,product_number,wo_no,cnt, start_time,end_time,ct_duration,stop_ts) values "

    for row in data:
        sql = sql + "('{}','{}','{}','{}','{}','{}','{}','{}'),".format(*row)
    sql = sql.strip(",") + ';'

    print(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
