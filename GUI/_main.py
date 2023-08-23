# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *

from button_field import ButtonField
from screen_field import ScreenField

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("DEMO CODE")
        self.root.state("zoomed")
        self.root.configure(bg='#1E1E1E')
        self.controller()
        
    def controller(self):
        button_field = ButtonField(self.root)
        button_field.create_buttons()
        screen_field = ScreenField(self.root)
        screen_field.create_screen()
        
        

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
