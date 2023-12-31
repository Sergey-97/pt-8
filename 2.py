# 2. Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
from scipy.stats import t

# Значения IQ выборки
iq = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

# Размер выборки
n = len(iq)

# Среднее значение выборки
mean = np.mean(iq)

# Стандартное отклонение выборки
std = np.std(iq)

# Критическое значение t-распределения для надежности 0.95 и степеней свободы (n-1)
t_value = t.ppf(0.975, n-1)

# Стандартная ошибка среднего
se = std / np.sqrt(n)

# Доверительный интервал
ci = (mean - t_value * se, mean + t_value * se)

print("Доверительный интервал:", ci)
