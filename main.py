import discord
import asyncio

# Configura tu token aquí
TOKEN = 'tu_token_de_discord'

# Configura el intervalo de tiempo para enviar el mensaje (en segundos)
INTERVALO = 3600  # Ejemplo: mensaje cada hora

# Mensaje que deseas enviar
MENSAJE = "¡Hola! Soy un bot de Discord y estoy enviando este mensaje automáticamente."

# Inicializa el cliente de Discord
client = discord.Client()

# Función para enviar el mensaje
async def enviar_mensaje():
    await client.wait_until_ready()
    while not client.is_closed():
        # Obtiene el servidor y el canal donde deseas enviar el mensaje
        server = client.get_guild(ID_DE_TU_SERVIDOR)
        canal = server.get_channel(ID_DE_TU_CANAL)
        # Envía el mensaje
        await canal.send(MENSAJE)
        # Espera el intervalo de tiempo antes de enviar el próximo mensaje
        await asyncio.sleep(INTERVALO)

# Evento que se ejecuta cuando el bot se conecta correctamente a Discord
@client.event
async def on_ready():
    print('Bot conectado como {0.user}'.format(client))
    # Inicia la tarea para enviar mensajes automáticamente
    client.loop.create_task(enviar_mensaje())

# Ejecuta el bot con tu token
client.run(TOKEN)
