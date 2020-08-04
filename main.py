# -*- coding: utf-8 -*-

import PySimpleGUI as sg
from model.db import insert_ct_data, parse_acv_data, parse_report_data
from model.acv import get_acv, delete_acv_by_id
import sqlite3
import csv
import datetime
import os

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

if __name__ == '__main__':
    db_file = "./first.db"
    conn = sqlite3.connect(db_file)

    sg.theme('Dark Blue 3')  # please make your windows colorful
    gen_lines = list(lines.keys())

    one_line = [sg.Text("数据处理:", size=(10, 3)),
                sg.Combo(gen_lines, size=(30, 10), default_value='选择生产线', key='gen_line', auto_size_text=True,
                         pad=((2, 2), (2, 2))),
                sg.Input(key='acv_file', enable_events=True, visible=False),
                sg.FileBrowse("导入ACV数据", target='acv_file', size=(20, 2), key="import_acv_csv", enable_events=True)]
    two_line = [sg.Text("表格操作:", size=(10, 3)), sg.Input(key='import_report_file', enable_events=True, visible=False),
                sg.FileBrowse("导入报表", target='import_report_file', size=(20, 2), key="import_report_table",
                              enable_events=True),

                sg.Input(key='export_report_path', enable_events=True, visible=False),
                sg.FolderBrowse("导出报表", target='export_report_path', size=(20, 2), key='export_table',
                                enable_events=True)]
    three_line = [sg.Text("CT设置:", size=(10, 2)), sg.Input(key='ct_file', enable_events=True, visible=False),
                  sg.FileBrowse("导入CT设置表", target='ct_file', size=(20, 2), key="import_ct_xlsm", enable_events=True),
                  sg.Button("导出CT设置表", size=(20, 2))]

    # header = [[sg.Text('  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]
    # input_rows = [[sg.Input(size=(15, 1), pad=(0, 0)) for col in range(4)] for row in range(10)]

    headings = [
        'id', '机种', '品番', '工单号', '面番', '批量',
        '开始时间', '结束时间', '标准CT(秒)', '理论时间',
        '实际时间', '可动率', '短暂停时间(分钟)', '短暂停回数',
        '故障停时间(分钟)',
        '故障备注', '换线时间', '导入时间']

    # headings = ['id', 'jizhong', 'pinfan', 'gongdanhao', 'mianfan', 'piliang', 'kaishi_shijian', 'jieshu_shijian',
    #             'biaozhun_ct', 'lilun_shijian', 'shiji_shijian', 'kedong_lv', 'duanzanting_shijian', 'duanzanting_huishu', 'guzhangting_shijian',
    #             'guzhang_beizhu','huanxian_shijian','daoru_shijian',
    #             'gen_line']
    data = get_acv(conn)
    if len(data) == 0:
        data = [headings]

    layout = [[sg.Text('SMT', size=(20, 2))],
              one_line,
              two_line,
              three_line,
              [sg.Text("明细数据:", size=(10, 3), auto_size_text=True),
               sg.Button("删除数据", key="delete_table_row", enable_events=True)],
              [sg.Table(values=data,
                        headings=headings,
                        enable_events=True,
                        justification='center',
                        display_row_numbers=True,
                        num_rows=1000,
                        col_widths=[1000 for i in headings],
                        font='Courier 14',
                        key='_table_',
                        text_color='red',
                        alternating_row_color='green',
                        max_col_width=8000
                        )]
              ]

    window = sg.Window(
        'SMT',
        layout,
        resizable=True,
        # auto_size_text=True,
        # auto_size_buttons=True,
        # size=(1000, 1600)
    )

    while True:
        event, values = window.read()
        print(event, values)
        if event == 'acv_file':
            gen_line_key = values.get("gen_line")
            import_acv_csv = values.get("import_acv_csv")
            parse_acv_data(import_acv_csv, gen_line_key, conn)
            sg.popup("导入成功")
            data = get_acv(conn)
            window.Element('_table_').Update(data)
            sg.popup("页面已刷新")

        if event == 'delete_table_row':
            # if event == '_table_':
            select_index = values.get("_table_")[0]
            row = window.Element('_table_').Values[select_index]
            data = window.Element('_table_').Values
            delete_acv_by_id(conn, row[0])
            sg.popup("删除成功")
            result = get_acv(conn)
            window.Element('_table_').Update(result)
            sg.popup("页面已刷新")

        if event == 'ct_file':
            ct_file = values.get('ct_file')
            insert_ct_data(conn, ct_file)
            sg.popup("导入成功")

        if event == 'report_file':
            report_table = values.get('import_report_table')

        if event == 'export_table':
            pass

        if event == 'export_report_path':
            export_report_path = values.get("export_report_path")
            if export_report_path:
                file_path = os.path.join(export_report_path,
                                         "export_tab_{}.csv".format(datetime.datetime.now().strftime("%Y%m%d")))
                result = get_acv(conn)
                with open(file_path, 'w') as f:
                    f_csv = csv.writer(f)
                    f_csv.writerow(headings[1:])
                    for row in result:
                        f_csv.writerow(row[1:])
                sg.popup("导出成功!")
            else:
                sg.popup("请选择一个合法的目录!")

        if event == 'import_report_file':
            import_report_file = values.get('import_report_file')
            if import_report_file:
                parse_report_data(import_report_file, conn)
                sg.popup("导入成功")
                result = get_acv(conn)
                window.Element('_table_').Update(result)
                sg.popup("页面已刷新")
            else:
                sg.popup("请选择一个合法的文件!")

        if event == sg.WIN_CLOSED or event == 'Cancel':
            conn.close()
            break
    window.close()
