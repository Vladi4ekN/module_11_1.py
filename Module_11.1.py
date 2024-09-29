import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание линейного графика
plt.plot(x, y, marker='o')
plt.title('Простой линейный график')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

# Сохранение графика в файл
plt.savefig('plot.png')

# Показать график
plt.show()
