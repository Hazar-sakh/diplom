import os.path
import matplotlib.pyplot as plt
import datetime

# period - период для представления
# norm_name - название нормы
# norm_nums - список значений нормы по количеству периодов
# name - название объекта представления
# stat - статистика объекта представления


# Строим простейший график
def simple_mpl(period, norm_nums, stat):
    t_mpl1 = datetime.datetime.now()
    if os.path.exists('simple_plots/simple_mpl.png'):
        plt.clf()
        plt.close()
    plt.plot(period, stat)
    plt.plot(period, norm_nums)
    plt.savefig('simple_plots/simple_mpl.png')
    t_mpl2 = datetime.datetime.now()
    return f'{t_mpl2 - t_mpl1}'

# Строим усложненный график
def hard_mpl(period, stat_h):
    t_mpl1 = datetime.datetime.now()
    if os.path.exists('complicated_plots/compl_mpl.png'):
        plt.clf()
        plt.close()
    for i in stat_h:
        plt.plot(period, i)
    plt.savefig('complicated_plots/compl_mpl.png')
    t_mpl2 = datetime.datetime.now()
    return f'{t_mpl2 - t_mpl1}'
