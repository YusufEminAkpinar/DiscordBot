import discord
import random
from time import sleep
from reddit import red_post, secret_red_post
import sys
sys.path.insert(0, '..\\Others')
from cred import SECRET

client = discord.Client()

def percent(x):
    denom = random.randint(1, 100)
    if denom <= x:
        return True
    else:
        return False


shrek_ascii = '''
⠑⡄⠀⠀⠀⠀⠀⠀ ⠀ ⣀⣀⣤⣤⣤⣀⡀
⠸⠿⡀⠀ ⠀ ⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
'''

gif_trigger = {'sinüs', 'sin', 'cos', 'fizikçi', 'fizikçiler', 'kanit', 'kosinüs', 'cosinus', 'kanıt', 'sinus'}

@client.event
async def on_ready():
    global tilt_etme
    print('We have logged in as {}'.format(client.user))
    tilt_etme = False
    print(f'Tilt etme:{tilt_etme}')

@client.event
async def on_message(message):
    global tilt_etme
    if message.author == client.user:
        return

    message_list = message.content.lower().split()

    if message.content.startswith('!öneri'):
        suggestion = message.content[7:]
        with open('..\\Others\\yapılacaklar.txt', 'a') as file:
            file.write(f'{suggestion}\n')
        await message.channel.send(f'Öneriniz alındı. ```{suggestion}``` listeye eklendi :).')

    if message.content == '!yapılacaklar':
        with open('..\\Others\\yapılacaklar.txt', 'r') as file:
            yapilacaklar = file.read()
        await message.channel.send(f'Yapılacaklar listesi:\n{yapilacaklar}')

    # Women Moment !!!
    if message.content.lower() == '!women':
        await message.channel.send('WOMEN MOMENT!!!!')
        await message.channel.send('https://www.youtube.com/watch?v=e9mVfv3b-4E')


    if 'shrek' in message_list:
        await message.channel.send(shrek_ascii)


    if 'alper' in message_list:
        with open('..\\img\\gigachad.jpg', 'rb') as fh:
            f = discord.File(fh, filename='gigachad.jpg')
        await message.channel.send('Alper abin burda kardeşim', file=f)


    if set(message_list) & gif_trigger != set():
        with open('..\\img\\optimized_türev.gif', 'rb') as fh:
            f = discord.File(fh, filename='iki_kere_türevini_alıyorsun.gif')
        await message.channel.send(file=f)


    # tebip
    if 'tebip' in message_list:
        with open('..\\img\\Akil_Sagligini_Kaybet_Tebip.png', "rb") as fh:
            f = discord.File(fh, filename='..\\img\\Akil_Sagligini_Kaybet_Tebip.png')
        await message.channel.send('Tebip mi dedin? Bak sen Tebip diyince aklıma ne geldi...')
        await message.channel.send(file=f)

    # Average Nihat Berker Fan vs Nigar Berker Enjoyer
    if 'nigar' in message_list:
        with open('..\\img\\NigarvsNihat.mp4', "rb") as fh:
            f = discord.File(fh, filename='..\\img\\NigarvsNihat.mp4')
        await message.channel.send(file=f)


    # trappin
    if 'trappin' in message_list:
        with open('..\\img\\trappin.png', "rb") as fh:
            f = discord.File(fh, filename='..\\img\\trappin.png')
        await message.channel.send(file=f)


    # balkan momenttt
    if 'nagehan' in message_list or 'nagi' in message.content.lower():
        if percent(15):
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
    if 'köylü' in message_list or 'yavuz' in message_list:
        if percent(35):
            await message.channel.send('Köylüüüü')
            if percent(50):
                await message.channel.send('https://youtu.be/fMimbj9Q-pU')
            else:
                with open('..\\img\\anime_köylü.jpg', "rb") as fh:
                    f = discord.File(fh, filename='..\\img\\anime_köylü.jpg')
                await message.channel.send(file=f)


    # Yeterli izah yapmamışsınız. -5
    if len(str(message.content).split(' ')) < 3 and not message.content.startswith('!') and message.content != 'trappin':
        if percent(20) and len(message.content) < 10:
            if percent(3):
                await message.channel.send('Yeterli izah yapmamışsınız. -10')
                sleep(3)
                await message.channel.send('Düzeltme:  -5, yani  -10 değil')
            else:
                await message.channel.send('Yeterli izah yapmamışsınız. -5')
        else:
            pass


    # BULLY QQN
    if message.content.lower() == '!kanseraç':
        tilt_etme = True
        await message.channel.send('Kanser açık :)')
    if message.content.lower() == '!babuşkappa':
        tilt_etme = False
        await message.channel.send('Kanser Kapalı :(')
    if tilt_etme:
        if message.author.id == 755317094937264169:
            await message.channel.send('WOMEN MOMENT!!!!')
            await message.channel.send('https://www.youtube.com/watch?v=e9mVfv3b-4E')
        else:
            pass


client.run(SECRET)
