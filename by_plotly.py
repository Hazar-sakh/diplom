import os
import plotly.graph_objs as go
import datetime


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
    if os.path.exists('simple_plt.png'):
        os.remove('simple_plt.png')
    name = 'simple_plt'
    fig.write_image(f'{name}.png')
    t_ptl2 = datetime.datetime.now()
    return f'{t_ptl2 - t_ptl1}'


def hard_ptl(period, stat_h):
    t_ptl1 = datetime.datetime.now()
    fig = go.Figure()
    for i in stat_h:
        fig.add_trace(go.Scatter(x=period, y=i, mode='lines'))
    if os.path.exists('complicated_plt.png'):
        os.remove('complicated_plt.png')
    name = 'complicated_plt'
    fig.write_image(f'{name}.png')
    t_ptl2 = datetime.datetime.now()
    return f'{t_ptl2 - t_ptl1}'