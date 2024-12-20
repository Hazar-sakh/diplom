# Импортируем необходимые библиотеки для работы
import sys # для работы с интерпретатором
import pandas as pd # для работы с датафреймами и предобработкой данных
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog # для работы интерфейса
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap # для включения графиков в поля интерфейса

# Импортируем функции построения графиков
from Backend.by_matplotlib import simple_mpl, hard_mpl, demo_mpl
from Backend.by_seaborn import simple_sns, hard_sns, demo_sns
from Backend.by_plotly import simple_ptl, hard_ptl

# Задаем переменные, которые будут вызываться в разных функциях (глобальные)
period = [] # список со значениями периодизации
norm_name = str # наименование нормы
norm_nums = [] # список значений нормы
names = [] # список названий параметров
name = str # наименование параметра
df_mp = None # будущий общий датафрейм
df_sns_h = None # будущий датафрейм для sns
stat = [] # список статистики выбранного значения
stat_h = [] # список со значениями для усложненного графика
demo_type = None # имя демонстрируемого вида графика


# Импортируем интерфейс
from GUI.ui_main import Ui_MainWindow
from GUI.ui_demonstrator import Ui_Dialog
# Создаем класс для реализации интерфейса, построения логики его работы и включения в него бэкэнда
class Vis(QMainWindow): # Создаем класс Vis и наследуемся от базового класса QMainWindow
    def __init__(self): # Вызываем класс
        super(Vis, self).__init__() # Определяем класс как суперкласс
        self.ui_demo = None
        self.demons = None
        self.ui = Ui_MainWindow() # Создаем экземпляр класса UI_MainWindow
        self.ui.setupUi(self) # и применяем его
        self.ui.browse.clicked.connect(self.browse_) # включаем обработчик события, запускающий функцию выбора файла и первичной предобработки
        self.ui.show.clicked.connect(self.open_demons)  # включаем обработчик события, запускающий демонстратор графиков
        self.ui.show.hide()
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
            # Задаем список статистики выбранного значения как глобальную переменную имя параметра для представления
            global stat, name, norm_nums, df_sns_h
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

            # Включаем показ кнопки демонстратора
            self.ui.show.show()

    def open_demons(self):
        self.demons = QtWidgets.QDialog()
        self.ui_demo = Ui_Dialog()
        self.ui_demo.setupUi(self.demons)
        self.demons.show()
        self.ui_demo.choose_lib.currentIndexChanged.connect(self.demo_lib)

    def demo_lib(self, lib):
        global demo_type
        demo_type = lib
        d_mpl_list = ['Столбчатая', 'Круговая', 'С накоплением']
        d_sns_list = ['Гистограмма', 'Свечи sns', 'Мощщный sns']
        d_ptl_list = ['Круговой ptl', 'Свечи ptl', 'Мощщный ptl']
        cs = self.ui_demo.choose_lib.currentText()
        if cs == 'Matplotlib':
            self.ui_demo.comboBox_2.clear()
            for i in d_mpl_list:
                self.ui_demo.comboBox_2.addItem(i)
        elif cs == 'Seaborn':
            self.ui_demo.comboBox_2.clear()
            for i in d_sns_list:
                self.ui_demo.comboBox_2.addItem(i)
        elif cs == 'Plotly':
            self.ui_demo.comboBox_2.clear()
            for i in d_ptl_list:
                self.ui_demo.comboBox_2.addItem(i)
        self.ui_demo.comboBox_2.currentIndexChanged.connect(self.show_wow)

    def show_wow(self, cs_type):
        if demo_type == 0:
            demo_mpl(cs_type, period, stat, name, norm_nums)
        px_demo = QPixmap('demo_plot/demo.jpg')  # Определяем график как изображение для реализации в GUI
        self.ui_demo.view.setScaledContents(True)  # Включаем масштабирование контента для поля в GUI
        self.resize(px_demo.width(), px_demo.height())  # Масштабируем график под выделенное поле GUI
        self.ui_demo.view.setPixmap(px_demo)  # Вставляем график в интерфейс

        if demo_type == 1:
            demo_sns(cs_type, df_mp, df_sns_h, name)
        px_demo = QPixmap('demo_plot/demo.jpg')  # Определяем график как изображение для реализации в GUI
        self.ui_demo.view.setScaledContents(True)  # Включаем масштабирование контента для поля в GUI
        self.resize(px_demo.width(), px_demo.height())  # Масштабируем график под выделенное поле GUI
        self.ui_demo.view.setPixmap(px_demo)  # Вставляем график в интерфейс


# Инициируем работу программы в соответствии с рекомендациями библиотеки PySide6
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Vis()
    window.show()

    sys.exit(app.exec())