import numpy as np

# входные данные
X=int(input()).split('')
#X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# ожидаемый выход
#y = np.array([[0], [0], [1], [1]])

# инициализация весов нейрона
weights = np.array([[6.9388939e-17],[6.9388939e-17]])

# функция активации (сигмоидная)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# прямое распространение
outputs = sigmoid(np.dot(X, weights))

print(max(sigmoid(np.dot(X, weights))))
