import os
import shutil
import plotly.graph_objs as go
from plotly.offline import plot
import datetime
from time import sleep
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
    plot(fig, image='png')
    t_ptl2 = datetime.datetime.now()
    sleep(3)
    shutil.move('C:/Users/Hazar/Downloads/plot_image.png',
                'C:/Users/Hazar/Desktop/Python/Dplm/simple_plots/simple_plt.png')
    print(f'Plotly: {t_ptl2 - t_ptl1}')
