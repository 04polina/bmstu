foot_dict = {
    'Россия': 'A',
    'Португалия': 'B',
    'Франция': 'C',
    'Дания': 'C',
    'Египет': 'A'
}

# Задание #1
foot_dict['Турция'] = 'B'

# Задание #2
group = input()
for country in foot_dict:
    if foot_dict[country] == group:
        print(country)

# Задание #3
values = list(foot_dict.values())
for i in range(len(values)):
    if not(values[i] in values[:i]):  # проверяем, что данная группа еще не встречалась в values
        # (чтобы количество стран каждой группы выводилось 1 раз)
        print(values[i]+': '+str(values.count(values[i])))

