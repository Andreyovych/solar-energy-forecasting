from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Прогнозування
y_pred = model.predict(X_test)
# Оцінка моделі
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Середня абсолютна помилка (MAE): {mae:.2f}")
print(f"Середньоквадратична помилка (MSE): {mse:.2f}")
print(f"Коефіцієнт детермінації (R2): {r2:.2f}")
