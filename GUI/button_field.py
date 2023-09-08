import tkinter as tk

from PROCESSOR._main import main as process
from PROCESSOR.sql_requests import main as sql_requests
from PROCESSOR.src1_api_get import main as api




class ButtonField:
    '''Класс ButtonField создает панель кнопок, и назначает им функционал'''
    def __init__(self, parent, ScreenField):
        self.parent = parent
        self.screen_field = ScreenField  
        
    # Применяем стили к кнопкам
    def apply_button_style(self, widget, style):
        for option, value in style.items():
            widget[option] = value

    def create_buttons(self, button_frame):
        btns = ['Данные', 'Отчет', 'Карта', 'Статус', 'Важность', 'Рейтинги']

        # Определяем размер самой широкой кнопки 
        widest_width = max(len(btn) for btn in btns)
        
        
        for i, btn in enumerate(btns):
            # Выравниваем кнопки по ширине самой широкой кнопки 
            button = tk.Button(button_frame, text = btn, width = widest_width)
            
            # Применяем стили к кнопкам
            self.apply_button_style(button, self.get_button_styles())
            # Применяем параметры позиционирования к кнопкам
            button.grid(row = 0, column = i, pady = 30)
            
            # Применяем функционал к кнопкам
            if i ==  0:
                button.config(command = self.on_data_click)
            elif i ==  1:
                button.config(command = self.on_rep_click)
            elif i ==  2:
                button.config(command = self.on_map_click)
            elif i ==  3:
                button.config(command = self.on_status_click)
            elif i ==  4:
                button.config(command = self.on_priority_click)
            elif i ==  5:
                button.config(command = self.on_rating_click)
        
        # Применяем веса к рядам/колонкам для адаптивности верстки
        self.parent.grid_rowconfigure(0, weight = 1)
        for i in range(len(btns)):
            button_frame.grid_columnconfigure(i, weight = 1)

    def get_button_styles(self):
        button_styles = {
            'bg': '#0078d7',
            'fg': 'white',
            'font': ('Helvetica', 12),
            'highlightbackground': '#1E1E1E',
            'highlightcolor': '#3498DB',
            'highlightthickness': 2,
        }
        return button_styles

    # Фукнции кнопок on_click   
    def on_data_click(self):
        process()
        connection = api()
        if connection != 0:
            self.screen_field.display_message('База данных обновлена', data_type = 'text')
        else:
            self.screen_field.display_message('База данных не обновлена. Проверьте подключение к интернету', data_type = 'text')
        
    def on_rep_click(self):
        userrep = sql_requests()
        self.screen_field.display_message(userrep[0], data_type = 'df')
        
    def on_map_click(self):
        geo_map = sql_requests()
        self.screen_field.display_message(geo_map[1], data_type = 'map')
    
    def on_status_click(self):
        status_chart = sql_requests()
        self.screen_field.display_message(status_chart[2], data_type = 'status_chart')
    
    def on_priority_click(self):
        urgency_chart = sql_requests()
        self.screen_field.display_message(urgency_chart[2], data_type = 'urgency_chart')
        
    def on_rating_click(self):
        ratings_chart = sql_requests()
        self.screen_field.display_message(ratings_chart[2], 'ratings_chart')
        
        