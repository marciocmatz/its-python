# Formatando valores com modificadores

num1 = 1
print(f'{num1:0>10}')  # 0000000001
print(f'{num1:0<10}')  # 1000000000
print(f'{num1:0^10}')  # 0000100000
# O primeiro número vai definir com qual caractere o python deve preencher esse número, sendo assim, é possível:
print(f'{num1:#>10}')  # #########1

# Colocando e definindo o tamanho das casas decimais de um número
num2 = 10 / 3
print(f'{num2:.2f}')  # 3.33

# Limpando um CPF que foi digitado com pontos e traço:
cpf_input = input("Insira seu CPF: ")
cpf_limpo = ''

for x in cpf_input:
    x = x.replace('.', '')
    x = x.replace('-', '')
    cpf_limpo += x
cpf_limpo = int(cpf_limpo)

print(cpf_input, type(cpf_input))  # <class 'str'>
print(cpf_limpo, type(cpf_limpo))  # <class 'int'>
