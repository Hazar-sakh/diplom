# Сравнение различных библиотек для визуализации данных: Matplotlib, Seaborn и Plotly

Предлагается создать набор визуализаций с использованием библиотек Matplotlib, Seaborn и Plotly, сравнить их функциональность и удобство использования.
Matplotlib, Seaborn и Plotly являются библиотеками для построения графиков массивов в Python, следовательно для реализации практической части содержания работы потребуется некоторый массив данных.

![Вступительное демо](https://github.com/Hazar-sakh/diplom/blob/master/demos/demo.jpg)

## Содержание
1. [Обзор проекта](##обзор-проекта)
2. [Структура проекта](#структура-проекта)
3. [Обзор библиотек и реализация визуализации](#обзор-библиотек-и-реализация-визуализации)
   - [Matplotlib](#matplotlib)
   - [Seaborn](#Seaborn)
   - [Plotly](#Plotly)
4. [Сравнительный анализ библиотек](#сравнительный-анализ-библиотек)
5. [Заключение](#заключение)

## Обзор проекта
Matplotlib, Seaborn и Plotly являются библиотеками для построения графиков массивов в Python, следовательно для реализации практической части содержания работы потребуется некоторый массив данных.
Используем данные ООО «Курильский Универсальный Комплекс» (место работы автора) по выдаче матросу средств индивидуальной защиты в период с 2014 по 2024 годы. 

Данные представлены в виде таблицы Excel, в связи с чем потребуется использование дополнительных библиотек: openpyxl – для считывания данных из таблицы и pandas для оперирования данными и их предобработки.
Вместе с тем, для удобства сравнения библиотек и представления результатов предлагаем обернуть программу в пользовательский интерфейс с помощью библиотеки PySide6.
Для измерения скорости быстродействия воспользуемся стандартной библиотекой datatime.

Критерии оценки исследуемых библиотек будет включать следующие пункты:

   1.	Особенности предобработки данных
   2.	Простоту построения графика без параметров стилизации
   3.	Полноту отображения информации
   4.	Быстродействие
   
В целях обеспечения объективности оценки библиотек остановимся на следующей методике: 
   1. с помощью каждой библиотеки будут построены графики двух типов:
      а. упрощенный – включает один параметр;
      в. усложненный – включает все параметры;
   4. быстродействие будет учитывать время между получением входных данных и завершением вывода графика;
   5. время предобработки данных не учитывается, поскольку форма поступающих данных зависит исключительно от программы и идеи реализуемого проекта, что не влияет на реализацию функций исследуемых библиотек;
   6. способ построения графиков будет субъективно простым;
   7. оценки субъективного характера (красота графиков, цветовые гаммы и т.п.) отводятся на второй план и будут рассмотрены в заключении.
        
    
## Структура проекта
Проект включает:
   1. Файл main.py, содержащий в себе код, объединяющий GUI и backend, считывающий таблицу excel, осуществляющий предобработку данных.
   2. Файл ui_main.py, содержащий в себе код GUI.
   3. Файлы by_matplotlib.py, by_plotly.py и by_seaborn.py, содержащие в себе код построения и сохранения графиков, и размещенные в директории Backend.
   4. Генерируемые программой файлы изображений графиков для их дальнейшего представления, размещенные в директориях simple_plots для простых графиков и complicated_plots для усложненных.

Для начала установим необходимые библиотеки с помощью pip install (см. Приложение 1. [Список необходимых библиотек](https://github.com/Hazar-sakh/diplom/blob/master/requirements.txt)).

Далее создадим пользовательский интерфейс с помощью библиотеки PySide6 и встроенного редактора QtDesigner.

Задача интерфейса предоставить пользователю форму для выбора таблицы excel, параметра таблицы, который необходимо визуализировать, и представление графиков в виде изображений.

Также, в GUI включим сведения о быстродействии исполнения подпрограмм построения графиков.
![Главное окно](https://github.com/Hazar-sakh/diplom/blob/master/demos/ГУИ.jpg)

Добавим отдельное окно для демонстрации графиков:
![Окно демонстарции графиков](https://github.com/Hazar-sakh/diplom/blob/master/demos/демо.png)

После построения GUI и формирования файла ui_main.ui преобразуем его в ui_main.py для последующей работы.
Создадим файл main.py, в который импортируем необходимые для дальнейшей работы библиотеки, а также напишем класс, наследуемый от Ui_MainWindow.

## Обзор библиотек и реализация визуализации
### Matplotlib
Matplotlib - популярная Python-библиотека для визуализации данных. Она используется для создания любых видов графиков: линейных, круговых диаграмм, построчных гистограмм и других - в зависимости от задач.
Matplotlib была написана американским нейробиологом Джоном Хантером (англ. John Hunter) и распространяется на условиях BSD-подобной лицензии.
Изначально Хантер разработал Matplotlib во время постдокторантуры по нейробиологии для визуализации данных электрокортикографии (ЭКоГ) у пациентов с эпилепсией.
Библиотека была создана для имитации графических команд MATLAB, она не зависит от MATLAB и может использоваться в объектно-ориентированном стиле Python. Хотя Matplotlib написана на чистом Python, она активно использует NumPy и другие расширения для обеспечения высокой производительности даже для больших массивов.
Matplotlib использовалась для визуализации данных во время посадки космического аппарата «Феникс» на Марс в 2008 году и для создания первого изображения чёрной дыры.
Пример построения упрощенного и усложненного графиков с помощью Matplotlib:
    
     ```python
     # Импортируем необходимые библиотеки для работы
     import matplotlib.pyplot as plt # Для работы с графиком
     import datetime # Для измерения времени работы
     import numpy as np
     
     # V V V Создаем для удобства список глобальных переменных, которыми будем пользоваться
     # period - период для представления
     # norm_name - название нормы
     # norm_nums - список значений нормы по количеству периодов
     # name - название объекта представления
     # stat - статистика объекта представления
     # stat_h - статистика объектов представления всех параметров
     # df - датафрейм для простого графика Seaborn
     # df_sns_h - датафрейм для усложненного графика Seaborn
     
     # Строим простейший график в функцию которого передаем значения периода, нормы и статистики
     def simple_mpl(period, norm_nums, stat):
         t_mpl1 = datetime.datetime.now() # Задаем время начала работы функции
         plt.plot(period, stat) # Добавляем линию статистики
         plt.plot(period, norm_nums) # Добавляем линию нормы
         plt.savefig('simple_plots/simple_mpl.png') # Сохраняем график в виде изображения
         t_mpl2 = datetime.datetime.now() # Задаем время окончания работы функции
         plt.close() # Закрываем график с освобождением ресурсов
         return f'{t_mpl2 - t_mpl1}' # Возвращаем время работы функции
     
     # Строим усложненный график в функцию которого передаем значения периода и статистики
     def hard_mpl(period, stat_h):
         t_mpl1 = datetime.datetime.now() # Задаем время начала работы функции
         for i in stat_h: # Добавляем все линии циклом for для каждого списка из списка статистки
             plt.plot(period, i)
         plt.savefig('complicated_plots/compl_mpl.png') # Сохраняем график в виде графического изображения
         t_mpl2 = datetime.datetime.now() # Задаем время окончания работы функции
         plt.close() # Закрываем график с освобождением ресурсов
         return f'{t_mpl2 - t_mpl1}' # Возвращаем время работы функции
     ```

### Seaborn
Seaborn — это библиотека для создания статистической графики на Python. Она основана на Matplotlib и тесно интегрируется со структурами данных pandas.
Seaborn помогает изучать и понимать данные. Его функции построения графиков работают с datafraim’ами и массивами, содержащими целые наборы данных, и выполняют необходимое семантическое сопоставление и статистическую агрегацию для создания информативных графиков. Его API, ориентирован на наборы данных, позволяет сосредоточиться на том, что означают различные элементы ваших графиков, а не на деталях их построения.
Seaborn для построения графиков неявно использует Matplotlib, создаёт полноценную графику с помощью одного вызова функции: при необходимости его функции автоматически добавляют информативные подписи к осям и легенды, которые объясняют семантические соответствия на графике.
Во многих случаях Seaborn также выбирает значения параметров по умолчанию в зависимости от характеристик данных.
Интеграция Seaborn с Matplotlib позволяет использовать его во многих средах, которые поддерживает Matplotlib, включая исследовательский анализ данных, взаимодействие в реальном времени в приложениях с графическим интерфейсом и архивирование в различных растровых и векторных форматах.
Сочетание высокоуровневого интерфейса Seaborn и широких возможностей настройки Matplotlib позволяет быстро изучать данные и создавать графику, которую можно адаптировать для публикации.
Seaborn был разработан специалистом по машинному обучению и нейробиологии компании Modal Labs Майклом Уаскомом (англ. Michael Waskom) и выпущен в 2014 году. Основная цель Seaborn — упростить создание сложных визуализаций и улучшить эстетику графиков, что делает его идеальным для быстрого анализа данных.
В академических кругах Seaborn часто применяется для визуализации результатов, которые затем публикуются в научных статьях и журналах. Графики, созданные с помощью неё, используются для демонстрации результатов экспериментов, а также для построения информативных графических абстракций, поддерживающих аргументацию исследований.
В бизнес-сфере Seaborn служит ключевым инструментом для визуализации данных, помогая аналитикам представлять сложные выводы в понятной форме для принятия решений. Графики, построенные с использованием этой библиотеки, могут украшать доклады и презентации, делая данные доступными для неподготовленной аудитории.
Пример построения упрощенного и усложненного графиков с помощью Seaborn:
      
      ```python
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
          plt.close()
          return f'{t_s2 - t_s1}' # Возвращаем время работы функции
      
      # Строим усложненный график
      def hard_sns(df_sns_h):
          t_s1 = datetime.datetime.now() # Задаем время начала работы функции
          splt = sns.relplot(data=df_sns_h, kind='line') # Создаем график из датафрейма
          splt.savefig('complicated_plots/compl_sns.png') # Сохраняем график в виде изображения
          t_s2 = datetime.datetime.now() # Задаем время окончания работы функции
          plt.close() # Закрываем график
          return f'{t_s2 - t_s1}' # Возвращаем время работы функции
      ```

### Plotly
Plotly - это компания, занимающаяся техническими вычислениями, со штаб-квартирой в Монреале, которая разрабатывает онлайн-инструменты для анализа данных и визуализации. Plotly предоставляет онлайн-инструменты для построения графиков, аналитики и статистики для индивидуальных пользователей и совместной работы, а также научные графические библиотеки для Python, R, MATLAB, Perl, Julia, Arduino, JavaScript и REST.
Компания была основана Алексом Джонсоном, Джеком Пармером, Крисом Пармером и Мэтью Сандквистом.
Основатели имеют опыт работы в сфере науки, энергетики, анализа и визуализации данных. Среди первых сотрудников - Кристоф Вио, канадский инженер-программист, и Бен Постлтуэйт, канадский геофизик.
Plotly также упрощает создание интерактивных графиков. Интерактивные графики не только красиво выглядят, но и позволяют публике более внимательно изучить каждую точку на графике. С помощью Plotly достаточно легко создавать сложные графики, он отлично подходит для создания интерактивных и качественных графиков при помощи нескольких строк кода.
Благодаря своей гибкости и простоте использования библиотека широко используется в различных областях: анализ данных, научные исследования, финансы, веб-разработка и других.
      
      ```python
      # Импортируем необходимые библиотеки для работы
      import os.path # Для проверки наличия файла графика
      import plotly.graph_objs as go # Для работы с графиком
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
      
      # Строим простейший график в функцию которого передаем значения периода, нормы и статистики
      def simple_ptl(period, norm_nums, stat):
          t_ptl1 = datetime.datetime.now() # Задаем время начала работы функции
          fig = go.Figure() # Определяем переменную графика
          fig.add_trace(go.Scatter(x=period, y=norm_nums, mode='lines')) # Добавляем линию нормы
          fig.add_trace(go.Scatter(x=period, y=stat, mode='lines')) # Добавляем линию статистики
          if not os.path.exists('simple_plots/'): # Определяем условие создания директории
              os.mkdir('simple_plots/')
              if os.path.exists('simple_plots/simple_plt.png'): # Определяем условие обновления (через удаление) файла графика
                  os.remove('simple_plots/simple_plt.png')
          name = 'simple_plt' # Задаем имя графика
          fig.write_image(f'simple_plots/{name}.png') # Сохраняем график в виде изображения
          t_ptl2 = datetime.datetime.now() # Задаем время окончания работы функции
          return f'{t_ptl2 - t_ptl1}' # Возвращаем время работы функции
      
      
      def hard_ptl(period, stat_h):
          t_ptl1 = datetime.datetime.now() # Задаем время начала работы функции
          fig = go.Figure() # Определяем переменную графика
          for i in stat_h: # Циклом for создаем линии графика для каждого параметра
              fig.add_trace(go.Scatter(x=period, y=i, mode='lines'))
          if not os.path.exists('complicated_plots/'): # Определяем условие создания директории
              os.mkdir('complicated_plots/')
              if os.path.exists('complicated_plots/complicated_plt.png'): # Определяем условие обновления (через удаление) файла графика
                  os.remove('complicated_plots/complicated_plt.png')
          name = 'complicated_plt' # Задаем имя графика
          fig.write_image(f'complicated_plots/{name}.png') # Сохраняем график в виде изображения
          t_ptl2 = datetime.datetime.now() # Задаем время окончания работы функции
          return f'{t_ptl2 - t_ptl1}' # Возвращаем время работы функции
      ```

## Сравнительный анализ библиотек
В целях исполнения созданных функций построения графиков с применением пользовательского интерфейса, импортируем их в файл main.py.

```python
# Импортируем функции построения графиков
from Backend.by_matplotlib import simple_mpl, hard_mpl, demo_mpl
from Backend.by_seaborn import simple_sns, hard_sns, demo_sns
from Backend.by_plotly import simple_ptl, hard_ptl, demo_ptl
```

Далее в функции, выполняемой по изменению (выбору) параметра из выпадающего списка, инициализируем выполнение функций построения графика.
Напомним, что функция построения графика возвращает время её исполнения, которую мы интегрируем в соответствующее текстовое поле пользовательского интерфейса.
Вместе с тем, в поля пользовательского интерфейса интегрируем масштабированную таблицу упрощенного графика.

```python
# Выводим результаты построения упрощенного графика MatplotLib
self.ui.t_mpl_s.setText(simple_mpl(period, norm_nums, stat)) # Инициируем выполнение функции построения графика и задаем получившееся время работы в качестве текста поля в GUI
px_simple_mpl = QPixmap('simple_plots/simple_mpl.png') # Определяем график как изображение для реализации в GUI
self.ui.mpl_g_s.setScaledContents(True) # Включаем масштабирование контента для поля в GUI
self.resize(px_simple_mpl.width(), px_simple_mpl.height()) # Масштабируем график под выделенное поле GUI
self.ui.mpl_g_s.setPixmap(px_simple_mpl) # Вставляем график в интерфейс
```

После чего сделаем то же самое и для отображения усложненных графиков, и таким образом, завершим создание программы.

Для анализа работы библиотек проведем эксперименты с отображением различных параметров заданной таблицы.

![Эксперимент1](https://github.com/Hazar-sakh/diplom/blob/master/demos/vis4.jpg)

Итак, по результатам исполнения программы видим, что графики успешно создаются, при этом:
   1. среднее время построения упрощенного графика с помощью Matplotlib по использованному методу составляет 0,066 секунды, и усложненного графика 0,038 секунды;
   2. среднее время построения графика с помощью Seaborn составляет 0,105 секунды, усложненного – 0,211, следует отметить, что ввиду использования датафрейма в графике автоматически отображается легенда;
   3. среднее время построения графика с помощью Plotly составляет 0,623 секунды, усложненного – 0,615, при этом, как и в Seaborn отображается легенда, но ввиду неприменения датафрейма отсутствует конкретизация.

Таким образом, оценивая библиотеки по определенным ранее критериям можно сделать вывод, что Seaborn в простейшей реализации передает всю смысловую нагрузку графика, дает возможность без дополнительной стилизации интерпретировать его и интегрировать в приложения. Это достигается за счет использования метода предобработки данных в датафрейм. Скорость его работы располагается в промежутке между результатами остальных сравниваемых библиотек, и является приемлемой. Вместе с тем, от пользователя требуются базовые знания библиотеки pandas ввиду необходимости работы с датафреймами, в связи с чем данная особенность может иметь субъективную оценку пользователя как отрицательную (необходимость изучения pandas), так и положительную (построение графика из датафрейма с минимальными затратами времени на предобработку и получение приемлемого результата построения графика). 

График, построенный с применением Plotly, менее информативен, что усложняет его восприятие без дополнительной стилизации, скорость его выполнения самая медленная, предобработка данных может быть реализована в различных вариантах. Особенности записи графического представления графика, связанные с необходимостью наличия библиотеки kaleido и браузера Google Chrome, являются скорее техническим недостатком, который компенсируется предназначением Plotly – построением интерактивных графиков высокого качества. 

Matplotlib является наиболее быстродействующей библиотекой и в то же время без стилизации возможность интерпретация данных весьма сомнительна. Предобработка данных достаточно простая, не требует знаний сторонних библиотек, хотя возможность работы с датафреймами имеется.

Все три библиотеки, с т.з. простоты построения графиков без применения стилизации, оказались приемлемы. Официальная документация позволяет реализовать базовые методы в максимально краткие сроки. В то же время, особенности и возможности библиотек в большей степени определяют сферы их применения, нежели субъективные предпочтения пользователей.


## Заключение
В рамках проведенного исследования были определены и оценены ключевые в рамках предложенной методики параметры библиотек визуализации Matplotlib, Seaborn и Plotly.
Вместе с тем, субъективные параметры, например, красота графиков, разнообразие тем и цветовых гамм, не учитывались, однако, для части пользователей они являются важными показателями для выбора используемой библиотеки.

В этом отношении Matplotlib является достаточно «гибкой» библиотекой, которую можно настроить очень подробно, и получить желаемый результат. Библиотека обладает большой коллекцией графиков. Построение красивого графика требует определенных затрат времени и среднего знания методов и атрибутов библиотеки, дизайнерских навыков для выбора приемлемых вариантов гамм и форм. Возможность взаимодействия с датафреймами имеется, но не является преимуществом, по сравнению с Seaborn.

Визуализация некоторых из графиков, построенных с помощью Matplotlib через окно демонстратора:

![Matplotlib1](https://github.com/Hazar-sakh/diplom/blob/master/demos/демо1.png)

![Matplotlib2](https://github.com/Hazar-sakh/diplom/blob/master/demos/демо2.png)

Seaborn:

![Seaborn1](https://github.com/Hazar-sakh/diplom/blob/master/demos/демо4.png)

![Seaborn2](https://github.com/Hazar-sakh/diplom/blob/master/demos/демо6.png)

Plotly:

![Plotly1](https://github.com/Hazar-sakh/diplom/blob/master/demos/демо7.png)

![Plotly2](https://github.com/Hazar-sakh/diplom/blob/master/demos/демо8.png)

Стоит отметить, что Matplotlib, Seaborn и Plotly не являются взаимоисключающими и могут использоваться вместе в зависимости от конкретных потребностей проекта. 

Matplotlib хорошо подходит для статичных графиков в печатных материалах, Seaborn прост в обращении и хорошо подходит для визуализации научных данных «на скорую руку», а Plotly отлично подходит для создания интерактивных и веб-визуализаций, создания карт.

В рамках бизнес-задачи по анализу расхода средств индивидуальной защиты в период с 2014 по 2024 годы наиболее предпочтительным решением будет использование Seaborn, однако если эту задачу необходимо было бы выполнить для интерактивного или веб-представления, то использование библиотеки Plotly видится более рациональным, так как Matplotlib хоть и обладает соответствующим функционалом, но реализация такого графика потребовала бы больших затрат времени и большего объема кода.

