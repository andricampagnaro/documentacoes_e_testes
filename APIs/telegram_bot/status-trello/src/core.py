import requests
import json
from future import builtins
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, TELEGRAM_WHITE_LIST, TRELLO_API_URL, TRELLO_KEY, TRELLO_TOKEN
from functools import wraps

COMANDOS_VALIDOS = "\n".join(['/boards', '/cards'])

def valida_usuario(funcao):
    @wraps(funcao)
    def funcao_decorada(*args, **kwargs):
        # if args[1].message.chat_id in [1195845295]:
        if args[1].message.chat_id in TELEGRAM_WHITE_LIST:
            funcao(*args, **kwargs)
        else:
            unautorized(*args, **kwargs)
            print(f"Usuário {args[1].message.chat_id} não autorizado")
    return funcao_decorada


@valida_usuario
def start(bot, update):
    response_message = "Bem vindo ao trello.\nAguarde enquanto carregamos as informações."
    
    bot.send_message(
        chat_id = update.message.chat_id,
        text = response_message
    )
    
    response_message = f"Tudo pronto. Pode utilizar.\nVocê pode executar os seguintes comandos:\n{COMANDOS_VALIDOS}"
    
    bot.send_message(
        chat_id = update.message.chat_id,
        text = response_message
    )


@valida_usuario
def boards(bot, update):
    response = requests.get(f'{TRELLO_API_URL}/members/me/boards?key={TRELLO_KEY}&token={TRELLO_TOKEN}')
    _boards = [board['name'] for board in json.loads(response.content)]
    print([board['id'] for board in json.loads(response.content)])

    bot.send_message(
        chat_id = update.message.chat_id,
        text = "\n".join(_boards)
    )


@valida_usuario
def cards(bot, update):
    response = requests.get(f'{TRELLO_API_URL}/boards/5bf4394c13dbde47bb9cb8dc/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}')
    # response = requests.get(f'{TRELLO_API_URL}/boards/5ef4a9dfbc0b655c0571b53e/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}')
    # response_dict = json.loads(response.content)
    cards_names = [card['name'] for card in json.loads(response.content)]

    for card_name in cards_names:
        bot.send_message(
            chat_id = update.message.chat_id,
            text = card_name
            # text = f"{card['name']}\n{card['desc']}\n{card['due']}\n\n{card['labels']}"
        )


@valida_usuario
def card(bot, update):
    response = requests.get(f'{TRELLO_API_URL}/search?query=name:"Intymidade"&idBoards=5bf4394c13dbde47bb9cb8dc&key={TRELLO_KEY}&token={TRELLO_TOKEN}')
    _cards = {chave: valor for chave, valor in json.loads(response.content).items() if chave == 'cards'}
    for chave, valor in _cards.items():
        print(chave, valor)
    
    bot.send_message(
        chat_id = update.message.chat_id,
        text = f"hello"
    )

def unknown(bot, update):
    response_message = f"Comando desconhecido. Você pode utilizar os seguintes comandos:\n{COMANDOS_VALIDOS}"
    bot.send_message(
        chat_id = update.message.chat_id,
        text = response_message
    )


def unautorized(bot, update):
    response_message = "Você não tem autorização para executar esse processo."
    bot.send_message(
        chat_id = update.message.chat_id,
        text = response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('cards', cards)
    )
    dispatcher.add_handler(
        CommandHandler('card', card)
    )

    dispatcher.add_handler(
        CommandHandler('boards', boards)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("Press CTRL + C to cancel.")
    main()