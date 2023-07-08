import PySimpleGUI as sg

# Создаем раскладку интерфейса окна блокнота с вкладками
layout = [
    [sg.TabGroup([[sg.Tab('Вкладка 1', [[sg.Multiline(size=(80, 20), key='-TEXT1-')]])],
                  [sg.Tab('Вкладка 2', [[sg.Multiline(size=(80, 20), key='-TEXT2-')]])]])],
    [sg.Button('Сохранить'), sg.Button('Открыть'), sg.Button('Выход')]
]

# Создаем окно с указанной раскладкой
window = sg.Window('Блокнот', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Выход':
        break
    elif event == 'Сохранить':
        # Получаем текст из активной вкладки
        text = values['-TEXT1-'] if window['Вкладка 1'].get() else values['-TEXT2-']
        # Вызываем диалоговое окно для выбора файла для сохранения
        filename = sg.popup_get_file('Сохранить как', save_as=True)
        # Если имя файла не пустое, сохраняем текст в файл
        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(text)
                sg.popup('Файл сохранен.')
    elif event == 'Открыть':
        # Вызываем диалоговое окно для выбора файла для открытия
        filename = sg.popup_get_file('Открыть файл')
        # Если имя файла не пустое, открываем файл и читаем его содержимое
        if filename:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
                # Устанавливаем текст в активную вкладку
                if window['Вкладка 1'].get():
                    window['-TEXT1-'].update(value=text)
                else:
                    window['-TEXT2-'].update(value=text)

# Закрываем окно приложения
window.close()
