def likes(names):
    if len(names) == 0:
        s = 'Никто не оценил данную запись'
    elif len(names) == 1:
        s = f'{names[0]} оценил(а) данную запись'
    elif len(names) == 2:
        s = f'{names[0]} и {names[1]} оценили данную запись'
    elif len(names) == 3:
        s = f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else:
        s = f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'
    return s