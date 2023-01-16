##################################### Importando librerias ###########################################################
import os 
from dotenv import load_dotenv
from discord.ext import commands
import discord
from urllib import request , parse
import re 


load_dotenv()

#################################### Abriendo el archivo que contiene la clave ###################################################################
KEY = os.environ['KEY_BOOT']

############################################### Comandos para el bot ###############################################################################################
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='')


############################################ Funcionalidades para el bot ##################################################################
@bot.command()
async def Hola(ctx): 
    '''funcion ...'''
    resultado = 'Hola julieta :)'
    await ctx.send(resultado)


@bot.command()
async def YouTube(ctx,*, search):
    query = parse.urlencode({'search_query': search})

    html1 = request.urlopen('http://www.youtube.com/results?'+ query)
    search_results= re.findall('watch\?v=(.{11})',html1.read().decode('utf-8'))
    resultado = 'https://www.youtube.com/watch?v=' + search_results[0]
    #print(resultado)
    await ctx.send(resultado)



bot.run(KEY) ################ 