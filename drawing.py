import pylab
import matze
import numpy as np

m = 2
n = 2

def polygon(i, j, m, n, x, y, k=0, col='black'):
    if k == 1:
        return pylab.Polygon(
            [(j*m/(x + 2), -n/(y + 2)*i),
            ((j + 1)*m/(x + 2), -n/(y + 2)*i),
            ((j + 1)*m/(x + 2), -n/(y + 2)*(i + 1)),
            (j*m/(x + 2), -n/(y + 2)*(i + 1))],
            color=col)
    else:
        return pylab.Polygon(
            [((j + 1)*m/(x + 2), -n/(y + 2)*(i + 1)),
            ((j + 2)*m/(x + 2), -n/(y + 2)*(i + 1)),
            ((j + 2)*m/(x + 2), -n/(y + 2)*(i + 2)),
            ((j + 1)*m/(x + 2), -n/(y + 2)*(i + 2))],
            color=col)

def pr_matze(s, k=0):
    """Печатает лабиринт в более красивом виде"""
    if k == 0:
        a = s.space
    else:
        a = s.ans
    pylab.clf()
    pylab.rcParams['figure.figsize'] = 12, 10
    axes = pylab.gca()
    for i in np.arange(len(a[0]) + 2):
        axes.add_patch(polygon(0, i, m, n, len(a[0]), len(a), 1))
    for i in np.arange(len(a)):
        axes.add_patch(polygon(i + 1, 0, m, n, len(a[0]), len(a), 1))
        for j in np.arange(len(a[0])):
            if a[i][j] == 1:
                axes.add_patch(polygon(i, j, m, n, len(a[0]), len(a)))
            else:
                if (i, j) == s.start:
                    axes.add_patch(polygon(i, j, m, n, len(a[0]), len(a), col='green'))
                else:
                    if (i, j) == s.finish:
                        axes.add_patch(polygon(i, j, m, n, len(a[0]), len(a), col='red'))
                    else:
                        if a[i][j] == 2:
                            axes.add_patch(polygon(i, j, m, n, len(a[0]), len(a), col='yellow'))
        axes.add_patch(polygon(i + 1, len(a[0]) + 1, m, n, len(a[0]), len(a), 1))
    for i in np.arange(len(a[0]) + 2):
        axes.add_patch(polygon(len(a) + 1, i, m, n, len(a[0]), len(a), 1))
    pylab.xlim(0, m)
    pylab.ylim(-n, 0)
    pylab.show()
    return
