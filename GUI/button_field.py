from __init__ import *
from DC_settings import *

from PROCESSOR._main import main as process
from GUI.screen_field import ScreenField
from GUI.warning_field import WarningField



class ButtonField:
    def __init__(self, parent, ScreenField, WarningField):
        self.parent = parent
        self.screen_field = ScreenField  # Store the screen_field instance
        self.warning_field = WarningField  # Store the screen_field instance

    def apply_button_style(self, widget, style):
        for option, value in style.items():
            widget[option] = value

    def create_buttons(self):
        btns = ['Данные', 'Отчет', 'Карта', 'Статус', 'Важность', 'Рейтинги']

        # Determine the widest button width
        widest_width = max(len(btn) for btn in btns)

        # Create a container frame for the buttons
        # #1E1E1E
        button_frame = tk.Frame(self.parent, bg='blue')
        button_frame.pack(side="top", pady=10)

        # Loop thru the buttons
        for i, btn in enumerate(btns):
            # Apply the widest width to all buttons
            button = tk.Button(button_frame, text=btn, width=widest_width)
            # Apply the styles
            self.apply_button_style(button, self.get_button_styles())
            # Apply the positioning to the buttons
            button.grid(row=0, column=i, padx=5)  
            
            # Apply functionality to the buttons
            if i == 0:
                button.config(command=self.on_data_button_click)
        
        # Configure grid row/column weights for responsiveness
        self.parent.grid_rowconfigure(0, weight=1)
        for i in range(len(btns)):
            button_frame.grid_columnconfigure(i, weight=1)

    def get_button_styles(self):
        button_styles = {
            "bg": "#2E86C1",
            "fg": "white",
            "font": ("Helvetica", 12),
            "highlightbackground": "#1E1E1E",
            "highlightcolor": "#3498DB",
            "highlightthickness": 2,
            "relief": "ridge"
        }
        return button_styles


        
    def on_data_button_click(self):
        process()
        # self.screen_field.display_message('message')
        self.warning_field.display_message('База данных обновлена')
        
        
        

        
def main():
    root = tk.Tk()
    app = ButtonField(root)
    app.create_buttons()  # Call the create_buttons method
    root.mainloop()

if __name__ == '__main__':
    main()

