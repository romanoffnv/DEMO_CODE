# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *

from GUI.button_field import ButtonField
from GUI.screen_field import ScreenField
from GUI.warning_field import WarningField

class MainApplication:
    def __init__(self, root):
        self.root = root
        # self.bg = '#1E1E1E'
        self.bg = 'blue'
        self.root.title("DEMO CODE")
        self.root.state("zoomed")
        self.root.configure(bg=self.bg)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.height = 50
        self.layout()
    
    def layout(self):
        button_frame = tk.Frame(self.root, width = self.screen_width, height = self.height, bg='darkred')
        button_frame.grid(row=0, column=0, sticky="nsew")
        screen_frame = tk.Frame(self.root, width=self.screen_width, height=self.height * 10, bg='darkgreen')  # Customize background color as needed
        screen_frame.grid(row=1, column=0, sticky="nsew")
        warning_frame = tk.Frame(self.root, width=self.screen_width, height=self.height * 2, bg='darkblue')  # Customize background color as needed
        warning_frame.grid(row=2, column=0, sticky="nsew")
        
         # Configure row and column weights
        self.root.grid_rowconfigure(0, weight=0)  # First row (button_frame)
        self.root.grid_rowconfigure(1, weight=1)  # Second row (screen_frame)
        self.root.grid_rowconfigure(2, weight=0)  # Third row (warning_frame)
        
        self.root.grid_columnconfigure(0, weight=1)  # First column
        
        screen_field = ScreenField(self.root, screen_frame)
        warning_field = WarningField(self.root, screen_frame, warning_frame)
        button_field = ButtonField(self.root, screen_field, warning_field)  # Pass the screen_field instance
        button_field.create_buttons(button_frame)
        screen_field.create_screen()
        warning_field.create_screen()
        
  
       

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
