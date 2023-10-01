import discord
import os

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

file_path = 'token.txt'
text_file_path = "output.txt"

if not os.path.exists(file_path):
    bottoken = input('Enter bot token: ')
    with open('token.txt', 'w') as file:
        file.write(bottoken)
else:
    if input("There is already a bot ID, do you want to overwrite? (Y/N) ") == "Y":
        bottoken = input('Enter BOT ID: ')
        with open('token.txt', 'w') as file:
            file.write(bottoken)
    else:
        with open('token.txt', 'r') as file:
            bottoken = file.readline()


channel_id = input("Enter Channel ID: ")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
    bot_user_id = bot.user.id
    
    invite_link = f"https://discord.com/oauth2/authorize?client_id={bot_user_id}&permissions=67648&scope=bot"
    
    print(f'Use this link to add the bot to your server')
    print(f'{invite_link}')

async def handle_message(message):
    await message.add_reaction('✅')

    with open(text_file_path, 'w', encoding='utf-8') as file:
        file.write(f"{message.content}\n")

@bot.event
async def on_message(message):
    if message.channel.id == int(channel_id):
        await handle_message(message)


bot.run(bottoken)
