import discord
from bot_logic import gen_pass
from discord.ext import commands


# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command
#comando hello
async def hello(ctx):
    await ctx.send("Hello")

#comando bye
async def Bye(ctx):
    await ctx.send("Bye")

async def gen_pass(ctx):
    await ctx.send(gen_pass(10))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

bot.run("k")
