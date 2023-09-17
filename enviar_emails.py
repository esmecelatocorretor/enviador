import smtplib
import csv
import random
import time

# Configuração SMTP para o Hotmail/Outlook
smtp_server = 'smtp.live.com'  # Ou 'smtp-mail.outlook.com'
smtp_port = 587
username = 'esmecelato@hotmail.com'
password = 'kPEn6xFZwfKCEE'

# Ler a lista de e-mails do arquivo CSV
with open('lista_emails.csv', 'r') as file:
    reader = csv.reader(file)
    email_list = list(reader)

while True:
    # Escolher um e-mail aleatório da lista
    random_email = random.choice(email_list)

    try:
        # Configurar a conexão SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)

            # Preencher o corpo do e-mail
            subject = 'Apresentação - Corretor de Imóveis Edson Esmecelato'
            body = '''
            Seu corpo de e-mail aqui...
            '''

            message = f'{body}'

            # Não é necessário incluir 'Subject' no cabeçalho do e-mail
            server.sendmail(username, random_email, message)

        print(f'E-mail enviado para {random_email}')
    except smtplib.SMTPException as e:
        print(f"Erro ao enviar o e-mail: {str(e)}")

    # Esperar 5 minutos antes de enviar o próximo e-mail (300 segundos)
    time.sleep(300)