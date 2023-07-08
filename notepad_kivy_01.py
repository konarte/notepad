# Import necessary modules
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView

class NotepadApp(App):
    def build(self):
        self.notes = {}  # Dictionary to store notes
        self.current_note_id = None  # Track the ID of the currently loaded note

        layout = BoxLayout(orientation='vertical')

        # Create horizontal layout for note selection buttons
        note_buttons_layout = BoxLayout(orientation='horizontal')

        # Create toggle buttons for note selection
        self.note_buttons = {}
        for note_id in self.notes:
            button = ToggleButton(text=str(note_id), group='notes')
            button.bind(on_press=self.load_note)
            self.note_buttons[note_id] = button
            note_buttons_layout.add_widget(button)

        # Create scrollable container for notes
        scroll_view = ScrollView()

        # Create layout for note input
        note_input_layout = BoxLayout(orientation='vertical')

        # Create text input for note content
        self.note_input = TextInput()

        # Create button to save note
        save_button = Button(text='Save')
        save_button.bind(on_press=self.save_note)

        # Create label for status messages
        self.status_label = Label(text='')

        note_input_layout.add_widget(self.note_input)
        note_input_layout.add_widget(save_button)
        note_input_layout.add_widget(self.status_label)

        scroll_view.add_widget(note_input_layout)

        layout.add_widget(note_buttons_layout)
        layout.add_widget(scroll_view)

        return layout

    def load_saved_notes(self):
        for file_name in os.listdir():
            if file_name.startswith('note') and file_name.endswith('.txt'):
                note_id = int(file_name[4:-4])
                try:
                    with open(file_name, 'r', encoding='utf-8') as file:
                        content = file.read()
                        self.notes[note_id] = content

                        button = ToggleButton(text=str(note_id), group='notes')
                        button.bind(on_press=self.load_note)
                        self.note_buttons[note_id] = button

                        self.root.children[0].add_widget(button)
                except Exception as e:
                    print(f'Error loading note {note_id}: {e}')

    def load_note(self, instance):
        note_id = int(instance.text)
        self.note_input.text = self.notes[note_id]
        self.current_note_id = note_id

    def save_note(self, instance):
        note_content = self.note_input.text

        if self.current_note_id is None:
            # Create a new note
            note_id = len(self.notes) + 1
            self.notes[note_id] = note_content

            button = ToggleButton(text=str(note_id), group='notes')
            button.bind(on_press=self.load_note)
            self.note_buttons[note_id] = button

            self.root.children[0].add_widget(button)

            file_name = f'note{note_id}.txt'
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(note_content)
                self.status_label.text = f'Note {note_id} saved.'
            except Exception as e:
                print(f'Error saving note {note_id}: {e}')

        else:
            # Update an existing note
            note_id = self.current_note_id
            self.notes[note_id] = note_content

            file_name = f'note{note_id}.txt'
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(note_content)
                self.status_label.text = f'Note {note_id} updated.'
            except Exception as e:
                print(f'Error updating note {note_id}: {e}')

    def on_stop(self):
        # Save notes to files when the app is closed
        for note_id, content in self.notes.items():
            file_name = f'note{note_id}.txt'
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(content)
            except Exception as e:
                print(f'Error saving note {note_id}: {e}')
    def on_start(self):
        # Load saved notes when the app starts
        self.load_saved_notes()

# Run the app
if __name__ == '__main__':
    NotepadApp().run()
