import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
background_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *

from GUI.button_field import ButtonField
from GUI.screen_field import ScreenField


class MainApplication:
    '''Класс определяет параметры окна и верстку элементов GUI'''
    def __init__(self, root, background_image_path=None):
        self.root = root
        self.root.title('DEMO CODE')
        self.root.state('zoomed')
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.bg_button = '#202123'
        self.bg_main = '#666'
        self.layout()

    

    def layout(self):
        # Определяем фреймы элементов GUI
        button_frame = tk.Frame(self.root, width=self.screen_width, height=self.screen_height * 0.1, bg=self.bg_button)
        button_frame.grid(row=0, column=0, sticky='nsew')
        screen_frame = tk.Frame(self.root, width=self.screen_width, height=self.screen_height * 0.9, bg=self.bg_main)
        screen_frame.grid(row=1, column=0, sticky='nsew')

        # Определяем веса для каждого ряда в grid, влияющих на размер фрейма по высоте
        self.root.grid_rowconfigure(0, weight=5)  # button_frame
        self.root.grid_rowconfigure(1, weight=0)  # screen_frame

        # Определяем вес для колонки в grid
        self.root.grid_columnconfigure(0, weight=1)

        # Инициируем и запускаем классы
        screen_field = ScreenField(self.root, screen_frame, self.bg_main)
        button_field = ButtonField(self.root, screen_field)
        button_field.create_buttons(button_frame)
        screen_field.create_screen()

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ ==  '__main__':
    main()
    start_time = time.time()
    pprint('--- %s seconds ---' % (time.time() - start_time))
