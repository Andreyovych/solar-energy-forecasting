bash
pip install xgboost
import xgboost as xgb
# Створення моделі XGBoost
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, random_state=42)
# Навчання
xgb_model.fit(X_train, y_train)
# Прогнозування
xgb_pred = xgb_model.predict(X_test)
# Оцінка
xgb_r2 = r2_score(y_test, xgb_pred)
xgb_mae = mean_absolute_error(y_test, xgb_pred)
print(f"XGBoost - R2: {xgb_r2:.2f}, MAE: {xgb_mae:.2f}")
