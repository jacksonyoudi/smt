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
    stops varchar(50) default '',
    stop_ts int(10) default 0,
    fault_note varchar(50) default '',
    change_ts varchar(50) default '',
    gen_line varchar(20),
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""


def insert_acv(data, conn):
    cursor = conn.cursor()
    cursor.execute(acv_tab)
    conn.commit()
    sql = "insert into acv_tab (typ,model,product_number,wo_no,surface,cnt,start_time,end_time,ct_duration,stops,stop_ts,gen_line) values "

    for row in data:
        sql = sql + "('{typ}','{model}','{product_number}','{wo_no}','{surface}','{cnt}','{start_time}','{end_time}',{ct_duration},'{stops}',{stop_ts},'{gen_line}'),".format(
            **row)
    sql = sql.strip(",") + ';'

    print(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()


"""    id INTEGER PRIMARY KEY  AUTOINCREMENT,
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
    stops varchar(50) default '',
    stop_ts int(10) default 0,
    fault_note varchar(50) default '',
    change_ts varchar(50) default '',
    gen_line varchar(20),
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP"""


def get_acv(conn):
    cursor = conn.cursor()
    data = []
    cursor.execute(acv_tab)
    conn.commit()

    result = cursor.execute(
        "select id,typ,model,product_number,wo_no,surface,cnt,start_time,end_time,ct_duration,theory_ts,actual_ts,movable_rate,stops,stop_ts,fault_note,change_ts,gen_line from acv_tab;")
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
