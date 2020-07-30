# -*- coding: utf-8 -*-

import PySimpleGUI as sg
from controller.lib.csv_handle import parse_csv

if __name__ == '__main__':
    sg.theme('Dark Blue 3')  # please make your windows colorful
    gen_lines = ["EPS {i}#".format(i=i) for i in range(1, 17)]

    one_line = [sg.Text("数据处理:", size=(30, 1)),
                sg.Combo(gen_lines, size=(20, 1), default_value='选择生产线', key='gen_line'),
                sg.Input(key='acv_file', enable_events=True, visible=False),
                sg.FileBrowse("导入ACV数据", target='acv_file', size=(20, 1), key="import_acv_csv", enable_events=True)]
    two_line = [sg.Text("导入报表:", size=(30, 1)), sg.Button("导入报表", size=(20, 1)), sg.Button("导出报表", size=(20, 1))]
    three_line = [sg.Text("CT设置:", size=(30, 1)), sg.Button("导入CT设置表", size=(20, 1)),
                  sg.Button("导出CT设置表", size=(20, 1))]

    # header = [[sg.Text('  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]
    # input_rows = [[sg.Input(size=(15, 1), pad=(0, 0)) for col in range(4)] for row in range(10)]

    headings = ['17700004012603522-201G6433997B', '', '', 'R70', '', 'R2', '', 'C158', '', 'R69', '', 'R3', '', 'IC8',
                '', 'IC3', '', 'D11', '', 'L5', '', 'C150', '', 'C100', '']

    layout = [[sg.Text('Rename files or folders')],
              one_line,
              two_line,
              three_line,
              [sg.Table(values=[headings],
                        headings=headings,
                        enable_events=True,
                        display_row_numbers=True,
                        key='_table_',
                        text_color='red',
                        pad=((1, 1), (1, 1))
                        )]
              ]

    window = sg.Window('Rename Files or Folders', layout, resizable=True, auto_size_text=True, auto_size_buttons=True)

    while True:
        event, values = window.read()
        print(event, values)
        if event == 'acv_file':
            gen_line = values.get("gen_line")
            import_acv_csv = values.get("import_acv_csv")
            header, data = parse_csv(import_acv_csv)

            window.Element('_table_').Update(data)

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
    window.close()
