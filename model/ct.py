# -*- coding: utf-8 -*-

ct_tab = """
create table if not exists ct_tab (
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    model_name varchar(50),
    product_number varchar(50),
    surface varchar(50),
    model varchar(50),
    eps_1 decimal,
    eps_2 decimal,
    eps_3 decimal,
    eps_4 decimal,
    eps_5 decimal,
    eps_6 decimal,
    eps_7 decimal,
    eps_8 decimal,
    eps_9 decimal,
    eps_10 decimal,
    eps_11 decimal,
    eps_12 decimal,
    eps_13 decimal,
    eps_14 decimal,
    eps_15 decimal,
    eps_16 decimal,
    ts TIMESTAMP default CURRENT_TIMESTAMP
    )
"""


def insert_ct(data, conn):
    cursor = conn.cursor()
    cursor.execute("drop table if exists ct_tab;")
    conn.commit()
    cursor.execute(ct_tab)
    conn.commit()
    sql = "insert into ct_tab (model_name, product_number, surface, model,eps_1, eps_2,eps_3,eps_4,eps_5,eps_6,eps_7,eps_8,eps_9,eps_10,eps_11,eps_12,eps_13,eps_14,eps_15,eps_16) values "

    for row in data:
        sql = sql + "('{}','{}','{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}),".format(*row)
    sql = sql.strip(",") + ';'

    print(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()


def get_ct(conn):
    cursor = conn.cursor()
    data = {}

    result = cursor.execute(
        "select id,model_name, product_number, surface, model,eps_1, eps_2,eps_3,eps_4,eps_5,eps_6,eps_7,eps_8,eps_9,eps_10,eps_11,eps_12,eps_13,eps_14,eps_15,eps_16 from ct_tab;")
    for row in result:
        key = row[1] + row[2] + row[3]
        data[key] = row
    cursor.close()
    return data


if __name__ == '__main__':
    file_path = "/Users/youdi/Desktop/20200721.xlsm"
    # data = parse_excel_by_pd(file_path)
    # insert_ct(data)
    get_ct('aa')
