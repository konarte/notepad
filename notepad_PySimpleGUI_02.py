import PySimpleGUI as sg

# Создаем раскладку интерфейса окна блокнота
layout = [
    [sg.Multiline(size=(80, 20), key='-TEXT-')],
    [sg.Button('Сохранить'), sg.Button('Открыть'), sg.Button('Выход')]
]

# Создаем окно с указанной раскладкой
window = sg.Window('Блокнот', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Выход':
        break
    elif event == 'Сохранить':
        # Получаем текст из многострочного поля
        text = values['-TEXT-']
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
                # Устанавливаем текст в многострочное поле
                window['-TEXT-'].update(value=text)

# Закрываем окно приложения
window.close()
