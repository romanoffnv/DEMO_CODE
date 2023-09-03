from PROCESSOR._main import main as process
from GUI.display_functions import *
from __init__ import *
from DC_settings import *

import os
import sys


background_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))


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
        self.parent.grid_rowconfigure(1, weight=80)
        
        # Load the background image
        background_image_path = f"{background_dir}\\background.png"
        background_image = tk.PhotoImage(file=background_image_path)

        # Create a Label widget to display the background image
        background_label = tk.Label(self.screen_frame, bg=self.bg_main, image=background_image)
        background_label.image = background_image  # Keep a reference to the image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Make the label stack behind other widgets
        background_label.lower()

   

    def display_message(self, message, data_type):
       
        
        # Очищаем экран от контента
        if self.screen_frame is not None:
            for widget in self.screen_frame.winfo_children():
                widget.destroy()
        
        self.create_screen()
        
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
      
    
    
        

            
    