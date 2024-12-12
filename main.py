# from by_matplotlib import simple_mpl
# from by_seaborn import simple_sns
# from by_plotly import simple_ptl
#
#
# simple_mpl()
# simple_sns()
# simple_ptl()


import sys


import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_main import Ui_MainWindow
from by_matplotlib import simple_mpl

class Vis(QMainWindow):
    def __init__(self):
        super(Vis, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browse.clicked.connect(self.browse_)

    def browse_(self):
        file = QFileDialog.getOpenFileName(self, caption='Открыть таблицу', filter=('Таблицы (*.xlsx)'))

        try:
            table = pd.read_excel(file[0])
            self.ui.browse_label.setText(file[0])
            df_mp = pd.DataFrame(table)

            # Предобработка данных
            # Задаем список периодизации и имя нормирования
            period = []
            norm_name = str
            for i in df_mp.columns.values[1:]:
                if type(i) is str:
                    norm_name = i
                else:
                    period.append(str(i))

            # Задаем список названий строк для представления и имя искомого значения
            names = df_mp[df_mp.columns[0]].tolist()
            self.ui.select_type.addItems([f'{names.index(i) + 1}. {i}' for i in names])

            # point = 0
            pt = self.ui.select_type.textActivated()
            print(pt)
            point = names.index(pt)
            print(point)
            name = names[point]

            # Получаем список значений для представления по имени и норму
            pre_list = [int(i) for i in df_mp.iloc[names.index(name)] if type(i) is not str]
            stat = pre_list[1:]
            norm_nums = [pre_list[0] for i in stat]

            # Преобразуем данные в удобочитаемый датафрейм
            zip_l = list(zip(norm_nums, stat, period))
            data_l = [list(i) for i in zip_l]
            df = pd.DataFrame(data_l, columns=[norm_name, 'Факт', 'Год'])
            # print(f'\n\n\n{name}\n{period}\n{stat}\n\n')
        except:
            print('Неверные импортируемые данные, проверьте таблицу на соответствие требованиям к форме')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Vis()
    window.show()

    sys.exit(app.exec())