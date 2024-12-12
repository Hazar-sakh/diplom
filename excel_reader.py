import pandas as pd

# period - период для представления
# norm_name - название нормы
# norm_nums - список значений нормы по количеству периодов
# name - название объекта представления
# stat - статистика объекта представления



try:
    table = pd.read_excel('Data_PPE.xlsx')
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
    for i in names:
        print(f'{names.index(i)+1}. {i}')
    point = 0
    name = names[point]

    # Получаем список значений для представления по имени и норму
    pre_list = [int(i) for i in df_mp.iloc[names.index(name)] if type(i) is not str]
    stat = pre_list[1:]
    norm_nums = [pre_list[0] for i in stat]

    # Преобразуем данные в удобочитаемый датафрейм
    zip_l = list(zip(norm_nums, stat, period))
    data_l = [list(i) for i in zip_l]
    df = pd.DataFrame(data_l, columns=[norm_name, 'Факт', 'Год'])
    print(f'\n\n\n{name}\n{period}\n{stat}\n\n')
except:
    print('Неверные импортируемые данные, проверьте таблицу на соответствие требованиям к форме')
