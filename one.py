import PySimpleGUI as sg


if __name__ == '__main__':
    layout = [
        [sg.Text('Name1', size=(15, 1), background_color="white" ), sg.InputText()],
        [sg.Text('Name2', size=(15, 1), background_color="white" ), sg.InputText()],
        [sg.Text('Name3', size=(15, 1), background_color="white" ), sg.InputText()],

        [sg.Submit(), sg.Cancel()]
    ]

window = sg.Window('Test', layout, background_color="white")
event, values = window.Read()
window.Close()

if event == 'Submit':
    try:
        name_file = input('Name:')
        file= open(name_file, 'r+')
    except FileNotFoundError:
        file= open(name_file, 'w+')

    all_values = values.values() # values from dictionary
    text = "\n".join(all_values) # put values in separated lines
    file.write(text)             # write all as one string

    file.close()