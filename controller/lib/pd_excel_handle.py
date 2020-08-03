# -*- coding: utf-8 -*-

import pandas as pd

if __name__ == '__main__':
    file_path = "/Users/youdi/Desktop/20200721.xlsx"
    data_source = pd.read_excel(file_path, sheet_name='产能总表')
    data = data_source.iloc[2:, [2, 3, 4, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]]
    for i, row in data.iterrows():
        print(row.to_list())
