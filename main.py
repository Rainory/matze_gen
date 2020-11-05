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
          [sg.Button('Генерировать'), sg.Button('Решить'), sg.Button('Сохоанить')],
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
            if values[2] == '':
                start = (0, 0)
            else:
                start = tuple([int(i) for i in values[2].split(',')])
            if values[3] == '':
                finish = 0
            else:
                finish = tuple([int(i) for i in values[3].split(',')])
            a = matze.matze(int(values[0]), int(values[1]), start, finish)
            if values[4] == 'dfs':
                a.dfs()
            else:
                a.mst()
            drawing.pr_matze(a)
        
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
            print('Сначала сгенерируйте лабиринт!')
    
    if event == 'Загрузить':
        if values[5] == '' or values[5][-4:] != '.txt':
            print('Заполните имя файла(формат .txt)')
            continue
        try:
            a = matze.matze()
            a.upload(values[5])
        except:
            print('Проверьте наличие данного файла')
            continue

window.close()
