from collections import defaultdict


def smartdict_nan(key):
    return 10 * key


N = 10

smartdict = {}
for key in range(N):
    val = defaultdict(lambda key=key: smartdict_nan(key))
    smartdict[key] = val

'''
Код работает неверно из-за особенностей области видимости в цикле.
Питон пытается запоминать имя и поле видимости объекта, а не сам объект.
Создавая lambda функции, мы по сути производим одну и ту же в смысле имени и поля видимости функции,
из-за чего обращение и происходит только к одной из них (последней).
Добавив аргумент по умолчанию, мы изменили структуру lambda функции ->
теперь мы стали указывать на другой объект со своей уникальной структурой (значением по умолч).
Поэтому перекрытий в таком случае нет.
'''
