entrada = input('de que horas você entrou? HH:MM\n').strip().split()

for time in entrada:
    hour, minu = [int(i) for i in time.split(":")]
    print(hour, "hours and", minu, "minutes")
    print(type(hour))
