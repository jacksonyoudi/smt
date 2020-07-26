# -*- coding: utf-8 -*-

import PySimpleGUI as sg

if __name__ == '__main__':
    sg.theme('Dark Blue 3')  # please make your windows colorful

    headings = ['HEADER 1', 'HEADER 2', 'HEADER 3', 'HEADER 4']

    gen_lines = ["EPS {i}#".format(i=i) for i in range(1, 17)]

    one_line = [sg.Text("数据处理:"), sg.Combo(gen_lines), sg.Button("导入ACV数据")]
    two_line = [sg.Text("导入报表:"), sg.Button("导入报表", ), sg.Button("导出报表")]
    three_line = [sg.Text("CT设置:"), sg.Button("导入CT设置表"),
                  sg.Button("导出CT设置表")]

    header = [[sg.Text('  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]
    input_rows = [[sg.Input(size=(15, 1), pad=(0, 0)) for col in range(4)] for row in range(10)]

    layout = [[sg.Text('Rename files or folders')],
              one_line,
              two_line,
              three_line,
              [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(disabled=True), sg.FileBrowse()],
              [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(disabled=True), sg.FileBrowse()],
              [sg.Submit(), sg.Cancel()],
              ] + header + input_rows

    window = sg.Window('Rename Files or Folders', layout, size=(1000, 800), auto_size_text=True, auto_size_buttons=True)

    event, values = window.read()
    window.close()
    folder_path, file_path = values[0], values[1]  # get the data from the values dictionary
    print(folder_path, file_path)
