#   Выполнение практического задания по уроку "Неизменяемые и изменяемые объекты. Кортежи"
#   Студент: Костромин Александр Анатольевич
#
#
# Задаем переменные разных типов данных:
#
# Создаем переменную immutable_var и присвоим ей кортеж из нескольких элементов разных типов данных.
immutable_var = True, 'abc', [1, 2, 3]
#
# Выведим кортеж на экран
print(immutable_var)
#
# Изменяем значения переменных:
# Попытаемся изменить элементы кортежа immutable_var.
try:
    immutable_var[0] = False
except:
    print('Кортеж является неизменяемым типом данных')
#
# Создаем изменяемые структуры данных:
#
# Создаем переменную mutable_list и присваиваем ей список из нескольких элементов.
mutable_list = [True, 'abc', [1, 2, 3]]
print(mutable_list)
# Изменяем элементы списка mutable_list.
mutable_list[0] = False
mutable_list[1] = 'cba'
mutable_list[-1] = [3, 2, 1]
# Выводим на экран измененный список mutable_list.
print(mutable_list)