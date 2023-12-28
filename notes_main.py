#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
                            QPushButton, QLabel, QLineEdit, QListWidget, QTextEdit, QInputDialog)
import json

'''notes = {
    'Добро пожаловать!' : {
        'текст' : 'текст заметки',
        'теги' : ['тег1','тег2']
    }
}
with open('notes_data.json', 'w', encoding='UTF-8') as file:
    json.dump(notes, file)'''

app = QApplication([])
notes_win = QWidget()
notes_win.setWindowTitle('Глупые черкасики')
notes_win.resize(900,1000)

field_text = QTextEdit()
list_notes_label = QLabel('Список черкасиков:')
list_notes = QListWidget()

button_note_create = QPushButton('Черкануть свежую запись')
button_note_del = QPushButton('Изгнать запись из компа')
button_note_save = QPushButton('Оставить эту запись себе')

list_tags_label = QLabel('Перечень tagов')
list_tags = QListWidget()
field_tag = QLineEdit()
field_tag.setPlaceholderText('Черканите tag сюда')
button_tag_add = QPushButton('Сделать новый tag')
button_tag_del = QPushButton('Убить tag')
button_tag_search = QPushButton('Вычислить tag')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)
col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1)
layout_notes.addLayout(col_2)

notes_win.setLayout(layout_notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])

def add_note():
    note_name, ok =QInputDialog.getText(notes_win, "Добавить заметку", "Название заметки")
    if ok and note_name != "":
        notes[note_name] = {"текст": "", "теги": []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["теги"])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = field_text.toPlainText()
        with open("notes_data.json", "w", encoding = "utf-8") as f:
            json.dump(notes, f, sort_keys=True, ensure_ascii=False)

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("notes_data.json", "w", encoding = "utf-8") as f:
            json.dump(notes, f, sort_keys=True, ensure_ascii=False)

def add_tag():
    if list_notes.selectedItems:
        key = list_notes.selectedItems()[0].text()



list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_del.clicked.connect(del_note)
button_note_save.clicked.connect(save_note)


list_notes.itemClicked.connect(show_note)

with open('notes_data.json', 'r', encoding='UTF-8') as file:
    notes = json.load(file)
list_notes.addItems(notes)






























notes_win.show()
app.exec()