# Импортируем необходимые библиотеки для работы
import os.path # Для проверки наличия файла графика
import seaborn as sns # Для создания графика
import matplotlib.pyplot as plt # Для работы с графиком (ввиду зависимости Seaborn от Matplotlib)
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

# Строим простейший график в функцию которого передаем датафрейм
def simple_sns(df):
    t_s1 = datetime.datetime.now() # Задаем время начала работы функции
    if os.path.exists('simple_plots/simple_sns.png'): # Определяем условие обновления файла графика
        plt.clf()
        plt.close()
    splt = sns.relplot(data=df, kind='line') # Создаем график из датафрейма
    splt.savefig('simple_plots/simple_sns.png') # Сохраняем график в виде изображения
    t_s2 = datetime.datetime.now() # Задаем время окончания работы функции
    return f'{t_s2 - t_s1}' # Возвращаем время работы функции

# Строим усложненный график
def hard_sns(df_sns_h):
    t_s1 = datetime.datetime.now() # Задаем время начала работы функции
    if os.path.exists('complicated_plots/compl_sns.png'): # Определяем условие обновления файла графика
        plt.clf()
        plt.close()
    splt = sns.relplot(data=df_sns_h, kind='line') # Создаем график из датафрейма
    splt.savefig('complicated_plots/compl_sns.png') # Сохраняем график в виде изображения
    t_s2 = datetime.datetime.now() # Задаем время окончания работы функции
    return f'{t_s2 - t_s1}' # Возвращаем время работы функции
