from aiogram.fsm.state import State, StatesGroup


class NotesState(StatesGroup):
    default_state = State('default_state')
    add_note_state = State('add_note_state')
    delete_note_state = State('delete_note_state')
