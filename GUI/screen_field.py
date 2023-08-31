from __init__ import *
from DC_settings import *

from PROCESSOR._main import main as process
from __init__ import *
from DC_settings import *



class ScreenField:
    '''Этот класс создает виджеты разных типов на главном экране'''
    def __init__(self, parent, screen_frame):
        self.parent = parent
        self.screen_frame = screen_frame
        self.bg = '#F7F7F8'
        self.screen_styles = {
            'bg': self.bg,
            'fg': 'black',
            'font': ('Helvetica', 12), 
        }
        self.pad_x = 40
        self.pad_y = 40
        
    def apply_screen_style(self, widget, style):
        for option, value in style.items():
            widget[option] = value

    def create_screen(self):
        # Определяем вес ряда для отображения расширяемого контента
        self.parent.grid_rowconfigure(1, weight = 10)  

        # Создаем внутренний фрейм для отображения контента и пакуем его с указанными параметрами
        label = tk.Label(self.screen_frame, text = '', highlightthickness = 0)  
        self.apply_screen_style(label, self.screen_styles)  
        label.pack(padx = self.pad_x, pady = self.pad_x, fill = 'both', expand = True)  

    # Функция построения графиков
    def make_charts(self, sizes, labels, title, type_c):
        fig, ax = plt.subplots()
        # Распределение параметров построения графиков по типам
        if type_c ==  'pie':
            wedges, texts, autotexts = ax.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle = 240)
        elif type_c ==  'donut':
            wedges, texts, autotexts = ax.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle = 240, pctdistance = 0.85)
            centre_circle = plt.Circle((0, 0), 0.70, fc = 'white')
            ax.add_artist(centre_circle)
        elif type_c ==  'bar':
            fig, ax = plt.subplots()
            x = np.arange(len(labels))
            width = 0.3  # Adjust the width as needed for spacing
            ax.bar(x, sizes, width = width)
            ax.set_xticks(x)
            ax.set_xticklabels(labels)

        # Общие параметры для всех графиков
        ax.set_title(title)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master = self.screen_frame)
        canvas.draw()

        # Упаковываем виджет canvas в screen_frame
        canvas.get_tk_widget().pack(fill = 'both', padx = 40, pady = 40, expand = True)

        # Реднеринг графиков на экране
        canvas.get_tk_widget().update_idletasks()  

    def display_message(self, message, data_type, fade):
        
        # Очищаем экран от контента
        if self.screen_frame is not None:
            for widget in self.screen_frame.winfo_children():
                widget.destroy()
      
        # Параметры отображения контента в зависимости от типа контента или графика
        if data_type ==  'df':
            tree = ttk.Treeview(self.screen_frame)
            tree.pack(padx = self.pad_x, pady = self.pad_x, fill = 'both', expand = True)
            style = ttk.Style()
            style.configure('Treeview.Heading', font = (None, 20))
            style.configure('Treeview.Heading', background = self.bg)
            style.configure('Treeview', background = self.bg, font = (None, 12))

            columns = list(message.columns)
            tree['columns'] = columns
            for col in columns:
                tree.heading(col, text = col, anchor = 'w')
                tree.column(col, anchor = 'w', width = 100)

            for index, row in message.iterrows():
                tree.insert('', 'end', values = list(row))
            
        if data_type ==  'text':
            label = tk.Label(self.screen_frame, text = message, highlightthickness = 0)
            self.apply_screen_style(label, self.screen_styles)
            label.pack(padx = self.pad_x, pady = self.pad_x)
        
        # Построение графика 'Автомобили в сети'
        if data_type ==  'status_chart':
            status_chart = message.iloc[:, 0]
            on_count = (status_chart ==  'online').sum()
            off_count = (status_chart ==  'offline').sum()
            
            
            labels = ['online', 'offline']
            sizes = [on_count, off_count]  
            title = 'Автомобили в сети'
            self.make_charts(sizes, labels, title, 'pie')

        # Построение графика 'Распределение приоритетов заданий'
        if data_type ==  'urgency_chart':
            urgency_chart = message.iloc[:, 1]
            lower_count = (urgency_chart ==  'низк').sum()
            mid_count = (urgency_chart ==  'сред').sum()
            hi_count = (urgency_chart ==  'выс').sum()
            
            labels = ['низк', 'сред', 'выс']
            sizes = [lower_count, mid_count, hi_count]  
            title = 'Распределение приоритетов заданий'
            self.make_charts(sizes, labels, title, 'donut')
        
        # Построение графика 'Распределение рейтингов водителей'
        if data_type ==  'ratings_chart':
            rating_chart = message.iloc[:, 2]
            hi = ((rating_chart.astype(float) < 5.0) & (rating_chart.astype(float) > 4.7)).sum()
            mid = ((rating_chart.astype(float) < 4.7) & (rating_chart.astype(float) > 4.2)).sum()
            under_mid = ((rating_chart.astype(float) < 4.2) & (rating_chart.astype(float) > 3.7)).sum()
            low = ((rating_chart.astype(float) < 3.7) & (rating_chart.astype(float) > 3.3)).sum()
            trash = ((rating_chart.astype(float) < 3.3) & (rating_chart.astype(float) > 0)).sum()
            
            labels = ['Высокий', 'Средний', 'Ниже среднего', 'Низкий', 'Увольнение']
            sizes = [hi, mid, under_mid, low, trash]
            title = 'Распределение рейтингов водителей'
            self.make_charts(sizes, labels, title, 'bar')
        

        if data_type ==  'map':
            df = message
            # Преобразуем координаты из типа данных 'строка' в тип 'кортеж'
            df['Coords'] = df['Coords'].apply(lambda coord_str: ast.literal_eval(coord_str))
            
            # Размещаем виджет 'Карта' на главном экране
            map_widget = tkintermapview.TkinterMapView(self.screen_frame, corner_radius = 0)
            map_widget.grid(row = 0, column = 0, sticky = 'nsew', padx = self.pad_x, pady = self.pad_x)  

            # Делаем ряд и колонку в grid адаптивными под расширяющийся контент
            self.screen_frame.grid_rowconfigure(0, weight = 1)  
            self.screen_frame.grid_columnconfigure(0, weight = 1) 

            # Центрируем карту на Красной площади
            map_widget.set_position(55.752673, 37.622668)
            map_widget.set_zoom(12)

            # Собираем координаты и маркеры в листы для назначения динамически
            lat, long, markers = [], [], []
            for coords in df['Coords']:
                lat.append(coords[0])
                long.append(coords[1])
            for i, j, unit, plate in zip(lat, long, df['Units'], df['Plates']):
                markers.append(map_widget.set_marker(i, j, text = unit + '\n' + plate))
            for i in markers:
                i.set_position(...)
            
        # Удаление сообщения с экрана после 5000 милли/сек
        if fade:
            self.parent.after(5000, label.destroy)

            
    