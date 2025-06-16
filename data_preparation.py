import pandas as pd
from sklearn.model_selection import train_test_split
# Завантаження даних
data = pd.read_csv('solar_energy_data.csv')
# Перевірка даних
print(data.head())
# колонки:
# 'temperature', 'humidity', 'cloud_cover', 'solar_radiation', 'energy_generated'
# Вибір ознак і цільової змінної
X = data[['temperature', 'humidity', 'cloud_cover', 'solar_radiation']]
y = data['energy_generated']
# Розбиття на тренувальну і тестову вибірки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
