# Импортируем общие модули
from __init__ import *
from DC_settings import *

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