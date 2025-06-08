from aiogram.fsm.state import StatesGroup, State

class BillStates(StatesGroup):
    amount = State()
    photo = State()

class Abstract(StatesGroup):
    temp = State()

