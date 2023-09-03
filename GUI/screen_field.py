from PROCESSOR._main import main as process
from GUI.display_functions import *
from __init__ import *
from DC_settings import *



class ScreenField():
    '''Этот класс создает виджеты разных типов на главном экране'''
    def __init__(self, parent, screen_frame, bg_main):
        self.parent = parent
        self.bg_main = bg_main
        self.screen_frame = screen_frame
        self.pad_x = 40
        self.pad_y = 40
        
    
    def create_screen(self):
        # Определяем вес ряда для отображения расширяемого контента
        self.parent.grid_rowconfigure(1, weight = 80)  

        # Создаем внутренний фрейм для отображения контента и пакуем его с указанными параметрами
        label = tk.Label(self.screen_frame, text = '', highlightthickness = 0)  
        label.configure(bg=self.bg_main)
        label.pack(padx = self.pad_x, pady = self.pad_x, fill = 'both', expand = True)  

   

    def display_message(self, message, data_type):
        
        # Очищаем экран от контента
        if self.screen_frame is not None:
            for widget in self.screen_frame.winfo_children():
                widget.destroy()
        
        if data_type == 'df':
            display_df(self.screen_frame, message, self.pad_x, self.pad_y)
        elif data_type == 'text':
            display_text(self.screen_frame, message, self.parent, self.pad_x, self.pad_y)
        elif data_type == 'status_chart':
            display_status_chart(self.screen_frame, message, self.pad_x, self.pad_y)
        elif data_type == 'urgency_chart':
            display_urgency_chart(self.screen_frame, message, self.pad_x, self.pad_y)
        elif data_type == 'ratings_chart':
            display_ratings_chart(self.screen_frame, message, self.pad_x, self.pad_y)
        elif data_type == 'map':
            display_map(self.screen_frame, message, self.pad_x, self.pad_y)
      
    
    
        

            
    