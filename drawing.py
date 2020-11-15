import pylab
import matze
import numpy as np

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
        axes.add_patch(pylab.Polygon([(i*2/(len(a[0]) + 2), 0),((i+1)*2/(len(a[0]) + 2), 0),((i+1)*2/(len(a[0]) + 2), -2/(len(a) + 2)), (i*2/(len(a[0]) + 2), -2/(len(a) + 2))], color='black'))
    for i in np.arange(len(a)):
        axes.add_patch(pylab.Polygon([(0, -2/(len(a) + 2)*(i + 1)),(2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 1)),(2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 2)), (0, -2/(len(a) + 2)*(i + 2))], color='black'))
        for j in np.arange(len(a[0])):
            if a[i][j] == 1:
                axes.add_patch(pylab.Polygon([((j + 1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 1)),((j + 2)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 1)),((j + 2)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 2)), ((j + 1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 2))], color='black'))
            else:
                if (i, j) == s.start:
                    axes.add_patch(pylab.Polygon([((j + 1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 1)),((j + 2)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 1)),((j + 2)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 2)), ((j + 1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 2))], color='green'))
                else:
                    if (i, j) == s.finish:
                        axes.add_patch(pylab.Polygon([((j + 1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 1)),((j + 2)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 1)),((j + 2)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 2)), ((j + 1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 2))], color='red'))
                    else:
                        if a[i][j] == 2:
                            axes.add_patch(pylab.Polygon([((j + 1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 1)),((j + 2)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 1)),((j + 2)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 2)), ((j + 1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 2))], color='yellow'))
        axes.add_patch(pylab.Polygon([((len(a[0]) + 1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 1)),(2, -2/(len(a) + 2)*(i + 1)),(2, -2/(len(a) + 2)*(i + 2)), ((len(a[0]) + 1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(i + 2))], color='black'))
    for i in np.arange(len(a[0]) + 2):
        axes.add_patch(pylab.Polygon([(i*2/(len(a[0]) + 2), -2/(len(a) + 2)*(len(a) + 1)),((i+1)*2/(len(a[0]) + 2), -2/(len(a) + 2)*(len(a) + 1)),((i+1)*2/(len(a[0]) + 2), -2), (i*2/(len(a[0]) + 2), -2)], color='black'))
    pylab.xlim(0, 2)
    pylab.ylim(-2, 0)
    pylab.show()
    return
