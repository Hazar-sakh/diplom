# Импортируем необходимые библиотеки для работы
import os.path # Для проверки наличия файла графика
import matplotlib.pyplot as plt # Для работы с графиком
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
