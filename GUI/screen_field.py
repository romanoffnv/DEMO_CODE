from __init__ import *
from DC_settings import *

from PROCESSOR._main import main as process
class ScreenField:
    def __init__(self, parent, screen_frame):
        self.parent = parent
        self.screen_frame = screen_frame
        self.bg = 'darkgreen'

    def apply_screen_style(self, widget, style):
        for option, value in style.items():
            widget[option] = value

    def create_screen(self):
        # Configure the height using the rowconfigure method
        self.parent.grid_rowconfigure(1, weight=22)  # Allow row 1 to expand

        # Create a label and add it to the screen_frame using pack
        label = tk.Label(self.screen_frame, text="", highlightthickness=0)  # Set highlightthickness to 0
        self.apply_screen_style(label, self.get_screen_styles())
        label.pack(padx=20, pady=20, fill="both", expand=True)  
       
    def get_screen_styles(self):
        screen_styles = {
            'bg': self.bg,
            "fg": "white",
            "font": ("Helvetica", 12),
        }
        return screen_styles

    def display_message(self, message, fade):
        # Clear any previous content from the screen_frame
        if self.screen_frame is not None:
            # Clear any previous content from the screen_frame
            for widget in self.screen_frame.winfo_children():
                widget.destroy()

        # Create a label to display the message and pack it into screen_frame
        label = tk.Label(self.screen_frame, text=message, highlightthickness=0)
        self.apply_screen_style(label, self.get_screen_styles())
        label.pack(padx=20, pady=20)
        
        # Schedule the destruction of the label after 2000 milliseconds
        if fade:
            self.parent.after(5000, label.destroy)
            

