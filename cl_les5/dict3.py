# Дан список с посетителями ветеринарной клиники в формате
# Кличка Возраст Имя
# Оптимизировать хранение так , чтобы у каждого владельца был список собак.
# Список посетителей доступен по ссылке

data = [('Джеки', 26, 'Петр'), ('Одиссей', 21, 'Иван'), ('Эмир', 5, 'Анатолий'), ('Эмир', 48, 'Алексей'),
        ('Цезарь', 33, 'Иван'), ('Дружок', 47, 'Иван'), ('Мартин', 46, 'Петр'), ('Эмир', 13, 'Алексей'),
        ('Мартин', 36, 'Анатолий'), ('Одиссей', 17, 'Алексей'), ('Анда', 24, 'Петр'), ('Анда', 47, 'Петр'),
        ('Анда', 31, 'Анатолий'), ('Дружок', 35, 'Анатолий'), ('Шарик', 5, 'Алексей'), ('Дарман', 11, 'Анатолий'),
        ('Шарик', 46, 'Петр'), ('Джеки', 26, 'Петр'), ('Джеки', 47, 'Анатолий'), ('Мартин', 28, 'Анатолий'),
        ('Анда', 43, 'Иван'), ('Цезарь', 20, 'Анатолий'), ('Одиссей', 25, 'Петр'), ('Дружок', 13, 'Алексей'),
        ('Дарман', 25, 'Иван'), ('Дарман', 43, 'Иван'), ('Цезарь', 42, 'Анатолий'), ('Дарман', 31, 'Анатолий'),
        ('Дружок', 26, 'Иван'), ('Цезарь', 23, 'Иван')]



#d = {"<Имя владельца>": ["Собака", "Собака"]}
d = {}
for x in data:
   # dog_name=x[0]
  #  age = x[1]
  #  owner_name = x[2]
 #   print(x)

