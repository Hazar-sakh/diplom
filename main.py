from by_matplotlib import simple_mpl, hard_mpl
from by_seaborn import simple_sns
from by_plotly import simple_ptl


import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from ui_main import Ui_MainWindow

class Vis(QMainWindow):

    def __init__(self):
        super(Vis, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browse.clicked.connect(self.browse_)

    def browse_(self):
        # Объявление глобальных переменных и диалоговое окно выбора таблицы
        global period, norm_name, names, df_mp, statH
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
            statH = []
            statH.clear()
            for i in range(0, len(names)):
                j = list(df_mp.iloc[i])
                statH.append(j)

            hard_mpl(period, statH)

            # Преобразуем данные в удобочитаемый датафрейм
            zip_l = list(zip(norm_nums, stat, period))
            data_l = [list(i) for i in zip_l]
            df = pd.DataFrame(data_l, columns=[norm_name, 'Факт', 'Год'])

            # Выводим результаты работы упрощенного графика MatplotLib
            self.ui.t_mpl_s.setText(simple_mpl(period, norm_nums, stat))
            px_simple_mpl = QPixmap('simple_plots/simple_mpl.png')
            self.ui.mpl_g_s.setScaledContents(True)
            self.resize(px_simple_mpl.width(), px_simple_mpl.height())
            self.ui.mpl_g_s.setPixmap(px_simple_mpl)

            # Выводим результаты работы упрощенного графика Seaborn
            self.ui.t_sns_s.setText(simple_sns(df))
            px_simple_sns = QPixmap('simple_plots/simple_sns.png')
            self.ui.sns_g_s.setScaledContents(True)
            self.resize(px_simple_sns.width(), px_simple_sns.height())
            self.ui.sns_g_s.setPixmap(px_simple_sns)

            # Выводим результаты работы упрощенного графика Plotly
            self.ui.t_ptl_s.setText(simple_ptl(period, norm_nums, stat))
            px_simple_ptl = QPixmap('simple_plots/simple_plt.png')
            self.ui.ptl_g_s.setScaledContents(True)
            self.resize(px_simple_ptl.width(), px_simple_ptl.height())
            self.ui.ptl_g_s.setPixmap(px_simple_ptl)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Vis()
    window.show()

    sys.exit(app.exec())