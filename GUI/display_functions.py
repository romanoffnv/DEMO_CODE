# Импортируем общие модули
from __init__ import *
from DC_settings import *



def display_df(screen_frame, message, pad_x, pad_y):
    tree = ttk.Treeview(screen_frame)
    tree.pack(padx = pad_x, pady = pad_y, fill = 'both', expand = True)
    style = ttk.Style()
    style.configure('Treeview.Heading', font = (None, 20))
    style.configure('Treeview.Heading')
    style.configure('Treeview', font = (None, 12))

    columns = list(message.columns)
    tree['columns'] = columns
    for col in columns:
        tree.heading(col, text = col, anchor = 'w')
        tree.column(col, anchor = 'w', width = 100)
    for index, row in message.iterrows():
        tree.insert('', 'end', values = list(row))

def display_text(screen_frame, message, parent, pad_x, pad_y):
    screen_styles = {
            'bg': '#F7F7F8',
            'fg': 'black',
            'font': ('Helvetica', 12), 
        }
    label = tk.Label(screen_frame, text = message, highlightthickness = 0)
    for option, value in screen_styles.items():
        label[option] = value
    label.pack(padx = pad_x, pady = pad_y)
    # Удаление сообщения с экрана после 3000 милли/сек
    parent.after(3000, label.destroy)

 # Функция построения графиков
def make_charts(screen_frame, sizes, labels, title, type_c, pad_x, pad_y):
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
    canvas = FigureCanvasTkAgg(fig, master = screen_frame)
    canvas.draw()

    # Упаковываем виджет canvas в screen_frame
    canvas.get_tk_widget().pack(fill = 'both', padx = pad_x, pady = pad_y, expand = True)

    # Реднеринг графиков на экране
    canvas.get_tk_widget().update_idletasks()  

def display_status_chart(screen_frame, message, pad_x, pad_y):
    pprint('triggered')
    # Построение графика 'Автомобили в сети'
    status_chart = message.iloc[:, 0]
    on_count = (status_chart ==  'online').sum()
    off_count = (status_chart ==  'offline').sum()
    
    labels = ['online', 'offline']
    sizes = [on_count, off_count]  
    title = 'Автомобили в сети'
    make_charts(screen_frame, sizes, labels, title, 'pie', pad_x, pad_y)

def display_urgency_chart(screen_frame, message, pad_x, pad_y):
    # Построение графика 'Распределение приоритетов заданий'
    urgency_chart = message.iloc[:, 1]
    lower_count = (urgency_chart ==  'низк').sum()
    mid_count = (urgency_chart ==  'сред').sum()
    hi_count = (urgency_chart ==  'выс').sum()
    
    labels = ['низк', 'сред', 'выс']
    sizes = [lower_count, mid_count, hi_count]  
    title = 'Распределение приоритетов заданий'
    make_charts(screen_frame, sizes, labels, title, 'donut', pad_x, pad_y)

def display_ratings_chart(screen_frame, message, pad_x, pad_y):
    # Построение графика 'Распределение рейтингов водителей'
    rating_chart = message.iloc[:, 2]
    hi = ((rating_chart.astype(float) < 5.0) & (rating_chart.astype(float) > 4.7)).sum()
    mid = ((rating_chart.astype(float) < 4.7) & (rating_chart.astype(float) > 4.2)).sum()
    under_mid = ((rating_chart.astype(float) < 4.2) & (rating_chart.astype(float) > 3.7)).sum()
    low = ((rating_chart.astype(float) < 3.7) & (rating_chart.astype(float) > 3.3)).sum()
    trash = ((rating_chart.astype(float) < 3.3) & (rating_chart.astype(float) > 0)).sum()
    
    labels = ['Высокий', 'Средний', 'Ниже среднего', 'Низкий', 'Увольнение']
    sizes = [hi, mid, under_mid, low, trash]
    title = 'Распределение рейтингов водителей'
    make_charts(screen_frame, sizes, labels, title, 'bar', pad_x, pad_y)
    
def display_map(screen_frame, message, pad_x, pad_y):
    df = message
    # Преобразуем координаты из типа данных 'строка' в тип 'кортеж'
    df['Coords'] = df['Coords'].apply(lambda coord_str: ast.literal_eval(coord_str))
    
    # Размещаем виджет 'Карта' на главном экране
    map_widget = tkintermapview.TkinterMapView(screen_frame, corner_radius = 0)
    map_widget.grid(row = 0, column = 0, sticky = 'nsew', padx = pad_x, pady = pad_y)  

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
              

  
