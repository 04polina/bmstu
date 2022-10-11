persons = list()

bestB = {'res': '10000'} # лучший мальчик
bestG = {'res': '10000'} # лучшая девочка

with open("run_of_60_m.txt", "r") as file:
    for line in file:
        line = line.rstrip('\n')
        name, year, gen, res = line.split()
        person = {
            'name': name,
            'year': year,
            'gen': gen,
            'res': res,
        }
        year = int(year)
        res = float(res)

        # Определение оценки
        mark = 0
        if gen == 6:
            if gen == 'b': # если мальчик
                if res <= 9.9:
                    mark = 5
                elif res <= 10.4:
                    mark = 4
                elif res <= 11.1:
                    mark = 3
                else:
                    mark = 2
            else: # иначе, если девочка
                if res <= 10.3:
                    mark = 5
                elif res <= 10.6:
                    mark = 4
                elif res <= 11.2:
                    mark = 3
                else:
                    mark = 2
        else:
            if gen == 'b': # если мальчик
                if res <= 9.4:
                    mark = 5
                elif res <= 10.2:
                    mark = 4
                elif res <= 11.0:
                    mark = 3
                else:
                    mark = 2
            else: # иначе, если девочка
                if res <= 9.8:
                    mark = 5
                elif res <= 10.6:
                    mark = 4
                elif res <= 11.4:
                    mark = 3
                else:
                    mark = 2
        # Добавление оценки в словарь
        person['mark'] = str(mark)
        persons.append(person)

        if gen == 'g':
            if float(bestG['res']) > res:
                bestG = person
        else:
            if float(bestB['res']) > res:
                bestB = person

with open("run_of_60_ mark.txt", "w") as file:
    file.writelines(
        "%s\n" % (i['name'] + " " + i['year'] + " " + i['gen'] + " " + i['res'] + " " + i['mark']) for i in persons)

print("Лучшая девочка\n" + bestG['name'] + " " + bestG['year'] + " " + bestG['gen'] + " " + bestG['res'] + " " + bestG['mark'])
print("Лучший мальчик\n" + bestB['name'] + " " + bestB['year'] + " " + bestB['gen'] + " " + bestB['res'] + " " + bestB['mark'])
