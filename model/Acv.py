# -*- coding: utf-8 -*-

acv_tab = """
create table if not exists acv_tab (
    id INTEGER PRIMARY KEY  AUTOINCREMENT ,
    wo_no varchar(50) NOT NULL,
    time varchar(50),
    c3 varchar(50),
    c4 varchar(50),
    R70 varchar(50),
    c6 varchar(50),
    C158 varchar(50),
    c8 varchar(50),
    R69 varchar(50),
    c10 varchar(50),
    R3 varchar(50),
    c12 varchar(50),
    IC8 varchar(50),
    c14 varchar(50),
    IC3 varchar(50),
    c16 varchar(50),
    D11 varchar(50),
    c18 varchar(50),
    L5 varchar(50),
    c20 varchar(50),
    C150 varchar(50),
    c22 varchar(50),
    C100 varchar(50),
    C24 varchar(50),
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
"""

agg_tab = """
create table if not exists detail_tab (
    id INTEGER PRIMARY KEY  AUTOINCREMENT ,
    typ INTEGER(5),
    c1 varchar(50),
    c2 varchar(50),
    c3 varchar(50),
    c4 varchar(50),
    c5 varchar(50),
    c6 varchar(50),
    c7 varchar(50),
    c8 varchar(50),
    c9 varchar(50),
    c10 varchar(50),
    c11 varchar(50),
    c12 varchar(50),
    c13 varchar(50),
    c14 varchar(50),
    c15 varchar(50),
    c16 varchar(50),
    c17 varchar(50),
    ts TIMESTAMP default CURRENT_TIMESTAMP
    )
"""
