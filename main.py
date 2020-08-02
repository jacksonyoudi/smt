# -*- coding: utf-8 -*-

import PySimpleGUI as sg
from controller.lib.csv_handle import parse_csv

if __name__ == '__main__':
    sg.theme('Dark Blue 3')  # please make your windows colorful
    gen_lines = ["EPS {i}#".format(i=i) for i in range(1, 17)]

    one_line = [sg.Text("数据处理:", size=(10, 3)),
                sg.Combo(gen_lines, size=(30, 10), default_value='选择生产线', key='gen_line', auto_size_text=True,
                         pad=((2, 2), (2, 2))),
                sg.Input(key='acv_file', enable_events=True, visible=False),
                sg.FileBrowse("导入ACV数据", target='acv_file', size=(20, 2), key="import_acv_csv", enable_events=True)]
    two_line = [sg.Text("导入报表:", size=(10, 2), auto_size_text=True), sg.Button("导入报表", size=(20, 2)),
                sg.Button("导出报表", size=(20, 2))]
    three_line = [sg.Text("CT设置:", size=(10, 2)), sg.Button("导入CT设置表", size=(20, 2)),
                  sg.Button("导出CT设置表", size=(20, 2))]

    # header = [[sg.Text('  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]
    # input_rows = [[sg.Input(size=(15, 1), pad=(0, 0)) for col in range(4)] for row in range(10)]

    headings = ['机种', '品番', '工单号', '面番', '批量', '开始时间', '结束时间', '标准CT(秒)', '理论时间', '实际时间', '可动率', '短暂停时间(分钟)', '短暂停回数',
                '故障停时间(分钟)',
                '故障备注', '换线时间', '导入时间', '操作']

    layout = [[sg.Text('SMT', size=(20, 2))],
              one_line,
              two_line,
              three_line,
              [sg.Text("明细数据:", size=(10, 3), auto_size_text=True)],
              [sg.Table(values=[headings, headings, headings],
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
            gen_line = values.get("gen_line")
            import_acv_csv = values.get("import_acv_csv")
            header, data = parse_csv(import_acv_csv)

            window.Element('_table_').Update(data)

        if event == '_table_':
            select_index = values.get("_table_")[0]
            row = window.Element('_table_').Values[select_index]
            data = window.Element('_table_').Values
            data.remove(row)
            window.Element('_table_').Update(data)
            sg.popup("删除成功")

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
    window.close()
