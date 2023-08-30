from __init__ import *
from DC_settings import *

from PROCESSOR._main import main as process
from PROCESSOR.sql_requests import main as sql_requests
from GUI.screen_field import ScreenField
from GUI.warning_field import WarningField




class ButtonField:
    def __init__(self, parent, ScreenField, WarningField):
        self.parent = parent
        self.screen_field = ScreenField  # Store the screen_field instance
        self.warning_field = WarningField  # Store the screen_field instance
        

    def apply_button_style(self, widget, style):
        for option, value in style.items():
            widget[option] = value

    def create_buttons(self, button_frame):
        btns = ['Данные', 'Отчет', 'Карта', 'Статус', 'Важность', 'Рейтинги']

        # Determine the widest button width
        widest_width = max(len(btn) for btn in btns)
        
        # Loop through the buttons
        for i, btn in enumerate(btns):
            # Apply the widest width to all buttons
            button = tk.Button(button_frame, text=btn, width=widest_width)
            
            # Apply the styles
            self.apply_button_style(button, self.get_button_styles())
            # Apply the positioning to the buttons
            button.grid(row=0, column=i, pady=20)
            
            # Apply functionality to the buttons
            if i == 0:
                button.config(command=self.on_data_click)
            elif i == 1:
                button.config(command=self.on_rep_click)
            elif i == 2:
                button.config(command=self.on_map_click)
            elif i == 3:
                button.config(command=self.on_status_click)
            elif i == 4:
                button.config(command=self.on_priority_click)
            elif i == 5:
                button.config(command=self.on_rating_click)
        
        # Configure grid row/column weights for responsiveness
        self.parent.grid_rowconfigure(0, weight=1)
        for i in range(len(btns)):
            button_frame.grid_columnconfigure(i, weight=1)

    def get_button_styles(self):
        button_styles = {
            "bg": "#2E86C1",
            "fg": "white",
            "font": ("Helvetica", 12),
            "highlightbackground": "#1E1E1E",
            "highlightcolor": "#3498DB",
            "highlightthickness": 2,
            "relief": "ridge"
        }
        return button_styles
        
    def on_data_click(self):
        process()
        self.screen_field.display_message('', type='text', fade = False)
        self.warning_field.display_message('База данных обновлена', type='text', fade = True)
        
    def on_rep_click(self):
        userrep = sql_requests()
        self.screen_field.display_message(userrep[0], type='df', fade = False)
        self.warning_field.display_message('Report Anomalies', type='text', fade = False)
        
    def on_map_click(self):
        userrep = sql_requests()
        self.screen_field.display_message(userrep[0], type='map', fade = False)
        self.warning_field.display_message('', type='text', fade = False)
    
    def on_status_click(self):
        status_chart = sql_requests()
        self.screen_field.display_message(status_chart[1], type = 'status_chart', fade = False)
        self.warning_field.display_message('', type='text', fade = False)
    
    def on_priority_click(self):
        urgency_chart = sql_requests()
        self.screen_field.display_message(urgency_chart[1], type = 'urgency_chart', fade = False)
        self.warning_field.display_message('', type='text', fade = False)
        
    def on_rating_click(self):
        ratings_chart = sql_requests()
        self.screen_field.display_message(ratings_chart[1], 'ratings_chart', fade = False)
        self.warning_field.display_message('', type='text', fade = False)
        

