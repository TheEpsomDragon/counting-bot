import discord
global i
i = 0


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  global i
  if message.author == client.user:
       return

  if message.content.startswith('.count'):
    i += 1
    await message.channel.send(i)
    await message.add_reaction("✅")
  if i == 100:
   await message.channel.send("TheKatDev#9725 helped me with this project and asked for credit" )



client.run('')
# Elax#6083 helped me with this project so hes amazing my discord is TheEpsomDragon#8277 also TheKatDev#9725 helped me as well
