import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
rooms = int(input("Количество комнат: "))
distance = float(input("Расстояние до центра: "))
bathrooms = int(input("Ванных комнат: "))
cars = int(input("Автомобилей: "))
df = pd.read_csv("Melbourne_housing_FULL.csv")

del df['Address']
del df['Method']
del df['SellerG']
del df['Date']
del df['Postcode']
del df['YearBuilt']
del df['Type']
del df['Lattitude']
del df['Longtitude']
del df['Regionname']
del df['Suburb']
del df ['CouncilArea']

# print(df.head())
# print(df.isnull().sum())

df_heat = df.corr()
sns.heatmap(df_heat,annot=True, cmap='coolwarm')
# plt.show()

del df ['Bedroom2']
del df ['Landsize']
del df ['Propertycount']
del df ['BuildingArea']
df["Car"] = df["Car"].fillna(df["Car"].mean())
df.dropna(axis=0, how='any', subset=None, inplace=True)

X = df[['Rooms', 'Distance', 'Bathroom', 'Car']]

y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10, shuffle=True)

model = LinearRegression()

model.fit(X_train, y_train)
# print(model.intercept_)
model_results = pd.DataFrame(model.coef_, X.columns, columns=['Coefficients'])



new_house = pd.DataFrame([{
    'Rooms': rooms,
    'Distance': distance,
    'Bathroom': bathrooms,
    'Car': cars
}])

# new_house_predict = model.predict(new_house)
#
# print(new_house_predict)
#
# prediction = model.predict(X_test)
#
# print(metrics.mean_absolute_error(y_test, prediction))

user_data_predict = model.predict(new_house)[0]
print(f'Возможная цена дома составляет {user_data_predict} долларов.')