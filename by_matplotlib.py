import os.path
import matplotlib.pyplot as plt
import datetime

# period - период для представления
# norm_name - название нормы
# norm_nums - список значений нормы по количеству периодов
# name - название объекта представления
# stat - статистика объекта представления


# Строим простейшую таблицу
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

# Строим усложненную таблицу
def hard_mpl(period, statH):
    row = []
    for i in statH:
        print(i)
        m = [int(j) for j in i if i.index(j) > 1]
        print(m)



    # t_mpl1 = datetime.datetime.now()
    # if os.path.exists('simple_plots/simple_mpl.png'):
    #     plt.clf()
    #     plt.close()
    # plt.plot(period, stat)
    # plt.plot(period, norm_nums)
    # plt.savefig('simple_plots/simple_mpl.png')
    # t_mpl2 = datetime.datetime.now()
    # return f'{t_mpl2 - t_mpl1}'
