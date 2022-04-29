# Script para enviar email através do Python

from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('template.html', 'r') as html:
    template = Template(html.read())
    mensagem = template.substitute(nome='Cima')

msg = MIMEMultipart()
msg['from'] = 'nome_de_quem_esta_enviando'
msg['to'] = 'email_de_quem_esta_recebendo'
msg['subject'] = 'Atenção: este é um e-mail de testes.'

corpo = MIMEText(mensagem, 'html')
msg.attach(corpo)

# Loop para enviar em sequêcia 10 vezes o mesmo email
for x in range(11):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('meu_email_vai_aqui', 'minha_senha_vai_aqui')
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')