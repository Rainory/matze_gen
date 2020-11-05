import numpy as np

class matze():
    def __init__(self, n, m):# n - высота, а m - ширина лабиринта?
        a = np.ones((2*n - 1, 2*m -1))
        for i in np.arange(2*n - 1):
            for j in np.arange(2*m - 1):
                if i % 2 == 0 and j % 2 == 0:
                    a[i, j] = 0
        self.space = a

    def neib(self, i, j):
      sd
    
    def __str__(self):
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
