from __init__ import *
from DC_settings import *

from GUI.screen_field import ScreenField

class WarningField(ScreenField):
    def __init__(self, parent, screen_frame, warning_frame):
        super().__init__(parent, warning_frame)
        self.screen_frame = warning_frame
        self.bg = 'darkblue'
        



