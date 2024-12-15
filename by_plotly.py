import os
import plotly.graph_objs as go
import datetime
# from excel_reader import *


# period - период для представления
# norm_name - название нормы
# norm_nums - список значений нормы по количеству периодов
# name - название объекта представления
# stat - статистика объекта представления


def simple_ptl(period, norm_nums, stat):
    t_ptl1 = datetime.datetime.now()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=period, y=norm_nums, mode='lines'))
    fig.add_trace(go.Scatter(x=period, y=stat, mode='lines'))
    if not os.path.exists('simple_plots/'):
        os.mkdir('simple_plots/')
    dirs = os.listdir('simple_plots')
    name = max(int(filename) for filename in dirs) + 1 if dirs else 0
    fig.write_image(f'simple_plots/{name}.png')
    t_ptl2 = datetime.datetime.now()
    return f'{t_ptl2 - t_ptl1}'