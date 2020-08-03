# -*- coding: utf-8 -*-
import pandas as pd

if __name__ == '__main__':
    file_path = "/Users/youdi/Desktop/20200721.xlsm"
    data_source = pd.read_excel(file_path, sheet_name='产能总表')
    data = data_source.iloc[2:, [2, 4, 5, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]]
    for i, row in data.iterrows():
        item = row.to_list()
        if item[0] != item[0] or item[1] != item[1] or item[2] != item[2]:
            continue
        print(item)


def parse_excel_by_pd(file_path):
    data_source = pd.read_excel(file_path, sheet_name='产能总表')
    data = data_source.iloc[2:, [2, 4, 5, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]]

    datas = []
    for i, row in data.iterrows():
        item = row.to_list()
        if item[1] != item[1] or item[2] != item[2]:
            continue
        for j in range(4, 20):
            if item[j] != item[j]:
                item[j] = 0.0
        datas.append(item)
    return datas
