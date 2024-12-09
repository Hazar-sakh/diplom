import matplotlib.pyplot as plt
import datetime
from excel_reader import *

# period - период для представления
# norm_name - название нормы
# norm_nums - список значений нормы по количеству периодов
# name - название объекта представления
# stat - статистика объекта представления


# Строим простейшую таблицу
def simple_mpl():
    t_mpl1 = datetime.datetime.now()
    plt.plot(period, stat)
    plt.plot(period, norm_nums)
    plt.savefig('simple_plots/simple_mpl.png')
    t_mpl2 = datetime.datetime.now()
    print(f'Matplotlib: {t_mpl2 - t_mpl1}')