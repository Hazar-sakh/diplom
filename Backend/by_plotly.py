# Импортируем необходимые библиотеки для работы
import os.path # Для проверки наличия файла графика

import plotly.graph_objs as go # Для работы с графиком
import datetime # Для измерения времени работы

# V V V Создаем для удобства список глобальных переменных, которыми будем пользоваться
# period - период для представления
# norm_name - название нормы
# norm_nums - список значений нормы по количеству периодов
# name - название объекта представления
# stat - статистика объекта представления
# stat_h - статистика объектов представления всех параметров
# df - датафрейм для простого графика Seaborn
# df_sns_h - датафрейм для усложненного графика Seaborn

# Строим простейший график в функцию которого передаем значения периода, нормы и статистики
def simple_ptl(period, norm_nums, stat):
    t_ptl1 = datetime.datetime.now() # Задаем время начала работы функции
    fig = go.Figure() # Определяем переменную графика
    fig.add_trace(go.Scatter(x=period, y=norm_nums, mode='lines')) # Добавляем линию нормы
    fig.add_trace(go.Scatter(x=period, y=stat, mode='lines')) # Добавляем линию статистики
    if not os.path.exists('simple_plots/'): # Определяем условие создания директории
        os.mkdir('simple_plots/')
        if os.path.exists('simple_plots/simple_plt.png'): # Определяем условие обновления (через удаление) файла графика
            os.remove('simple_plots/simple_plt.png')
    name = 'simple_plt' # Задаем имя графика
    fig.write_image(f'simple_plots/{name}.png') # Сохраняем график в виде изображения
    t_ptl2 = datetime.datetime.now() # Задаем время окончания работы функции
    return f'{t_ptl2 - t_ptl1}' # Возвращаем время работы функции


def hard_ptl(period, stat_h):
    t_ptl1 = datetime.datetime.now() # Задаем время начала работы функции
    fig = go.Figure() # Определяем переменную графика
    for i in stat_h: # Циклом for создаем линии графика для каждого параметра
        fig.add_trace(go.Scatter(x=period, y=i, mode='lines'))
    if not os.path.exists('complicated_plots/'): # Определяем условие создания директории
        os.mkdir('complicated_plots/')
        if os.path.exists('complicated_plots/complicated_plt.png'): # Определяем условие обновления (через удаление) файла графика
            os.remove('complicated_plots/complicated_plt.png')
    name = 'complicated_plt' # Задаем имя графика
    fig.write_image(f'complicated_plots/{name}.png') # Сохраняем график в виде изображения
    t_ptl2 = datetime.datetime.now() # Задаем время окончания работы функции
    return f'{t_ptl2 - t_ptl1}' # Возвращаем время работы функции


def demo_ptl(cs_type, period, stat_h, names):
    fig = go.Figure()
    if cs_type == 0:
        for i in stat_h:
            if stat_h.index(i) <= 2:
                fig.add_trace(go.Bar(x=period, y=i, name=f'Показатель {stat_h.index(i)}'))
        fig.update_layout(title='Столбчатый с наложением', barmode='stack')
    if cs_type == 1:
        fig.add_trace(go.Pie(values=stat_h[0], labels=period, hole=0.8))
        fig.update_layout(title=f'Круговая \n({names[0]})', barmode='stack',
                          annotations=[dict(text=f'Выдано за все время {sum(stat_h[0])}', x=0.5, y=0.5, font_size=16,
                                            showarrow=False)])
    if cs_type == 2:
        for i in stat_h:
            if stat_h.index(i) <= 2:
                fig.add_trace(go.Scatter(x=period, y=i, name=f'Показатель {stat_h.index(i)}', mode='lines+markers',
                                         marker=dict(symbol='diamond')))
        fig.update_layout(title='Интерактивный')
        fig.show()
    name = 'demo'  # Задаем имя графика
    fig.write_image(f'demo_plot/{name}.png')  # Сохраняем график в виде изображения
