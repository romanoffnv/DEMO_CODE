import numpy as np
import tkinter as tk
from tkinter import ttk
# from PIL import ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkintermapview 
import ast


def display_df(screen_frame, message):
    tree = ttk.Treeview(screen_frame, show = 'headings')
    tree.pack(padx = 40, pady = 40, fill = 'both', expand = True)
    style = ttk.Style()
    style.configure('Treeview.Heading', font = (None, 20))
    style.configure('Treeview', font = (None, 12))

    columns = list(message.columns)
    tree['columns'] = columns
    for col in columns:
        tree.heading(col, text = col, anchor = 'w')
        tree.column(col, anchor = 'w', width = 100)
    for row in message.itertuples(index=False):
        tree.insert('', 'end', values = list(row))

def display_text(screen_frame, message, parent):
    screen_styles = {
            'bg': '#666',
            'fg': 'white',
            'font': ('Helvetica', 12), 
        }
    label = tk.Label(screen_frame, text = message, highlightthickness = 0)
    for option, value in screen_styles.items():
        label[option] = value
    label.pack(padx = 40, pady = 40)
    # Удаление сообщения с экрана после 3000 милли/сек
    parent.after(3000, label.destroy)

# Функция построения графиков
def make_charts(screen_frame, config):
    sizes = config['sizes']
    labels = config['labels']
    type_c = config['type_c']
    title = config['title']
    
    
    fig, ax = plt.subplots()
    # Распределение параметров построения графиков по типам
    if type_c ==  'pie':
        ax.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle = 240)
    elif type_c ==  'donut':
        ax.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle = 240, pctdistance = 0.85)
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
    canvas = FigureCanvasTkAgg(fig, master = screen_frame)
    canvas.draw()

    # Упаковываем виджет canvas в screen_frame
    canvas.get_tk_widget().pack(fill = 'both', padx = 40, pady = 40, expand = True)

    # Реднеринг графиков на экране
    canvas.get_tk_widget().update_idletasks()  

def display_status_chart(screen_frame, message):
    # Построение графика 'Автомобили в сети'
    status_chart = message.iloc[:, 0]
    on_count = (status_chart ==  'online').sum()
    off_count = (status_chart ==  'offline').sum()
    
    config = {
    'sizes': [on_count, off_count],
    'labels': ['online', 'offline'],
    'title': 'Автомобили в сети',
    'type_c': 'pie',
    }
    make_charts(screen_frame, config)

def display_urgency_chart(screen_frame, message):
    # Построение графика 'Распределение приоритетов заданий'
    urgency_chart = message.iloc[:, 1]
    lower_count = (urgency_chart ==  'низк').sum()
    mid_count = (urgency_chart ==  'сред').sum()
    hi_count = (urgency_chart ==  'выс').sum()
    
    config = {
    'sizes': [lower_count, mid_count, hi_count],
    'labels': ['низк', 'сред', 'выс'],
    'title': 'Распределение приоритетов заданий',
    'type_c': 'donut',
    }
    make_charts(screen_frame, config)

def display_ratings_chart(screen_frame, message):
    # Построение графика 'Распределение рейтингов водителей'
    rating_chart = message.iloc[:, 2]
    hi = ((rating_chart.astype(float) < 5.0) & (rating_chart.astype(float) > 4.7)).sum()
    mid = ((rating_chart.astype(float) < 4.7) & (rating_chart.astype(float) > 4.2)).sum()
    under_mid = ((rating_chart.astype(float) < 4.2) & (rating_chart.astype(float) > 3.7)).sum()
    low = ((rating_chart.astype(float) < 3.7) & (rating_chart.astype(float) > 3.3)).sum()
    trash = ((rating_chart.astype(float) < 3.3) & (rating_chart.astype(float) > 0)).sum()
    
    config = {
    'sizes': [hi, mid, under_mid, low, trash],
    'labels': ['Высокий', 'Средний', 'Ниже среднего', 'Низкий', 'Увольнение'],
    'title': 'Распределение рейтингов водителей',
    'type_c': 'bar',
    }
    make_charts(screen_frame, config)
    
    
def display_map(screen_frame, message):
    df = message
    # Преобразуем координаты из типа данных 'строка' в тип 'кортеж'
    df['Coords'] = df['Coords'].apply(lambda coord_str: ast.literal_eval(coord_str))
    
    # Размещаем виджет 'Карта' на главном экране
    map_widget = tkintermapview.TkinterMapView(screen_frame, corner_radius = 0)
    map_widget.grid(row = 0, column = 0, sticky = 'nsew', padx = 40, pady = 40)  

    # Делаем ряд и колонку в grid адаптивными под расширяющийся контент
    screen_frame.grid_rowconfigure(0, weight = 1)  
    screen_frame.grid_columnconfigure(0, weight = 1) 

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
              

  
