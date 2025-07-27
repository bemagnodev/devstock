import smtplib
from email.mime.text import MIMEText
import logging
import os
from dotenv import load_dotenv

load_dotenv() 

def send_email(to_email: str, subject: str, body: str):
    """
    Envia um e-mail com as informações fornecidas.
    
    :param to_email: Endereço de e-mail do destinatário
    :param subject: Assunto do e-mail
    :param body: Corpo do e-mail
    """

    # Configuração do servidor SMTP
    smtp_server  = os.getenv("SMTP_SERVER")
    smtp_port  = os.getenv("SMTP_PORT")
    smtp_username  = os.getenv("SMTP_USERNAME")
    smtp_password  = os.getenv("SMTP_PASSWORD")


    # Criação do e-mail
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = smtp_username
    msg["To"] = to_email

    try:
        # Conectar ao servidor SMTP e estabelecer a comunicação
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.set_debuglevel(1)  # Ativa o modo de debug para ver mais detalhes da conexão
            server.ehlo()  # Verifica a conexão com o servidor SMTP
            server.starttls()  # Inicia uma conexão segura (TLS)
            server.login(smtp_username, smtp_password)  # Login no servidor
            server.sendmail(smtp_username, to_email, msg.as_string())  # Envia o e-mail

        logging.info(f"E-mail enviado com sucesso para {to_email}.")
    except Exception as e:
        logging.error(f"Erro ao enviar o e-mail: {e}")
        raise

