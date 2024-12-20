# Task#8. Numpy

Задачу выполняла в [Google Colab](https://colab.research.google.com/drive/19cr3WRLZPp3nKwiwhuYtI10cnrW48joP?usp=sharing), ссылка на сам ноутбук также есть в README.md всего репозитория.

Эта же папка, в свою очередь, дублирует его.


### Описание выполненной работы

В задаче были выполнены следующие основные этапы:

1. **Подготовка данных**:
    - Загружен датасет Ирисов, который был представлен в виде одномерного массива меток классов и двумерной матрицы признаков.
    - Проведена нормализация данных в диапазон от 0 до 1 и преобразование одного признака (третий столбец) в категориальную переменную с тремя типами.

2. **Разделение данных**:
    - Датасет был случайным образом разделен на тренировочную и тестовую выборки в пропорции 80%/20%.

3. **Обучение модели**:
    - Применен метод классификации Support Vector Classifier (`SVC`), модель обучена на тренировочных данных и оценена на тестовых.

4. **Эксперименты**:
    - Проведено три эксперимента с изменением гиперпараметров модели и условий препроцессинга (изменение параметра `C`, типа ядра, нормализованные и не нормализованные данные).

5. Визуализация:
    - Для визуализации данных использованы методы `PCA` и `t-SNE` с понижением размерности до 2D.
    - Построены `scatter plot` графики, где цвет точек соответствует типу ириса, как для истинных, так и для предсказанных меток.

Каждый этап сопровожден пояснениями в Markdown, и финальная работа представлена в `numpy.ipynb`
