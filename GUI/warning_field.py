from __init__ import *
from DC_settings import *

from GUI.screen_field import ScreenField


class WarningField:
    def __init__(self, parent):
        self.parent = parent
        self.screen_frame = None  # Initialize screen_frame attribute

    def apply_screen_style(self, widget, style):
        for option, value in style.items():
            widget[option] = value

    def create_screen(self):
        self.screen_frame = tk.Frame(self.parent, width=500, height=50, bg='darkblue')  # Set height to 50
        self.screen_frame.pack(fill="both", expand=False, padx=0, pady=0)  # Disable expansion

        # Create a label and add it to the screen_frame using pack
        label = tk.Label(self.screen_frame, text="", highlightthickness=0)  # Set highlightthickness to 0
        self.apply_screen_style(label, self.get_screen_styles())
        label.pack(padx=20, pady=20)  # Adjust padding as needed

       
    def get_screen_styles(self):
        screen_styles = {
            'bg': 'darkblue',
            "fg": "white",
            "font": ("Helvetica", 12),
        }
        return screen_styles

    def display_message(self, message):
        pprint(message)
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
        self.parent.after(5000, label.destroy)
    


def main():
    root = tk.Tk()

    # Create instances of both ScreenField and WarningField
    screen_app = ScreenField(root)
    warning_app = WarningField(root)

    # Create main grid layout
    screen_app.create_screen()
    warning_app.create_screen()

    root.mainloop()

if __name__ == '__main__':
    main()

