from __init__ import *
from DC_settings import *

from PROCESSOR._main import main as process
from __init__ import *
from DC_settings import *



class ScreenField:
    def __init__(self, parent, screen_frame):
        self.parent = parent
        self.screen_frame = screen_frame
        self.bg = 'darkgreen'
        self.screen_styles = {
            'bg': self.bg,
            "fg": "black",
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
        
        if type == 'status_chart':
            status_chart = message.iloc[:, 0]
            on_count = (status_chart == 'online').sum()
            off_count = (status_chart == 'offline').sum()
            pprint(f'works great {status_chart}')
            pprint(f'works + {on_count}')
            # Example data
            labels = ['online', 'offline']
            sizes = [on_count, off_count]  # Percentages for each category

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
        
        if type == 'urgency_chart':
            urgency_chart = message.iloc[:, 1]
            lower_count = (urgency_chart == 'низк').sum()
            mid_count = (urgency_chart == 'сред').sum()
            hi_count = (urgency_chart == 'выс').sum()
            
            # Example data
            labels = ['низк', 'сред', 'выс']
            sizes = [lower_count, mid_count, hi_count]  # Percentages for each category

            # Create a figure and axes
            fig, ax = plt.subplots()
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=240, pctdistance=0.85)
            ax.axis('equal')

            # Add a white circle to create the donut effect
            centre_circle = plt.Circle((0,0),0.70,fc='white')
            fig.gca().add_artist(centre_circle)

            # Add a title
            ax.set_title('Распределение приоритетов заданий')

            # Create a FigureCanvasTkAgg instance
            canvas = FigureCanvasTkAgg(fig, master=self.screen_frame)
            canvas.draw()

            # Pack the canvas widget into the screen_frame
            canvas.get_tk_widget().pack(fill="both", expand=True)

            # Display the chart
            canvas.get_tk_widget().update_idletasks()  # Ensure correct rendering
        
        if type == 'ratings_chart':
            rating_chart = message.iloc[:, 2]
            hi = ((rating_chart.astype(float) < 5.0) & (rating_chart.astype(float) > 4.7)).sum()
            mid = ((rating_chart.astype(float) < 4.7) & (rating_chart.astype(float) > 4.2)).sum()
            under_mid = ((rating_chart.astype(float) < 4.2) & (rating_chart.astype(float) > 3.7)).sum()
            low = ((rating_chart.astype(float) < 3.7) & (rating_chart.astype(float) > 3.3)).sum()
            trash = ((rating_chart.astype(float) < 3.3) & (rating_chart.astype(float) > 0)).sum()
            
            labels = ['Высокий', 'Средний', 'Ниже среднего', 'Низкий', 'Увольнение']
            sizes = [hi, mid, under_mid, low, trash]
            
            fig, ax = plt.subplots()
            x = np.arange(len(labels))
            width = 0.3  # Adjust the width as needed for spacing
            ax.bar(x, sizes, width=width)
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            ax.set_title('Распределение рейтингов водителей')
            plt.tight_layout()

            canvas = FigureCanvasTkAgg(fig, master=self.screen_frame)
            canvas.draw()

            # Pack the canvas widget into the screen_frame
            canvas.get_tk_widget().pack(fill="both", padx=40, pady=40, expand=True)

            # Display the chart
            canvas.get_tk_widget().update_idletasks()  # Ensure correct rendering

        if fade:
            self.parent.after(5000, label.destroy)

            
    