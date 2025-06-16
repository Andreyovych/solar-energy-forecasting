results = pd.DataFrame({
    'Model': ['Linear Regression', 'Decision Tree', 'Random Forest', 'XGBoost', 'Neural Network'],
    'R2 Score': [r2, tree_r2, rf_r2, xgb_r2, nn_r2],
    'MAE': [mae, mean_absolute_error(y_test, tree_pred), rf_mae, xgb_mae, nn_mae]
})
print(results)
# Візуальне порівняння:
results.plot(x='Model', y=['R2 Score', 'MAE'], kind='bar', figsize=(10, 6))
plt.title('Порівняння якості моделей')
plt.ylabel('Значення')
plt.grid(True)
plt.show()
