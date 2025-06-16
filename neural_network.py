bash
pip install tensorflow
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# Створення моделі нейронної мережі
nn_model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])
# Компіляція моделі
nn_model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
# Навчання
history = nn_model.fit(X_train, y_train, validation_split=0.2, epochs=100, verbose=0)
# Прогнозування
nn_pred = nn_model.predict(X_test).flatten()
# Оцінка
nn_r2 = r2_score(y_test, nn_pred)
nn_mae = mean_absolute_error(y_test, nn_pred)
print(f"Neural Network - R2: {nn_r2:.2f}, MAE: {nn_mae:.2f}")
