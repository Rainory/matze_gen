import numpy as np
#import 

class matze():
    def __init__(self, n, m):# n - высота, а m - ширина лабиринта?
        a = np.ones((2*n - 1, 2*m -1))
        for i in np.arange(2*n - 1):
            for j in np.arange(2*m - 1):
                if i % 2 == 0 and j % 2 == 0:
                    a[i, j] = 0
        self.space = a

    def neib(self, i, j, k):
        ''' поиск соседей к узлу лабиринта (графа, в которых еще не бывал алгоритм), где (i, j) - координаты узла, а k - шаг до соседа
        т.е. если k = 1 - ищем соседниеузлы, если 2, то через один и т.д.'''
        res = []
        if i - k >= 0:
            if self.space[i - k, j] == 0:
                res.append((i - k, j))
        if j - k >= 0:
            if self.space[i, j - k] == 0:
                res.append((i, j - k))
        if i + k < len(self.space):
            if self.space[i + k, j] == 0:
                res.append((i + k, j))
        if j + k < len(self.space[0]):
            if self.space[i, j + k] == 0:
                res.append((i, j + k))
        return res

    
    """def asdf(self):
        stack = []
        for i in for i in np.arange(0, 2*n - 1, 2):
            for j in np.arange(0, 2*m - 1, 2):
                stack.append((i, j))"""
    
    def __str__(self):# вывод лабиринта в командную строку посимвольно
        res = '#'*(len(self.space[0]) + 2) + '\n'
        for i in range(len(self.space)):
            res += '#'
            for j in range(len(self.space[i])):
                if self.space[i, j] == 0:
                    res += ' '
                else:
                    res += '#'
            res += '#'
            res += '\n'
        res += '#'*(len(self.space[0]) + 2)
        return res


