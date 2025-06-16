import matplotlib.pyplot as plt
import numpy as np
# Дані для діаграми
experiments = ['Експеримент 1', 'Експеримент 2', 'Експеримент 3']
mae_values = [15, 18, 12]
rmse_values = [20, 24, 17]
x = np.arange(len(experiments))  # розташування міток на осі X
width = 0.35  # ширина стовпчиків
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mae_values, width, label='MAE')
rects2 = ax.bar(x + width/2, rmse_values, width, label='RMSE')
# Додавання підписів та заголовків
ax.set_xlabel('Експерименти')
ax.set_ylabel('Похибка (кВт·год)')
ax.set_title('Порівняння MAE та RMSE для різних експериментів')
ax.set_xticks(x)
ax.set_xticklabels(experiments)
ax.legend()
# Функція для додавання підписів над стовпчиками
def autolabel(rect
::contentReference[oaicite:54]{index=54}
