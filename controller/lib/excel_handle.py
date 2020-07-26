# -*- coding: utf-8 -*-

from openpyxl import load_workbook

if __name__ == '__main__':
    wb = load_workbook(filename="/Users/youdi/Documents/20200721.xlsm")
    sheet = wb["产能总表"]
    for i in sheet.iter_rows():
        
        print(i[2], i[4], i[5], i[44:60])
