import telebot

CHAVE_API = "7161976316:AAEMoXADLn2jabivOJ5mkL6HXN0HrCOJkM0"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["TShirtPequena"])
def TShirtPequena(mensagem):
   bot.send_message(mensagem.chat.id, "entre em contato com 85985533178, Clique aqui para o menu inicial: /iniciar")

@bot.message_handler(commands=["TShirtMedia"])
def TShirtMedia(mensagem):
    bot.send_message(mensagem.chat.id, "entre em contato com 85985533178, Clique aqui para o menu inicial: /iniciar")


@bot.message_handler(commands=["TshirtGrande"])
def TshirtGrande(mensagem):
    bot.send_message(mensagem.chat.id, "entre em contato com 85985533178, Clique aqui para o menu inicial: /iniciar")


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
   O que você quer? (Clique em uma opção)
   /TShirtPequena
   /TShirtMedia
   /TshirtGrande"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para fazer um reclamção, entre em contato com 85985533178")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Obrigado! Volte sempre!")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma das opções para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Encerrar
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()
