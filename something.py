from django.template.defaultfilters import length

grades = [
    ("Аня", 5, 4, 5, 3),
    ("Боря", 3, 3, 4, 2),
    ("Ваня", 5, 5, 5, 4),
    ("Галя", 4, 4, 4, 4),
    ("Андрей", 2, 3, 2, 3),
]

filtered = filter(
    lambda row: sum(row[1:]) / len(row[1:]) >= 4,
    grades
)

result = map(
    lambda row: {
        "name": row[0],
        "avg": round(sum(row[1:]) / len(row[1:]), 2),
        "status": "Отлично" if sum(row[1:]) / len(row[1:]) >= 4.5 else "Хорошо"
    },
    filtered
)
print(list(result))

n = [1,2,3,2,1]
pal =lambda x: x == x[::-1]
#print(pal(n))#так чисто на тру чекнул

p = lambda x,y: (x+y)**2
print(p(4,5))
#tuple

w = lambda x:', '.join(x)
print(w(['виноград','сливы','яблоко одно']))
#list
dict = {'name': 'ахаха',
        'age' : 20}
introduce = lambda x : f'меня зовут {x['name']} и мне {x['age']}'
print(introduce(dict))
#на словарик

'----------------------------------------------------------------'

nums = [1,2,3,4]
sq = list(map(lambda x:x**2,nums))
print(sq)#база

words = ['чиназс','игрушка','аахаха']
length = list(map(lambda x: len(x),words))
print(length)#посчитал лен стр

pairs =[(1,2),(3,4)]
sums = list(map(lambda x : x[0]+x[1],pairs))
print(sums)#список кортежей


users = [
    {"name": "Аня", "city": "Москва"},
    {"name": "Боря", "city": "Питер"},
    {"name": "Ваня", "city": "Казань"}
    ]
info = list(map(lambda x : f'{x['name']} из {x['city']}',users))
print(info)
#словарик в стр
pairs = [(5, 3), (2, 8), (10, 1), (4, 4)]
n = list(filter(lambda x:x[0]>x[1] ,pairs))
print(n)#tuple

users = [
    {"name": "Аня", "age": 20},
    {"name": "Боря", "age": 16},
    {"name": "Ваня", "age": 18},
    {"name": "Галя", "age": 14},]

n  = list(filter(lambda x : x['age']>=18,users))
print(n)#dict
