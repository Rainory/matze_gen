import numpy as np

class stack :
    def __init__(self, items=[]):
        self.items = items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

class matze():
    def __init__(self, n, m):# n - высота, а m - ширина лабиринта?
        a = np.ones((2*n - 1, 2*m -1))
        for i in np.arange(2*n - 1):
            for j in np.arange(2*m - 1):
                if i % 2 == 0 and j % 2 == 0:
                    a[i, j] = 0
        self.space = a

    def neib(self, c, k):
        ''' поиск соседей к узлу лабиринта (графа, в которых еще не бывал алгоритм), где c - координаты узла, а k - шаг до соседа
        т.е. если k = 1 - ищем соседниеузлы, если 2, то через один и т.д.'''
        res = []
        i, j = c
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
    
    def get(self, c):
        """возвращает элемент space с индексами 'c' """
        i, j = c
        return self.space[i, j]
    
    def push(self, c, n):
        '''кладем в c значение n'''
        i, j = c
        self.space[i, j] = n
        return

    def zeros(self):
        res = []
        for i in np.arange(len(self.space)):
            for j in np.arange(len(self.space[0])):
                if self.space[i, j] == 0:
                    res.append((i, j))
        return res

    
    def dfs(self):
        """реализуем алгоритм dfs"""
        s = stack()
        current = (0, 0)
        while 0 in [el for st in self.space for el in st]:
            neighbours = self.neib(current, k=2)
            self.push(current, -1)
            if len(neighbours) > 0:
                s.push(current)
                ind = np.random.randint(len(neighbours))
                current = neighbours[ind]
                self.push(current, -1)
                self.push(((current[0] + s.items[-1][0])//2, (current[1] + s.items[-1][1])//2), -1)
            elif len(s.items) != 0:
                current = s.pop()
            else:
                zer = self.zeros()
                ind = np.random.randint(len(zer))
                current = zer[ind]
        for i in np.arange(len(self.space)):
            for j in np.arange(len(self.space[0])):
                if self.space[i, j] == -1:
                    self.push((i, j), 0)
        return
    
    def __str__(self):
        """вывод лабиринта в командную строку посимвольно"""
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
