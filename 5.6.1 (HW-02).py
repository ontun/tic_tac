def display(output_matrix): # функция отображения игрового поля
    for i in range(4):
        print(*output_matrix[i])

def tic_tac(M,line,column): # функция присваивающая полю крестик или нолик, также проверяет не победил ли какой-то
    # игрок или не заполнилось все игровое поле

    if any([all([M[1][1]=='0', # проверка нулевой строки на заполнение только ноликами или крестиками
            M[1][2]=='0',
            M[1][3]=='0']),
            all([M[1][1]=='x',
            M[1][2]=='x',
            M[1][3]=='x'])]):
        return True
    for i in range(2,4): # проверка 1 и 2 строки на заполнение только крестиками
        if '-' not in M[i] and '0' not in M[i]:
            return True
    for i in range(2,4): # проверка 1 и 2 строки на заполнение только ноликами
        if '-' not in M[i] and 'x' not in M[i]:
            return True
    if  any([all([M[1][1]=='0', # проверка нулевого столбца на заполнение только ноликами или крестиками
            M[2][1]=='0',
            M[3][1]=='0']),
            all([M[1][1]=='x',
            M[2][1]=='x',
            M[3][1]=='x'])]):
        return True
    if  any([all([M[1][2]=='0', # проверка первого столбца на заполнение только ноликами или крестиками
            M[2][2]=='0',
            M[3][2]=='0']),
            all([M[1][2]=='x',
            M[2][2]=='x',
            M[3][2]=='x'])]):
        return True
    if  any([all([M[1][3]=='0', # проверка первого столбца на заполнение только ноликами или крестиками
            M[2][3]=='0',
            M[3][3]=='0']),
            all([M[1][3]=='x',
            M[2][3]=='x',
            M[3][3]=='x'])]):
        return True
    if any([all([M[1][1] == '0', # проверка главной диагонали на заполнение только ноликами или крестиками
               M[2][2] == '0',
               M[3][3] == '0']),
           all([M[1][1] == 'x',
               M[2][2] == 'x',
               M[3][3] == 'x'])]):
        return True
    if any([all([M[1][3] == '0', # проверка побочной диагонали на заполнение только ноликами или крестиками
               M[2][2] == '0',
               M[3][1] == '0']),
           all([M[1][3] == 'x',
               M[2][2] == 'x',
               M[3][1] == 'x'])]):
        return True

    if '-' not in M[1] and '-' not in M[2] and '-' not in M[3]: #проверка заполнены все поля или нет
        return True




M = [(' ', '0', '1', '2'),
    ['0','-','-','-'],
    ['1','-','-','-'],
    ['2','-','-','-'],
    ]

end=False
move=''

while move!='x' and move!='0' and move!='e': #цикл с выбором нолик или крестик будет первым присвоен полю

    move=input('Выберите крестик или нолик будет первым нарисован?,\Введите x - если крестик\nВведите 0 - если нолик\nВведите e для выхода :\n')
    if move=='x':
        print('Выбраны крестики')
    elif move=='0':
        print('Выбраны нолики')
    elif move=='e':
        end=True
    else:
        print('Вы не выбрали, кто будет ходить первым')

while end!=True: # цикл с вводом индексов ячейки игрового поля пользователем, для внесения в ячейку крестика или нолика
    display(M)
    numbers=input('Выберите поле,введите пару чисел через пробел, которая соответствует выбранному вами полю(например 1-строка 2-столбец)\n')

    numbers_list=numbers.split()
    try:# попытка преобразовать введеные строки в целые числа, пре ошибке преобразования обработка исключений, и повторный ввод чисел
        if (int(numbers_list[0])>2 or int(numbers_list[0])<0) and  (int(numbers_list[1])>2 or int(numbers_list[1])<0): #проверка
            # введеных чисел на попадание в диапазон игрового поля
            print('Вы ввели числа, не попадающие в поле, попробуйте снова')
        else:
            if M[int(numbers_list[0]) + 1][int(numbers_list[1]) + 1] == '0' or M[int(numbers_list[0]) + 1][int(numbers_list[1]) + 1] == 'x': #проверка не поставлен ли в этот поле крестик или нолик
                print('Это поле занято, попробуйте снова')
            else:
                M[int(numbers_list[0]) + 1][int(numbers_list[1]) + 1] = move #присвоение полю крестика или нолика

                end=tic_tac(M, int(numbers_list[0]), int(numbers_list[1]))
                if move=='x': # Смена хода игроков
                    move='0'
                else:
                    move='x'
    except:
        print('Вы ввели не числа или меньше двух чисел, попробуйте снова')

display(M)