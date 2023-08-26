from __init__ import *
from DC_settings import *

class ScreenField:
    def __init__(self, parent):
        self.parent = parent
        self.screen_frame = None  # Initialize screen_frame attribute

    def apply_screen_style(self, widget, style):
        for option, value in style.items():
            widget[option] = value

    def create_screen(self):
        self.screen_frame = tk.Frame(self.parent, width=500, height=600, bg='darkgreen')  # Customize background color as needed
        self.screen_frame.pack(fill="both", expand=True, padx=0, pady=0)  # Fill and expand to take all available space

        # Create a label and add it to the screen_frame using pack
        label = tk.Label(self.screen_frame, text="", highlightthickness=0)  # Set highlightthickness to 0
        self.apply_screen_style(label, self.get_screen_styles())
        label.pack(padx=20, pady=20)

       
    def get_screen_styles(self):
        screen_styles = {
            'bg': 'green',
            "fg": "white",
            "font": ("Helvetica", 12),
        }
        return screen_styles

    def display_message(self, message):
        # Clear any previous content from the screen_frame
        if self.screen_frame is not None:
            # Clear any previous content from the screen_frame
            for widget in self.screen_frame.winfo_children():
                widget.destroy()

        # Create a label to display the message and pack it into screen_frame
        label = tk.Label(self.screen_frame, text=message, highlightthickness=0)
        self.apply_screen_style(label, self.get_screen_styles())
        label.pack(padx=20, pady=20)
    


def main():
    root = tk.Tk()
    app = ScreenField(root)
    app.create_screen()
    root.mainloop()

if __name__ == '__main__':
    main()

