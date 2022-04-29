def convert_numero(num):  # Aqui é a definição da função
    try:  # Primeira tentativa
        num = int(num)  # Vai tentar transformar o input em inteiro
        return num  # Caso transforme vai retornar o num e finalizar a função
    except ValueError:  # Primeiro erro que pode acontecer: não ser possível transformar em inteiro
        try:  # Segunda tentativa (so vai acontecer se o primeiro caso der erro)
            num = float(num) # Vai tentar transformar o input em float
            return num # Caso transforme vai retornar o num e finalizar a função
        except ValueError: # Segudno erro que pode acontecer: não ser possível transformar em float
            print('Isso não é um número.')  # Vai ser excutado caso os dois erros possíveis aconteçam
# Caso a função chegue ate o fim, será retornardo o valor None (é padrão do python isso)

while True:
    numero = convert_numero(input('Digite um número: '))  # Aqui é passado um input para a função e chama ela pra executar

    if numero is not None:  # Vai verificar qual o retorno da função e caso não seja none, vai executar
        print(numero * 5)
