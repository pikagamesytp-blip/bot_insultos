import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

INSULTOS = [
    "retrasado", "tonto", "gilipollas", "cabrón", "puta", "mierda", 
    "subnormal", "imbécil", "estúpido", "retrasada", "puto", 
    "capullo", "joder", "carajo", "putada", "retrasados", "zorra", "maricón"
]

bote_insultos = {}

@client.event
async def on_ready():
    print(f'¡Bot conectado como {client.user}! Bote activo 24/7.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    contenido = message.content.lower()
    conteo_mensaje = 0
    
    for taco in INSULTOS:
        if taco in contenido:
            apariciones = contenido.count(taco)
            conteo_mensaje += apariciones

    if conteo_mensaje > 0:
        user_id = message.author.id
        bote_insultos[user_id] = bote_insultos.get(user_id, 0) + conteo_mensaje
        total_acumulado = bote_insultos[user_id]
        
        await message.channel.send(
            f"Bote de insultos: +{conteo_mensaje}. Llevas un total de **{total_acumulado}**, {message.author.mention}."
        )

    if message.content.lower() == '!bote':
        user_id = message.author.id
        total = bote_insultos.get(user_id, 0)
        await message.channel.send(f"Tu bote personal es de **{total}** insultos/tacos, {message.author.mention}.")

client.run(os.environ.get('DISCORD_TOKEN'))