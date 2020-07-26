import PySimpleGUI as sg
import csv

if __name__ == '__main__':
    sg.theme('Dark Brown 1')
    headings = None
    input_rows = []
    with open('gdp.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            headings = list(row.keys())

            r = [sg.Input(
                size=(15, 2),
                pad=(1, 1),
                default_text=col,
                disabled=True,
                text_color='black'
            ) for col in list(row.values())]
            r.append(sg.Input(



            ))

            input_rows.append(r)

    header = [[sg.Text('  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]

    layout = header + input_rows

    window = sg.Window('Table Simulation', layout, font='Courier 12')
    event, values = window.read()
