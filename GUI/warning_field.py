from __init__ import *
from DC_settings import *

from GUI.screen_field import ScreenField


class WarningField(ScreenField):
    ''' Класс WarningField наследуется от класса ScreenField модуля screen_field.py и служит как экран оповещений '''
    def __init__(self, parent, screen_frame, warning_frame):
        super().__init__(parent, warning_frame)
        self.screen_frame = warning_frame
        self.bg = '#96A4A4'
        self.screen_styles = {
            'bg': self.bg,
            "fg": "white",
            "font": ("Helvetica", 12), 
        }
    
        
        



