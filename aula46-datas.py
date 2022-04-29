from datetime import datetime, timedelta

#               YEAR  M   D   H   M   S
data = datetime(2020, 4, 20, 10, 53, 20)
print(data)  # Vai retornar no padrão norte americado (2020-04-20 10:53:20)

print(data.strftime('%d/%m/%Y %Hh%M'))  # Assim é possível manipular o formato. Nesse caso, será: 20/04/2020 10h53

# Timestamp
print(data.timestamp())
data = data.fromtimestamp(1801090009.0)
print(data)

# Somando valores as datas
data = datetime.strptime('16/03/1998 15h50', '%d/%m/%Y %Hh%M')
print(data)
data = data + timedelta(days=1000)
print(data)  # Vai apresentar a data mais 1000 dias.

# Calculando diferencã entre duas datas
data1 = datetime.strptime('16/03/1998 15h50', '%d/%m/%Y %Hh%M')
data2 = datetime.now()
print(data1)
print(data2)

dif = data2 - data1
print(f'Segundos: {dif.seconds}')
print(f'Dias: {dif.days}')