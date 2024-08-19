data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_ = 0


def int_(num_cycl):
    global sum_
    if isinstance(num_cycl, int):               # Проверка на число
        sum_ += num_cycl
        return sum_
    else:
        return sum_


def str_(num_cycl):
    global sum_
    if isinstance(num_cycl, str):               # Проверка на строку
        sum_ += len(num_cycl)
        return sum_
    else:
        return sum_


def _list(num_cycl):
    global sum_
    if isinstance(num_cycl, list):
        for core_list in num_cycl:
            int_(core_list)                     # Проверка на спсиок
            str_(core_list)
            _dict(core_list)
            _set(core_list)
            _tuple(core_list)
    else:
        return sum_


def _set(num_cycl):
    global sum_
    if isinstance(num_cycl, set):
        for core_set in num_cycl:
            int_(core_set)                       # Проверка на множество
            str_(core_set)
            _dict(core_set)
            _tuple(core_set)
            _set(core_set)
    else:
        return sum_


def _dict(num_cycl):
    global sum_
    if isinstance(num_cycl, dict):
            for key, value in num_cycl.items():
                int_(key)
                str_(key)                       # Проверка на словарь
                int_(value)
                str_(value)
    else:
        return sum_


def _tuple(num_cycl):
    global sum_
    if isinstance(num_cycl, tuple):
        for core_tuple in num_cycl:
            _list(core_tuple)     # Проверка на кортеж
            _dict(core_tuple)
            int_(core_tuple)
            str_(core_tuple)
            _tuple(core_tuple)
    else:
        return sum_


def sum_obj(list_):
    global sum_
    for num_ in list_:
        int_(num_)
        str_(num_)
        _list(num_)
        _dict(num_)
        _set(num_)
        _tuple(num_)
    print(sum_)


sum_obj(data_structure)
