import PySimpleGUI as sg
import matze
import drawing

sg.theme('DarkAmber')
form = sg.FlexForm('Генератор лабиринтов')
layout = [[sg.Text('Введите размеры лабиринта и (по желанию) координаты (через запятую) старта и финиша')],
          [sg.Text('n:', size=(10, 1)), sg.InputText(), sg.Text('m:', size=(10, 1)), sg.InputText()],
          [sg.Text('start:', size=(10, 1)), sg.InputText(), sg.Text('finish:', size=(10, 1)), sg.InputText()],
          [sg.Text('Выберите алгоритм генерации:', size=(30, 1)), sg.InputCombo(('dfs', 'mst'), size=(20, 3))],
          [sg.Text('имя файла:', size=(15, 1)), sg.InputText()],
          [sg.Button('Генерировать'), sg.Button('Вывести'), sg.Button('Решить'), sg.Button('Сохранить')],
          [sg.Button('Загрузить'), sg.Button('Закрыть')]]

window = sg.Window('Генератор лабиринтов', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Закрыть':
        break
    
    if event == 'Генерировать':
        if values[0] == '' or values[1] == '' or values[4] == '':
            print('Заполните поля n, m и выберите алгоритм')
            continue
        else:
            try:
                n1 = int(values[0])
                n2 = int(values[1])
                if n1 < 1 and n2 < 1:
                    raise Exception
            except:
                print('Введены некорректные размеры лабиринта. Должно быть два натуральных числа')
            if values[2] == '':
                start = (0, 0)
            else:
                try:
                    start = tuple([int(i) for i in values[2].split(',')])
                    if start[0] > n1 or start[0] < 0 or start[1] > n2 or start[1] < 0:
                        print('Недопустимые координаты старта')
                        raise Exception
                except:
                    print('Введены некоректные координаты старта. Они должны быть в промежутке [0, n), [0, m)')
            if values[3] == '':
                finish = 0
            else:
                try:
                    finish = tuple([int(i) for i in values[3].split(',')])
                    if finish[0] > n1 or finish[0] < 0 or finish[1] > n2 or finish[1] < 0:
                        print('Недопустимые координаты финиша')
                        raise Exception
                except:
                    print('Введены некоректные координаты финиша. Они должны быть в промежутке [0, n), [0, m)')
            a = matze.matze(int(values[0]), int(values[1]), start, finish)
            if values[4] == 'dfs':
                a.dfs()
            else:
                a.mst()
            drawing.pr_matze(a)

    if event == 'Вывести':
        try:
            print(a)
            drawing.pr_matze(a)
        except:
            print('Что-то пошло не так. Возможно, вы еще не создали или не загрузили лабиринт')

    if event == 'Решить':
        try:
            a.solve()
            drawing.pr_matze(a, 1)
        except:
            print('Сначала сгенерируйте или загрузите лабиринт!')
            continue
    
    if event == 'Сохранить':
        if values[5] == '' or values[5][-4:] != '.txt':
            print('Заполните имя файла(формат .txt)')
        try:
            a.save(values[5])
        except:
            print('Возможно лабиринт не сгенерирован или введено некорректное имя файла')
    
    if event == 'Загрузить':
        if values[5] == '' or values[5][-4:] != '.txt':
            print('Заполните имя файла(формат .txt)')
            continue
        try:
            a = matze.matze()
            a = a.upload(values[5])
            print(a)
        except:
            print('Проверьте наличие данного файла')
            continue

window.close()
