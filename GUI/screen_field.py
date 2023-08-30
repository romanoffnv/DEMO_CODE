from __init__ import *
from DC_settings import *

from PROCESSOR._main import main as process
from __init__ import *
from DC_settings import *

from PROCESSOR._main import main as process

class ScreenField:
    def __init__(self, parent, screen_frame):
        self.parent = parent
        self.screen_frame = screen_frame
        self.bg = 'darkgreen'
        self.screen_styles = {
            'bg': self.bg,
            "fg": "white",
            "font": ("Helvetica", 12), 
        }
        
    def apply_screen_style(self, widget, style):
        for option, value in style.items():
            widget[option] = value

    def create_screen(self):
        # Configure the height using the rowconfigure method
        self.parent.grid_rowconfigure(1, weight=22)  # Allow row 1 to expand

        # Create a label and add it to the screen_frame using pack
        label = tk.Label(self.screen_frame, text="", highlightthickness=0)  # Set highlightthickness to 0
        self.apply_screen_style(label, self.screen_styles)  # Use self.screen_styles directly
        label.pack(padx=20, pady=20, fill="both", expand=True)  

    def display_message(self, message, type, fade):
        pprint(type)
        # Clear any previous content from the screen_frame
        if self.screen_frame is not None:
            # Clear any previous content from the screen_frame
            for widget in self.screen_frame.winfo_children():
                widget.destroy()
      
        # if isinstance(message, pd.DataFrame):
        if type == 'df':
            try:
                tree = ttk.Treeview(self.screen_frame)
                tree.pack(padx=20, pady=20, fill="both", expand=True)
                style = ttk.Style()
                style.configure("Treeview.Heading", font=(None, 20))
                style.configure("Treeview.Heading", background=self.bg)
                style.configure("Treeview", background=self.bg, font=(None, 12))

                columns = list(message.columns)
                tree["columns"] = columns
                for col in columns:
                    tree.heading(col, text=col, anchor="w")
                    tree.column(col, anchor="w", width=100)

                for index, row in message.iterrows():
                    tree.insert("", "end", values=list(row))
            except Exception as e:
                print("Error:", e)

        if type == 'text':
            label = tk.Label(self.screen_frame, text=message, highlightthickness=0)
            self.apply_screen_style(label, self.screen_styles)
            label.pack(padx=20, pady=20)
        
        if type == 'chart_pie':
            # Example data
            labels = ['online', 'offline']
            sizes = [message[0], message[1]]  # Percentages for each category

            # Create a figure and axes
            fig, ax = plt.subplots()

            # Create a pie chart on the axes
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=240)
            ax.axis('equal')
            ax.set_title('Автомобили в сети')

            # Create a FigureCanvasTkAgg instance
            canvas = FigureCanvasTkAgg(fig, master=self.screen_frame)
            canvas.draw()

            # Pack the canvas widget into the screen_frame
            canvas.get_tk_widget().pack(fill="both", expand=True)

            # Display the chart
            canvas.get_tk_widget().update_idletasks()  # Ensure correct rendering

            # Close the Matplotlib figure to prevent pop-up window
            plt.close(fig)
        
        if type == 'chart_donut':
            # Example data
            labels = ['низк', 'сред', 'выс']
            sizes = [message[0], message[1], message[2]]  # Percentages for each category

            # Create a figure and axes
            fig, ax = plt.subplots()
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=240, pctdistance=0.85)
            ax.axis('equal')

            # Add a white circle to create the donut effect
            centre_circle = plt.Circle((0,0),0.70,fc='white')
            fig.gca().add_artist(centre_circle)

            # Add a title
            ax.set_title('Автомобили в сети')

            # Create a FigureCanvasTkAgg instance
            canvas = FigureCanvasTkAgg(fig, master=self.screen_frame)
            canvas.draw()

            # Pack the canvas widget into the screen_frame
            canvas.get_tk_widget().pack(fill="both", expand=True)

            # Display the chart
            canvas.get_tk_widget().update_idletasks()  # Ensure correct rendering
            
        # Schedule the destruction of the label after 2000 milliseconds
        if fade:
            self.parent.after(5000, label.destroy)

            
    