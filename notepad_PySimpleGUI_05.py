import PySimpleGUI as sg

tabs = []  # List to store tab elements
tab_contents = {}  # Dictionary to store tab contents

# Create a new tab with a unique key
def create_tab(tab_name='Вкладка '+ str(len(tabs)+1), text='text_key'):
    text_key = f'-TEXT{len(tabs)+1}-'
    tab_layout = [[sg.Multiline(size=(80, 20), key=text_key, default_text=text)]]
    tab = sg.Tab(tab_name, tab_layout, key=text_key, element_justification='center')
    tabs.append(tab)
    tab_contents[text_key] = text
    window[text_key].Widget.grid_forget()
    window[text_key].update(value=tab_contents[text_key])
    return text_key

window = sg.Window('Блокнот', layout)
layout = [[sg.TabGroup([tabs])],[sg.Button('Добавить вкладку'), sg.Button('Сохранить'), sg.Button('Открыть'), sg.Button('Выход')]
]
# Create the initial tab
text_key = create_tab()





while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Выход':
        break
    elif event == 'Добавить вкладку':
        # Create a new tab
        text_key = create_tab()
        #window[text_key].Widget.grid_forget()
        #window[text_key].update(value=tab_contents[text_key])
    elif event == 'Сохранить':
        # Get the content of the active tab
        text = values[text_key]
        # Show a save file dialog
        filename = sg.popup_get_file('Сохранить как', save_as=True)
        # If a filename is provided, save the text to the file
        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(text)
                sg.popup('Файл сохранен.')
    elif event == 'Открыть':
        # Show an open file dialog
        filename = sg.popup_get_file('Открыть файл')
        # If a filename is provided, open the file and add a new tab with its content
        if filename:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
                text_key = create_tab(tab_name=filename, text=text)
                window[text_key].Widget.grid_forget()
                window[text_key].update(value=tab_contents[text_key])

# Save the content of each tab when exiting the program
for tab_key in tab_contents:
    text = values[tab_key]
    filename = f'{tab_key[1:]}.txt'  # Generate a filename based on the tab key
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

window.close()
