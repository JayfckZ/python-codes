def transformaHoras(horario):
    modo = detector(horario)
    horas = minutos = segundos = 0
    try:
        if modo == 1:
            horas = int(horario[0:2])
            minutos = int(horario[3:5])
            segundos = int(horario[6:])
        elif modo == 2:
            horas = int(horario[0:2])
            minutos = int(horario[3:])
        elif modo == 3:
            minutos = int(horario[0:2])
            segundos = int(horario[3:])
        elif modo == 4:
            segundos = int(horario)
    except(ValueError):
        return "Não foi possível converter os valores em números."
        

    if segundos & segundos >= 60:
        segundos -= 60
        minutos += 1
    if minutos & minutos >= 60:
        minutos -= 60
        horas += 1
    
    minutos += horas * 60
    segundos += minutos * 60

    return segundos


def detector(horario):
    "00:00:00"
    if len(horario) == 8:
        return 1
    elif len(horario) == 5:
        op = int(input("O horário está em qual modelo?\n1- Horas e Minutos\n2- Minutos e Segundos\nEscolha: "))
        if op == 1:
            return 2
        return 3
    elif len(horario) == 2:
        return 4


print(transformaHoras("hh:56"))