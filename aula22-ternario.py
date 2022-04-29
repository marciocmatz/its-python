# Operador ternário

logged_user = True

if logged_user:
    msg = 'Usuário Logado.'
else:
    msg = 'Usuário Não Logado.'
print(msg)

msg = 'Usuário Logado.' if logged_user else 'Usuário Não Logado.'
print(msg)

# os dois codes acima tem o mesmo valor.
