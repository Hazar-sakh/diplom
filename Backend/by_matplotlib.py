# Импортируем необходимые библиотеки для работы
import os.path # Для проверки наличия файла графика
import matplotlib.pyplot as plt # Для работы с графиком
import datetime # Для измерения времени работы
import numpy as np

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
def simple_mpl(period, norm_nums, stat):
    t_mpl1 = datetime.datetime.now() # Задаем время начала работы функции
    if os.path.exists('simple_plots/simple_mpl.png'): # Определяем условие обновления файла графика
        plt.clf()
        plt.close()
    plt.plot(period, stat) # Добавляем линию статистики
    plt.plot(period, norm_nums) # Добавляем линию нормы
    plt.savefig('simple_plots/simple_mpl.png') # Сохраняем график в виде изображения
    t_mpl2 = datetime.datetime.now() # Задаем время окончания работы функции
    return f'{t_mpl2 - t_mpl1}' # Возвращаем время работы функции

# Строим усложненный график в функцию которого передаем значения периода и статистики
def hard_mpl(period, stat_h):
    t_mpl1 = datetime.datetime.now() # Задаем время начала работы функции
    if os.path.exists('complicated_plots/compl_mpl.png'): # Определяем условие обновления файла графика
        plt.clf()
        plt.close()
    for i in stat_h: # Добавляем все линии циклом for для каждого списка из списка статистки
        plt.plot(period, i)
    plt.savefig('complicated_plots/compl_mpl.png') # Сохраняем график в виде графического изображения
    t_mpl2 = datetime.datetime.now() # Задаем время окончания работы функции
    return f'{t_mpl2 - t_mpl1}' # Возвращаем время работы функции

def demo_mpl(cs_type, period, stat, name, norm_nums):
    if os.path.exists('demo_plot/demo.jpg'):  # Определяем условие обновления файла графика
        plt.clf()
        plt.close()
    if cs_type == 0:
        plt.bar(period, stat)
        plt.xlabel('Период')
        plt.ylabel('Количество')
        plt.title(f'Столбчатая диаграмма\n({name})')
    elif cs_type == 1:
        plt.pie(stat, labels=period)
        plt.title(f"Распределение по периодам\n({name})")
    elif cs_type == 2:
        x = period
        ay = stat
        by = norm_nums
        y = np.vstack([ay, by])
        fig, ax = plt.subplots()
        ax.stackplot(x, y)
        plt.title(f"С накоплением\n({name})")
    plt.savefig('demo_plot/demo.jpg')  # Сохраняем график в виде изображения
