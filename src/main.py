import discord
import random
from time import sleep
from reddit import red_post, secret_red_post
import sys
sys.path.insert(0, 'C:\\Users\\Hardal\\PycharmProjects\\dc_bot\\Others')
from cred import SECRET

client = discord.Client()

def percent(x):
    denom = random.randint(1, 100)
    if denom <= x:
        return True
    else:
        return False


@client.event
async def on_ready():
    print('We have logged in as {}'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    # BULLY QQN
    tilt_etme = False
    if message.content.lower() == '!kanseraç':
        tilt_etme = True
        await message.channel.send('Kanser açık :)')
    if message.content.lower() == '!kanserkapat':
        tilt_etme = False
    if message.author.id == 954666083544096838:
        if tilt_etme:
            await message.channel.send('WOMEN MOMENT!!!!')
            await message.channel.send('https://www.youtube.com/watch?v=e9mVfv3b-4E')


    # Women Moment !!!
    if message.content.lower() == '!women':
        await message.channel.send('WOMEN MOMENT!!!!')
        await message.channel.send('https://www.youtube.com/watch?v=e9mVfv3b-4E')


    # tebip
    if 'tebip' in message.content.lower():
        with open('..\\img\\Akil_Sagligini_Kaybet_Tebip.png', "rb") as fh:
            f = discord.File(fh, filename='..\\img\\Akil_Sagligini_Kaybet_Tebip.png')
        await message.channel.send('Tebip mi dedin? Bak sen Tebip diyince aklıma ne geldi...')
        await message.channel.send(file=f)


    # trippin
    if 'trappin' in message.content.lower():
        with open('..\\img\\trappin.png', "rb") as fh:
            f = discord.File(fh, filename='..\\img\\trappin.png')
        await message.channel.send(file=f)


    # balkan momenttt
    if 'nagehan' in message.content.lower() or 'nagi' in message.content.lower():
        if percent(30):
            await message.channel.send('NAGEHAN MII\nBALKAN MOMENT!?!??!')
            await message.channel.send('https://www.youtube.com/watch?v=HfFx5UvzSxc')


    # reddit post
    if message.content.startswith('!reddit'):
        subred = str(message.content.split(' ')[1])
        await message.channel.send(await red_post(subred))


    # reddit post nsfw (sıkıntılı olmadığından emin olduğumuz zaman)
    if message.content.startswith('!peddit'):
        subred = str(message.content.split(' ')[1])
        await message.channel.send(await secret_red_post(subred))


    # Köylü takla
    if 'köylü' in message.content.lower() or 'yavuz' in message.content.lower():
        await message.channel.send('Köylüüüü')
        if percent(50):
            await message.channel.send('https://youtu.be/fMimbj9Q-pU')
        else:
            with open('..\\img\\anime_köylü.jpg', "rb") as fh:
                f = discord.File(fh, filename='..\\img\\anime_köylü.jpg')
            await message.channel.send(file=f)


    # Yeterli izah yapmamışsınız. -5
    if len(str(message.content).split(' ')) < 3 and not message.content.startswith('!') and message.content != 'trappin':
        if percent(20):
            if percent(3):
                await message.channel.send('Yeterli izah yapmamışsınız. -10')
                sleep(3)
                await message.channel.send('Düzeltme:  -5, yani  -10 değil')
            else:
                await message.channel.send('Yeterli izah yapmamışsınız. -5')
        else:
            pass


client.run(SECRET)
