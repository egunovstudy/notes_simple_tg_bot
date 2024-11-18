from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

add_note_btn = InlineKeyboardButton(text='Добавить заметку', callback_data='add_note_btn_pressed')
delete_note_btn = InlineKeyboardButton(text='Удалить заметку', callback_data='delete_note_btn_pressed')
show_notes_btn = InlineKeyboardButton(text='Показать мои заметки', callback_data='show_notes_btn_pressed')

menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [add_note_btn], [delete_note_btn], [show_notes_btn]
])
