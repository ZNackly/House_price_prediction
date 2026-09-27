# House Price Predictor

Модель **линейной регрессии** для предсказания цены дома на основе 4 признаков.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-orange?logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.0+-darkblue?logo=pandas&logoColor=white)

---

##  О проекте

Модель предсказывает **цену дома** на основе:

| Признак | Описание |
|---|---|
| **Rooms** | Количество комнат |
| **Distance** | Расстояние до центра Мельбурна (км) |
| **Bathroom** | Количество ванных комнат |
| **Car** | Количество парковочных мест |


##  Зависимости

```txt
pandas
scikit-learn
matplotlib
seaborn
```

---

##  Как это работает

1. Загружаем датасет `Melbourne_housing_FULL.csv`
2. Удаляем лишние столбцы
3. Заполняем пропуски в `Car` средним значением
4. Удаляем строки с оставшимися пропусками
5. Берём признаки: `Rooms`, `Distance`, `Bathroom`, `Car`
6. Делим данные на train/test (70/30)
7. Обучаем `LinearRegression`
8. Предсказываем цену нового дома

---

##  Коэффициенты модели

| Признак | Влияние на цену |
|---|---|
| **Rooms** | ⬆️ больше комнат → дороже |
| **Distance** | ⬇️ дальше от центра → дешевле |
| **Bathroom** | ⬆️ больше ванных → дороже |
| **Car** | ⬆️ больше парковок → немного дороже |

---

##  Структура

```
House_price_prediction/
├── model.py
├── Melbourne_housing_FULL.csv
└── README.md
```
