import os
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# period - период для представления
# norm_name - название нормы
# norm_nums - список значений нормы по количеству периодов
# name - название объекта представления
# stat - статистика объекта представления


# Строим простейший график
def simple_sns(df):
    t_s1 = datetime.datetime.now()
    if os.path.exists('simple_plots/simple_sns.png'):
        plt.clf()
        plt.close()
    splt = sns.relplot(data=df, kind='line')
    splt.savefig('simple_plots/simple_sns.png')
    t_s2 = datetime.datetime.now()
    return f'{t_s2 - t_s1}'

# Строим усложненный график
def hard_sns(df_sns_H):
    t_s1 = datetime.datetime.now()
    if os.path.exists('complicated_plots/compl_sns.png'):
        plt.clf()
        plt.close()
    splt = sns.relplot(data=df_sns_H, kind='line')
    splt.savefig('complicated_plots/compl_sns.png')
    t_s2 = datetime.datetime.now()
    return f'{t_s2 - t_s1}'
