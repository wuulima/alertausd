import requests
import smtplib
import email.message

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])

# Enviar E-mail
def enviar_email(cotacao):
    corpo_email = f"""
    <p>Dólar está abaixo de R$ 5.35. Cotação atual: R${cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Dólar está hoje abaixo de R$5.35"
    msg['From'] = 'wuulima@gmail.com'
    msg['To'] = 'segurancati.deinf@gmail.com'
    password = 'rvsauazbhodznwif'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao < 5.35:
    enviar_email(cotacao)
