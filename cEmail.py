import re
import smtplib


class cEmail(object):
    """
    Classe para realizar o envio de e-mails.
    Apenas para estudos.
    """

    verificar_email = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    def __init__(self, email=False, smtp=False, senha=False, remetente=False, destinatario=False, mensagem=False,
                 assunto=False, destinatario_nome=False, remetente_nome=False):
        self.email = email
        self.senha = senha
        self.smtp = smtp
        self.remetente = remetente
        self.destinatario = destinatario
        self.mensagem = mensagem
        self.assunto = assunto
        self.destinatario_nome = destinatario_nome
        self.remetente_nome = remetente_nome
        self.analisar_argumentos()

    def analisar_argumentos(self):
        if self.email == False or self.smtp == False or self.senha == False or self.remetente == False or self.destinatario == False or self.mensagem == False or self.assunto == False or self.destinatario_nome == False or self.remetente_nome == False:
            print("Oops.. você esqueceu de inserir algum argumento.")
        else:
            if not self.verificar_email.match(self.email):
                print("E-mail inválido.")
            else:
                self.testar_conexao()

    def testar_conexao(self):
        try:
            self.cemail = smtplib.SMTP_SSL(self.smtp)
            self.testar_autenticacao()
        except:
            print("Ocorreu um erro ao conectar com o servidor SMTP.")

    def testar_autenticacao(self):
        try:
            self.cemail.ehlo()
            self.cemail.login(str(self.email), str(self.senha))
            self.enviar_mensagem()
        except:
            print("Ocorreu um erro ao tentar efetuar o login no servidor SMTP.")
            print("\n*: Servidor SMTP - OK\n*: Login no servidor - NULL")

    def enviar_mensagem(self):
        try:
            msg = """From: {r_nome} <{remetente}>
To: {d_nome} <{destinatario}>
Subject: {assunto}

{mensagem}""".format(remetente=self.remetente, destinatario=self.destinatario, assunto=self.assunto,
                     mensagem=self.mensagem, r_nome=self.remetente_nome, d_nome=self.destinatario_nome)
            self.cemail.sendmail(self.remetente, self.destinatario, msg)
        except:
            print("Ocorreu um erro ao enviar o e-mail.")
            print("\n*: Servidor SMTP - OK\n*: Dados válidos - OK\n*: E-mail enviado - NULL")
        else:
            print("\n*: Servidor SMTP - OK\n*: Dados válidos - OK\n*: E-mail enviado - OK")

    def __str__(self):
        return "E-mail: " + str(self.email)
