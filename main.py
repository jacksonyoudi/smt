import PySimpleGUI as sg

if __name__ == '__main__':
    sg.theme('Dark Blue 3')  # please make your windows colorful

    headings = ['HEADER 1', 'HEADER 2', 'HEADER 3', 'HEADER 4']
    header = [[sg.Text('  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]
    input_rows = [[sg.Input(size=(15, 1), pad=(0, 0)) for col in range(4)] for row in range(10)]

    layout = [[sg.Text('Rename files or folders')],
              [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(disabled=True), sg.FileBrowse()],
              [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(disabled=True), sg.FileBrowse()],
              [sg.Submit(), sg.Cancel()],
              ] + header + input_rows

    window = sg.Window('Rename Files or Folders', layout)

    event, values = window.read()
    window.close()
    folder_path, file_path = values[0], values[1]  # get the data from the values dictionary
    print(folder_path, file_path)
