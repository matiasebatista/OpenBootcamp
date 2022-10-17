import time

tiempo = time.localtime()
print(tiempo)


def decirTiempo():
    return "hora: " + str(time.localtime().tm_hour) + "\nmin: " + str(time.localtime().tm_min) + "\nfecha:" + str(
        time.localtime().tm_mday) + "/" + str(time.localtime().tm_mon) + "/" + str(time.localtime().tm_year)


def salida():
    if time.localtime().tm_hour >= 19:
        return "Ya puede irse a su casa"
    else:
        return 19 - time.localtime().tm_hour


print(decirTiempo())
print(salida())
