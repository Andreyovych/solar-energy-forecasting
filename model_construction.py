from sklearn.linear_model import LinearRegression
# Створення моделі
model = LinearRegression()
# Навчання моделі
model.fit(X_train, y_train)
# Перевірка коефіцієнтів моделі
print("Коефіцієнти моделі:", model.coef_)
print("Вільний член:", model.intercept_)
