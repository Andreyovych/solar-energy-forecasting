from sklearn.ensemble import RandomForestRegressor
# Створення моделі Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
# Навчання
rf_model.fit(X_train, y_train)
# Прогнозування
rf_pred = rf_model.predict(X_test)
# Оцінка
rf_r2 = r2_score(y_test, rf_pred)
rf_mae = mean_absolute_error(y_test, rf_pred)
print(f"Random Forest - R2: {rf_r2:.2f}, MAE: {rf_mae:.2f}")
