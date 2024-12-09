import plotly.graph_objs as go
import datetime
from excel_reader import *


# period - период для представления
# norm_name - название нормы
# norm_nums - список значений нормы по количеству периодов
# name - название объекта представления
# stat - статистика объекта представления


def simple_ptl():
    t_ptl1 = datetime.datetime.now()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=period, y=norm_nums, mode='lines'))
    fig.add_trace(go.Scatter(x=period, y=stat, mode='lines'))
    fig.write_image('simple_plots/simple_mpl.png')
    t_ptl2 = datetime.datetime.now()
    print(f'Plotly: {t_ptl2 - t_ptl1}')