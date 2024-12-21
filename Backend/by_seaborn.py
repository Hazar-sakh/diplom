# Импортируем необходимые библиотеки для работы
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
    splt = sns.relplot(data=df, kind='line') # Создаем график из датафрейма
    splt.savefig('simple_plots/simple_sns.png') # Сохраняем график в виде изображения
    t_s2 = datetime.datetime.now() # Задаем время окончания работы функции
    plt.clf()
    plt.close()
    return f'{t_s2 - t_s1}' # Возвращаем время работы функции

# Строим усложненный график
def hard_sns(df_sns_h):
    t_s1 = datetime.datetime.now() # Задаем время начала работы функции
    splt = sns.relplot(data=df_sns_h, kind='line') # Создаем график из датафрейма
    splt.savefig('complicated_plots/compl_sns.png') # Сохраняем график в виде изображения
    t_s2 = datetime.datetime.now() # Задаем время окончания работы функции
    plt.clf() # Очищаем график
    plt.close() # Закрываем график
    return f'{t_s2 - t_s1}' # Возвращаем время работы функции

def demo_sns(cs_type, period, stat_h):
    plt.figure(figsize=(10,7), dpi=300)
    if cs_type == 0:
        for i in stat_h:
            sns.barplot(x=period, y=i)
        plt.title('Столбчатый график')
    elif cs_type == 1:
        for i in stat_h:
            sns.scatterplot(x=period, y=i, markers='o')
        plt.title('Точечный график')
    elif cs_type == 2:
        for i in stat_h:
            sns.scatterplot(x=period, y=i, markers='o')
            sns.rugplot(x=period, y=i)
            plt.xlim(-1)
            plt.ylim(-5)
        plt.title('Точечный с предельными распределениями')
    plt.xlabel('Год')
    plt.ylabel('Статистика')
    plt.savefig('demo_plot/demo.png')
    plt.clf()
    plt.close()
