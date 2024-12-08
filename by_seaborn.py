import seaborn as sns
import datetime
from excel_reader import *

# period - период для представления
# norm_name - название нормы
# norm_nums - список значений нормы по количеству периодов
# name - название объекта представления
# stat - статистика объекта представления


# Строим простейшую таблицу
def simple_sns():
    t_s1 = datetime.datetime.now()
    splt = sns.relplot(data=df, kind='line')
    splt.savefig('simple_plots/simple_sns.png')
    t_s2 = datetime.datetime.now()
    print(f'Seaborn: {t_s2 - t_s1}')
