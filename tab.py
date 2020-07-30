import PySimpleGUI as sg

import random
import string

"""
  This sample code shows how to use a Table Element to create and display a Table in PySimpleGUIWeb.  You'll learn how to make a table, display it, and how to get "events" back when items are clicked
"""


# ------------------ Create a fake table ------------------
class Fake():
    @classmethod
    def word(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    @classmethod
    def number(self, max=1000):
        return random.randint(0, max)


def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [Fake.word() for _ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [Fake.word(), *[Fake.number() for i in range(num_cols - 1)]]
    return data


if __name__ == '__main__':
    # table_data has our actual table data to be displayed
    table_data = make_table(num_rows=15, num_cols=6)
    headings = table_data[0]
    # ------------------ Create a window layout ------------------
    # Attempt  made to show all functioning parms to Table Element in PySimpleGUIWeb
    layout = [[sg.Table(values=table_data,
                        headings=headings,
                        enable_events=True,
                        display_row_numbers=True,
                        font='Courier 14',
                        key='_table_',
                        text_color='red',
                        pad=((1, 1), (1, 1))
                        )],
              [sg.Button('Exit')],
              [sg.T('Selected rows = '), sg.T('', size=(30, 1), key='_selected_rows_')],
              [sg.T('Selected value = '), sg.T('', size=(30, 1), key='_selected_value_')]]

    # ------------------ Create the window ------------------
    window = sg.Window('Table Element Example').Layout(layout)

    # ------------------ The Event Loop ------------------
    while True:
        event, values = window.Read()
        print(event, values)
        if event in (None, 'Exit'):
            break
        window.Element('_selected_rows_').Update(values['_table_'])
        window.Element('_selected_value_').Update(window.Element('_table_').SelectedItem)
    # ------------------ User closed window so exit ------------------
    window.Close()
