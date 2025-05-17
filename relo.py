import numpy as np
import math
def regular_polygon_Relo(n=3, center=np.array([0, 0]), r=1, N=100):
    """
    Создаёт матрицу точек, описывающих границу правильного многоугольника Рело.

    Аргументы:
    n (int): Количество вершин правильного многоугольника (нечётное, > 2).
    center (np.ndarray): Координаты центра многоугольника (массив из 2 элементов).
    r (float): Ширина многоугольника (положительное число).
    N (int): Количество точек для одной стороны (натуральное число).

    Возвращает:
    np.ndarray: Матрица с координатами точек границы многоугольника Рело.
    """
    assert isinstance(n, int) and n > 2 and n % 2 == 1, "n должно быть нечётным целым числом больше 2"
    assert isinstance(center, np.ndarray) and center.shape == (2,), "center должен быть массивом из 2 элементов"
    assert isinstance(r, (int, float)) and r > 0, "r должно быть положительным числом"
    assert isinstance(N, int) and N > 0, "N должно быть натуральным числом"
    alpha = 2*np.pi/n
    beta = alpha/2
    angle = np.linspace(-beta/2, beta/2, N)
    l=math.sqrt(2*r*r*(1-math.cos(beta)))
    R = l/(2*np.sin(np.pi/n))
    t = np.arange(0,2*np.pi,2*np.pi/n)
    vertices = center + R*np.transpose([np.cos(t), np.sin(t)])
    sides = np.concatenate([vertices[i] +
     r*np.transpose([np.cos(angle + np.pi + i*alpha),
     np.sin(angle + np.pi + i*alpha)])
     for i in range(n)])
    return sides