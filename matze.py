import numpy as np
from random import shuffle

class stack :
    def __init__(self, items=[]):
        self.items = items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

def find_id(e, sets):
    for i in np.arange(len(sets)):
        if e in sets[i]:
            return i

class matze():
    def __init__(self, n=2, m=2, start=(0, 0), finish=0):# n - высота, а m - ширина лабиринта?
        i, j = start
        self.start = (i*2, j*2) 
        if finish == 0:
            self.finish = (2*n - 2, 2*m -2)
        else:
            i, j = finish
            self.finish = (2*i, 2*j)
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

    def mst(self):
        """используем рандомизированный алгоритм Крускала"""
        cells = []
        for i in np.arange(0, len(self.space), 2):
            for j in np.arange(0, len(self.space[0]), 2):
                cells.append((i, j))
        sets_of_cells = [{i,} for i in cells]
        edges = []
        for c in cells:
            neighbours = self.neib(c, 2)
            c_edges = [{c, d} for d in neighbours]
            for i in c_edges:
                if i not in edges:
                    edges.append(i)
        shuffle(edges)
        for e in edges:
            e = list(e)
            i_0 = find_id(e[0], sets_of_cells)
            i_1 = find_id(e[1], sets_of_cells)
            if i_0 != i_1:
                sets_of_cells[i_0] = sets_of_cells[i_0].union(sets_of_cells[i_1])
                sets_of_cells.pop(i_1)
                self.push(((e[0][0] + e[1][0])//2, (e[0][1] + e[1][1])//2), -1)
        for i in np.arange(len(self.space)):
            for j in np.arange(len(self.space[0])):
                if self.space[i, j] == -1:
                    self.push((i, j), 0)
        return
   
    def __str__(self):
        """вывод лабиринта в командную строку посимвольно"""
        res = '#'*(len(self.space[0]) + 2) + '\n'
        for i in np.arange(len(self.space)):
            res += '#'
            for j in np.arange(len(self.space[i])):
                if self.space[i][j] == 0:
                    if (i, j) == self.start:
                        res += 's'
                    elif (i, j) == self.finish:
                        res += 'f'
                    else:
                        res += ' '
                else:
                    res += '#'
            res += '#'
            res += '\n'
        res += '#'*(len(self.space[0]) + 2)
        return res

    def save(self, s):
        if s[-4:] != '.txt':
            print("Введенный файл должен быть формата .txt. Пожалуйста, повторите попытку")
        else:
            res = ''
            res += str(self.start)[1:-1] + '\n'
            res += str(self.finish)[1:-1] + '\n'
            for i in np.arange(len(self.space)):
                if i < len(self.space) - 1:
                    res += str(self.space[i])[1:-1] + '\t'
                else:
                    res += str(self.space[i])[1:-1]
            with open(s, 'w') as f:
                f.write(res)
        return
    
    def upload(self, s):
        if s[-4:] != '.txt':
            print("Введенный файл должен быть формата .txt. Пожалуйста, повторите попытку")
            return
        else:
            with open(s, 'r') as f:
                res = f.read()
            res = res.split('\n')
            start = tuple([int(i) for i in res[0].split(', ')])
            finish = tuple([int(i) for i in res[1].split(', ')])
            space = [[float(k) for k in i.split(' ')] for i in res[2].split('\t')]
            r = matze()
            r.start = start
            r.finish = finish
            r.space = space
            return r
