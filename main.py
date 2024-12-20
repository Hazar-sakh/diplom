# Импортируем необходимые библиотеки для работы
import sys # для работы с интерпретатором
import pandas as pd # для работы с датафреймами и предобработкой данных
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog # для работы интерфейса
from PySide6.QtGui import QPixmap # для включения графиков в поля интерфейса

# Импортируем функции построения графиков
from Backend.by_matplotlib import simple_mpl, hard_mpl
from Backend.by_seaborn import simple_sns, hard_sns
from Backend.by_plotly import simple_ptl, hard_ptl

# Задаем переменные, которые будут вызываться в разных функциях (глобальные)
period = [] # список со значениями периодизации
norm_name = str # наименование нормы
names = [] # список названий параметров
df_mp = None # будущий датафрейм


# Импортируем интерфейс
from GUI.ui_main import Ui_MainWindow
# Создаем класс для реализации интерфейса, построения логики его работы и включения в него бэкэнда
class Vis(QMainWindow):
    # Создаем функцию инициализации по рекомендациям из документации к библиотеке PySide6
    def __init__(self):
        super(Vis, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browse.clicked.connect(self.browse_) # включаем обработчик события, запускающий функцию выбора файла и первичной предобработки
    # Реализуем функцию выбора файла для визуализации и его первичной предобработки
    def browse_(self):
        # Объявление переменных как глобальных и реализация диалогового окна выбора таблицы
        global period, norm_name, names, df_mp
        file = QFileDialog.getOpenFileName(self, caption='Открыть таблицу', filter='Таблицы (*.xlsx)')

        # Предобработка данных
        # V V V добавляем комментарий для исключения ошибки PEP8 ввиду отсутствия типа ошибки за её ненадобностью
        # noinspection PyBroadException
        try:
            table = pd.read_excel(file[0])
            self.ui.browse_label.setText(file[0])
            df_mp = pd.DataFrame(table)

            # Задаем список периодизации и имя нормирования
            period = []
            for i in df_mp.columns.values[1:]:
                if type(i) is str:
                    norm_name = i
                else:
                    period.append(str(i))

            # Задаем список названий строк для представления и вызываем функцию изменения выпадающего списка
            names = df_mp[df_mp.columns[0]].tolist()
            self.ui.select_type.addItems([f'{names.index(i) + 1}. {i}' for i in names])
            self.ui.select_type.currentIndexChanged.connect(self.index_changed) # Включаем обработчик (изменение выбранного параметра)
        except:
            print('Неверные импортируемые данные, проверьте таблицу на соответствие требованиям к форме')

    # Создаем функцию вторичной предобработки данных и связываем её с бэкэндом
    # V V V добавляем комментарий для исключения ошибки PEP8 ввиду разницы между исходным значением объявленной
    # глобальной переменной и её значением, получаемым после предобработки
    # noinspection PyUnresolvedReferences
    def index_changed(self, i):
            # Задаем имя параметра для представления
            name = names[i]

            # Получаем список значений для представления по имени и норму
            pre_list = [int(i) for i in df_mp.iloc[names.index(name)] if type(i) is not str]
            stat = pre_list[1:]
            norm_nums = [pre_list[0] for _ in stat]

            # Преобразуем данные в удобочитаемый датафрейм для Seaborn
            zip_l = list(zip(norm_nums, stat, period)) #
            data_l = [list(i) for i in zip_l] #
            df = pd.DataFrame(data_l, columns=[norm_name, 'Факт', 'Год']) #

            # Подготавливаем данные для усложненных таблиц
            #MatPlotLib
            if len(stat_h) > 0: # Устанавливаем условий для обновления списка значений параметров
                stat_h.clear()
            for i in names:
                pre_stat_h = [int(i) for i in df_mp.iloc[names.index(i)] if type(i) is not str] # создаем предварительный список списков значений параметров
                stat_h.append(pre_stat_h[1:]) # добавляем в список списков значений параметров список значений за вычетом нормы за ненадобностью
            #Seaborn
            df_sns_h = pd.DataFrame(stat_h) # Создаем датафрейм из списка списков значений параметров
            df_sns_h.columns = [i for i in period] # задаем заголовки колонн в виде значений периодизации
            df_sns_h = df_sns_h.transpose() # переворачиваем датафрейм (колонны транспортируем в строки)
            df_sns_h.columns = [i for i in names] # задаем заголовки колонн в виде имен параметров

            # Выводим результаты построения упрощенного графика MatplotLib
            self.ui.t_mpl_s.setText(simple_mpl(period, norm_nums, stat)) # Инициируем выполнение функции построения графика и задаем получившееся время работы в качестве текста поля в GUI
            px_simple_mpl = QPixmap('simple_plots/simple_mpl.png') # Определяем график как изображение для реализации в GUI
            self.ui.mpl_g_s.setScaledContents(True) # Включаем масштабирование контента для поля в GUI
            self.resize(px_simple_mpl.width(), px_simple_mpl.height()) # Масштабируем график под выделенное поле GUI
            self.ui.mpl_g_s.setPixmap(px_simple_mpl) # Вставляем график в интерфейс

            # Выводим результаты построения упрощенного графика Seaborn
            self.ui.t_sns_s.setText(simple_sns(df))# Инициируем выполнение функции построения графика и задаем получившееся время работы в качестве текста поля в GUI
            px_simple_sns = QPixmap('simple_plots/simple_sns.png') # Определяем график как изображение для реализации в GUI
            self.ui.sns_g_s.setScaledContents(True) # Включаем масштабирование контента для поля в GUI
            self.resize(px_simple_sns.width(), px_simple_sns.height()) # Масштабируем график под выделенное поле GUI
            self.ui.sns_g_s.setPixmap(px_simple_sns) # Вставляем график в интерфейс

            # Выводим результаты построения упрощенного графика Plotly
            self.ui.t_ptl_s.setText(simple_ptl(period, norm_nums, stat))# Инициируем выполнение функции построения графика и задаем получившееся время работы в качестве текста поля в GUI
            px_simple_ptl = QPixmap('simple_plots/simple_plt.png') # Определяем график как изображение для реализации в GUI
            self.ui.ptl_g_s.setScaledContents(True) # Включаем масштабирование контента для поля в GUI
            self.resize(px_simple_ptl.width(), px_simple_ptl.height()) # Масштабируем график под выделенное поле GUI
            self.ui.ptl_g_s.setPixmap(px_simple_ptl) # Вставляем график в интерфейс

            # Выводим результаты построения усложненного графика MatplotLib
            self.ui.t_mpl_h.setText(hard_mpl(period, stat_h))# Инициируем выполнение функции построения графика и задаем получившееся время работы в качестве текста поля в GUI
            px_comp_mpl = QPixmap('complicated_plots/compl_mpl.png') # Определяем график как изображение для реализации в GUI
            self.ui.mpl_g_h.setScaledContents(True) # Включаем масштабирование контента для поля в GUI
            self.resize(px_comp_mpl.width(), px_comp_mpl.height()) # Масштабируем график под выделенное поле GUI
            self.ui.mpl_g_h.setPixmap(px_comp_mpl) # Вставляем график в интерфейс

            # Выводим результаты построения усложненного графика Seaborn
            self.ui.t_sns_h.setText(hard_sns(df_sns_h))# Инициируем выполнение функции построения графика и задаем получившееся время работы в качестве текста поля в GUI
            px_comp_sns = QPixmap('complicated_plots/compl_sns.png') # Определяем график как изображение для реализации в GUI
            self.ui.sns_g_h.setScaledContents(True) # Включаем масштабирование контента для поля в GUI
            self.resize(px_comp_sns.width(), px_comp_sns.height()) # Масштабируем график под выделенное поле GUI
            self.ui.sns_g_h.setPixmap(px_comp_sns) # Вставляем график в интерфейс

            # Выводим результаты построения усложненного графика Plotly
            self.ui.t_ptl_h.setText(hard_ptl(period, stat_h))# Инициируем выполнение функции построения графика и задаем получившееся время работы в качестве текста поля в GUI
            px_comp_ptl = QPixmap('complicated_plots/complicated_plt.png') # Определяем график как изображение для реализации в GUI
            self.ui.ptl_g_h.setScaledContents(True) # Включаем масштабирование контента для поля в GUI
            self.resize(px_comp_ptl.width(), px_comp_ptl.height()) # Масштабируем график под выделенное поле GUI
            self.ui.ptl_g_h.setPixmap(px_comp_ptl) # Вставляем график в интерфейс

# Инициируем работу программы в соответствии с рекомендациями библиотеки PySide6
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Vis()
    window.show()

    sys.exit(app.exec())