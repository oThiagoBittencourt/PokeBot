from pokemon_api import PokeAPI
import telebot

API_KEY = "7242496023:AAE2CzX2FphfnR5PvyoeJqVvmvnJIC1mcRg"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Use o comando /pokemon <nome> para buscar por um Pokémon.")

@bot.message_handler(commands=['pokemon'])
def search(message):
    try:
        search_query = message.text.split(maxsplit=1)
        
        if len(search_query) > 1:
            query = search_query[1]
            bot.reply_to(message, f"Você buscou por: {query}")
            response = PokeAPI.search_pokemon(name=query)
            if not response:
                bot.reply_to(message, "Pokémon não encontrado, tente novamente! Exemplo: /pokemon pikachu")
        else:
            bot.reply_to(message, "Por favor, forneça um termo para busca após o comando. Exemplo: /pokemon pikachu")
    except:
                bot.reply_to(message, "Ocorreu um erro, tente novamente.")

def verify(msg):
    return True

@bot.message_handler(func=verify)
def default_response(msg):
    text = "Comando não encontrado\n\t/commands para ver todos os comandos!"
    bot.send_message(msg.chat.id, text)

bot.polling()