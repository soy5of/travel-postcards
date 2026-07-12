from aiogram.fsm.state import State, StatesGroup


class TripStates(StatesGroup):
    waiting_for_trip_code = State()
    choosing_destination = State()