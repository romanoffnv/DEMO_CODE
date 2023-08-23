from __init__ import *
from DC_settings import *

class ScreenField:
    def __init__(self, parent):
        self.parent = parent

    def apply_screen_style(self, widget, style):
        for option, value in style.items():
            widget[option] = value

    def create_screen(self):
        screen_frame = tk.Frame(self.parent, bg='black')  # Customize background color as needed
        screen_frame.pack(fill="both", expand=True, padx=0, pady=10)  # Fill and expand to take all available space
        
        # Add your content to the screen_frame here
        label = tk.Label(screen_frame, highlightthickness=0)  # Set highlightthickness to 0
        self.apply_screen_style(label, self.get_screen_styles())
       
    def get_screen_styles(self):
        screen_styles = {
            # 'bg': 'black',
            "fg": "white",
            "font": ("Helvetica", 12),
        }
        return screen_styles

    def display_message(self, message):
        # Clear any previous content from the screen_frame
        for widget in self.screen_frame.winfo_children():
            widget.destroy()

        # Create a label to display the message
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

