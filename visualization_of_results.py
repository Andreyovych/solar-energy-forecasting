import matplotlib.pyplot as plt
# Побудова графіка "Справжні vs Прогнозовані значення"
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Справжні значення')
plt.ylabel('Прогнозовані значення')
plt.title('Порівняння справжніх і прогнозованих значень')
plt.show()
