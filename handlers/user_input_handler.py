from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.menu_keyboard import menu_kb
from states.notes_states import NotesState

router = Router()


@router.message(CommandStart())
async def start_bot(m: Message, state: FSMContext):
    await state.set_state(NotesState.default_state)
    await m.answer('Привет я бот заметок. Выбери действие', reply_markup=menu_kb)


@router.callback_query(lambda cb: cb.data == 'add_note_btn_pressed')
async def add_note_btn_pressed(cb: CallbackQuery, state: FSMContext):
    await cb.message.answer('Введите текст заметки')
    await state.set_state(NotesState.add_note_state)


@router.message(StateFilter('NotesState:add_note_state'))
async def add_note(message: Message, state: FSMContext):
    notes = await state.get_value('notes', [])
    notes.append(message.text)
    await state.update_data(notes=notes)
    await message.answer(f'Заметка {message.text} добавлена')
    await start_bot(message, state)


@router.callback_query(lambda cb: cb.data == 'delete_note_btn_pressed')
async def delete_note_btn_pressed(cb: CallbackQuery, state: FSMContext):
    await state.set_state(NotesState.delete_note_state)
    notes = await state.get_value('notes', [])
    keys = [[InlineKeyboardButton(text=note, callback_data=note)] for note in notes]

    notes_kb = InlineKeyboardMarkup(
        inline_keyboard=keys
    )
    await cb.message.answer(text='Выберите заметку для удаления', reply_markup=notes_kb)


@router.callback_query(StateFilter('NotesState:delete_note_state'))
async def delete_note(cb: CallbackQuery, state: FSMContext):
    notes = await state.get_value('notes', [])
    notes.remove(cb.data)
    await state.update_data(notes=notes)
    await cb.message.answer(f'Заметка {cb.data} удалена')
    await start_bot(cb.message, state)


@router.callback_query(lambda cb: cb.data == 'show_notes_btn_pressed')
async def show_notes(cb: CallbackQuery, state: FSMContext):
    notes = await state.get_value('notes', [])
    keys = [[InlineKeyboardButton(text=note, callback_data=note)] for note in notes]

    notes_kb = InlineKeyboardMarkup(
        inline_keyboard=keys
    )
    await cb.message.answer(text='Ваши заметки', reply_markup=notes_kb)
