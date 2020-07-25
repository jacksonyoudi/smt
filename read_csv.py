import PySimpleGUI as sg
import csv

if __name__ == '__main__':
    sg.theme('Dark Brown 1')




    headings = ['HEADER 1', 'HEADER 2', 'HEADER 3', 'HEADER 4']
    header = [[sg.Text('  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]

    input_rows = [[sg.Input(
        size=(15, 2),
        pad=(1, 1),
        default_text="hello",
        disabled=True,
        text_color='black'

    ) for col in range(4)] for row
        in range(10)]

    layout = header + input_rows

    window = sg.Window('Table Simulation', layout, font='Courier 12')
    event, values = window.read()
