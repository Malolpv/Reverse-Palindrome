from datetime import datetime


class Clock:
    _time: int

    def __init__(self):
        self._time = datetime.now().hour

    def set_time(self, time):
        self._time = time
        return self

    @property
    def time(self):
        return self._time
