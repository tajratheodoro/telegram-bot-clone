from pyrogram import Client, filters
from pyrogram.errors import ChatWriteForbidden

# Token do bot do grupo matriz
TOKEN_MATRIZ = '000000000000000' # substitua pelo token do primeiro bot

# Token do bot do grupo clone
TOKEN_CLONE = '000000000000000' # substitua pelo token do segundo bot

# ID do grupo matriz
ID_MATRIZ = -1234567890  # substitua pelo ID do grupo matriz

# ID do grupo clone
ID_CLONE = -1234567890  # substitua pelo ID do grupo clone

# Cria o cliente do bot do grupo matriz
matriz_bot = Client('matriz_bot', bot_token=TOKEN_MATRIZ)

# Cria o cliente do bot do grupo clone
clone_bot = Client('clone_bot', bot_token=TOKEN_CLONE)

# Conecta aos clientes
matriz_bot.start()
clone_bot.start()

# Clona as mensagens do grupo matriz para o grupo clone
@matriz_bot.on_message(filters.chat(ID_MATRIZ))
async def clone_mensagem(client, message):
    try:
        await clone_bot.send_message(ID_CLONE, message.text)
    except ChatWriteForbidden:
        pass

# Apaga as mensagens do grupo clone quando forem apagadas no grupo matriz
@matriz_bot.on_deleted_messages(filters.chat(ID_MATRIZ))
async def apaga_mensagem(client, messages):
    for msg in messages:
        try:
            await clone_bot.delete_messages(ID_CLONE, msg.message_id)
        except ChatWriteForbidden:
            pass

# Mantém os clientes ativos
matriz_bot.idle()
clone_bot.idle()
