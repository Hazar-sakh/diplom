from Backend.by_matplotlib import simple_mpl, hard_mpl
from Backend.by_seaborn import simple_sns, hard_sns
from Backend.by_plotly import simple_ptl, hard_ptl

import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap

from GUI.ui_main import Ui_MainWindow

class Vis(QMainWindow):

    def __init__(self):
        super(Vis, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browse.clicked.connect(self.browse_)

    def browse_(self):
        # Объявление глобальных переменных и диалоговое окно выбора таблицы
        global period, norm_name, names, df_mp, stat_h, df_sns_h
        file = QFileDialog.getOpenFileName(self, caption='Открыть таблицу', filter=('Таблицы (*.xlsx)'))

        # Предобработка данных
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

            # Задаем список названий строк для представления и вызываем функцию изменения вып.списка
            names = df_mp[df_mp.columns[0]].tolist()
            self.ui.select_type.addItems([f'{names.index(i) + 1}. {i}' for i in names])
            self.ui.select_type.currentIndexChanged.connect(self.index_changed)
        except:
            print('Неверные импортируемые данные, проверьте таблицу на соответствие требованиям к форме')

    def index_changed(self, i):
            # Задаем имя параметра для представления
            name = names[i]

            # Получаем список значений для представления по имени и норму
            pre_list = [int(i) for i in df_mp.iloc[names.index(name)] if type(i) is not str]
            stat = pre_list[1:]
            norm_nums = [pre_list[0] for i in stat]

            # Преобразуем данные в удобочитаемый датафрейм для Seaborn
            zip_l = list(zip(norm_nums, stat, period))
            data_l = [list(i) for i in zip_l]
            df = pd.DataFrame(data_l, columns=[norm_name, 'Факт', 'Год'])

            # Подготавливаем данные для усложненных таблиц
            #MatPlotLib
            stat_h=[]
            if len(stat_h) > 0:
                stat_h.clear()
            for i in names:
                pre_stat_h = [int(i) for i in df_mp.iloc[names.index(i)] if type(i) is not str]
                stat_h.append(pre_stat_h[1:])
            #Seaborn
            df_sns_h = pd.DataFrame(stat_h)
            df_sns_h.columns = [i for i in period]
            df_sns_h = df_sns_h.transpose()
            df_sns_h.columns = [i for i in names]

            # Выводим результаты построения упрощенного графика MatplotLib
            self.ui.t_mpl_s.setText(simple_mpl(period, norm_nums, stat))
            px_simple_mpl = QPixmap('simple_plots/simple_mpl.png')
            self.ui.mpl_g_s.setScaledContents(True)
            self.resize(px_simple_mpl.width(), px_simple_mpl.height())
            self.ui.mpl_g_s.setPixmap(px_simple_mpl)

            # Выводим результаты построения упрощенного графика Seaborn
            self.ui.t_sns_s.setText(simple_sns(df))
            px_simple_sns = QPixmap('simple_plots/simple_sns.png')
            self.ui.sns_g_s.setScaledContents(True)
            self.resize(px_simple_sns.width(), px_simple_sns.height())
            self.ui.sns_g_s.setPixmap(px_simple_sns)

            # Выводим результаты построения упрощенного графика Plotly
            self.ui.t_ptl_s.setText(simple_ptl(period, norm_nums, stat))
            px_simple_ptl = QPixmap('simple_plots/simple_plt.png')
            self.ui.ptl_g_s.setScaledContents(True)
            self.resize(px_simple_ptl.width(), px_simple_ptl.height())
            self.ui.ptl_g_s.setPixmap(px_simple_ptl)

            # Выводим результаты построения усложненного графика MatplotLib
            self.ui.t_mpl_h.setText(hard_mpl(period, stat_h))
            px_comp_mpl = QPixmap('complicated_plots/compl_mpl.png')
            self.ui.mpl_g_h.setScaledContents(True)
            self.resize(px_comp_mpl.width(), px_comp_mpl.height())
            self.ui.mpl_g_h.setPixmap(px_comp_mpl)

            # Выводим результаты построения усложненного графика Seaborn
            self.ui.t_sns_h.setText(hard_sns(df_sns_h))
            px_comp_sns = QPixmap('complicated_plots/compl_sns.png')
            self.ui.sns_g_h.setScaledContents(True)
            self.resize(px_comp_sns.width(), px_comp_sns.height())
            self.ui.sns_g_h.setPixmap(px_comp_sns)

            # Выводим результаты построения усложненного графика Plotly
            self.ui.t_ptl_h.setText(hard_ptl(period, stat_h))
            px_comp_ptl = QPixmap('complicated_plots/complicated_plt.png')
            self.ui.ptl_g_h.setScaledContents(True)
            self.resize(px_comp_ptl.width(), px_comp_ptl.height())
            self.ui.ptl_g_h.setPixmap(px_comp_ptl)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Vis()
    window.show()

    sys.exit(app.exec())