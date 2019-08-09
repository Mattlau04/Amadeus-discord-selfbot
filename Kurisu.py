#Made with love by Mattlau04
#Also yes name is a reference to Makise Kurisu from steins;gate (and the ai with her personality named amadeus)

print("  /$$$$$$                                /$$                                                   `-:///-`")
print(" /$$__  $$                              | $$                                                 -oyyyyyyyys-")
print("| $$  \ $$ /$$$$$$/$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$$                  :ssssssssssyh/")
print("| $$$$$$$$| $$_  $$_  $$ |____  $$ /$$__  $$ /$$__  $$| $$  | $$ /$$_____/                  ssyyysyyyysyhh-")
print("| $$__  $$| $$ \ $$ \ $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  | $$|  $$$$$$                   syyshyysoyyyhds")
print("| $$  | $$| $$ | $$ | $$ /$$__  $$| $$  | $$| $$_____/| $$  | $$ \____  $$                  oyy::-.`.:yyhdd`")
print("| $$  | $$| $$ | $$ | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$/ /$$$$$$$/                  :yho.```./yhddd:")
print("|__/  |__/|__/ |__/ |__/ \_______/ \_______/ \_______/ \______/ |_______/                   `hydds+/+sdddmmo")
print("                                                                                             yhhddhs+ydosdmh")
print("                                                                                             -hys+y/ohy:.-od`")
print("                                                                                              -.:s//y:.```.h-")
print("       /$$$$$$            /$$  /$$$$$$  /$$                   /$$                            ``.o+`::.````-d/")
print("      /$$__  $$          | $$ /$$__  $$| $$                  | $$                            .`+/....````.sdo")
print("     | $$  \__/  /$$$$$$ | $$| $$  \__/| $$$$$$$   /$$$$$$  /$$$$$$                        `.../-..-````.+mds")
print("     |  $$$$$$  /$$__  $$| $$| $$$$    | $$__  $$ /$$__  $$|_  $$_/                      ``..`.:.`.```..:hmdy")
print("      \____  $$| $$$$$$$$| $$| $$_/    | $$  \ $$| $$  \ $$  | $$                        .````./:-``..-:ommdh")
print("      /$$  \ $$| $$_____/| $$| $$      | $$  | $$| $$  | $$  | $$ /$$                    ```..:--....:::dmddh")
print("     |  $$$$$$/|  $$$$$$$| $$| $$      | $$$$$$$/|  $$$$$$/  |  $$$$/                    `.``:::---.:-.:dddhs")
print("      \______/  \_______/|__/|__/      |_______/  \______/    \___/                         ````..-.....+dd//")
print("                                                                                            ``..``````..-hy-`")
print("")
print("")

try: #import default dependencies
    import sys
    import subprocess
    import os
except Exception as p:
    print(p)

def restart():
    if sys.platform.startswith('win32'): #The restart part was dev by me for RTB so i'm not stealing lol
        os.system('cls')
        os.system('cmd /C Kurisu.py')
        os.system('exit')
    else:
        os.system('clear')
        os.system('python3 Kurisu.py')
        sys.exit()

try: #importing dependencies (stolen from RTB lol)
    import discord
    from discord.ext import commands
except Exception as i:
    try:
        window.Close()
    except Exception:
        pass
    print ("Module error: " + str(i))
    install = input ("Would you like to try and install it?(Y/N)")
    if install.lower() == 'y':
        if sys.platform.startswith('win32'):
            try:
                import pip
            except Exception as e:
                print("Hmmm, pip doesn't seem to be installed so the dependencies can't be installed.")
                print("Please manually install")
                input()
                sys.exit()
            requirements = open("requirements.txt").read().splitlines()
            log = open("install.log", "w")
            for package in requirements:
                print("Attempting to install {}".format(package))
                p = subprocess.call([sys.executable, "-m", "pip", "install", package, "--user"],stdout=log, stderr=subprocess.STDOUT)
                if p == 1:
                    print("There was an error with installing the package {}, Refer to Install.log".format(package))
                elif p == 0:
                    print("Installed {} Successfully.".format(package))
            restart() #The restart part was dev by me for RTB so i'm not stealing lol
    else:
        sys.exit()

def configsetup():
    configstp = {}
    print("Welcome to the config setup of the amadeus selfbot")
    print("=================================================")
    configstp["token"] = "NotSet"
    configstp["prefix"] = "NotSet"
    while configstp["token"] == "NotSet":
        configstp["token"] = input("Enter your token without quotes: ")
        if configstp["token"] == "":
            print("You didn't enter anything :/")
            configstp["token"] = "NotSet"
            print("")
    print("")
    while configstp["prefix"] == "NotSet":
        configstp["prefix"] = input("Now enter the command prefix: ")
        if configstp["prefix"] == "":
            print("You didn't enter anything :/")
            configstp["prefix"] = "NotSet"
            print("")
    with open('config.json', encoding='utf-8', mode="w") as n:
        dump(configstp, n, sort_keys=True, indent=4)
    restart()

try: #import the config RTB style
    import json
    from json import dump
    with open('config.json', 'r') as handle:
        config = json.load(handle)
        token = config['token']
        prefix = config['prefix']
except Exception as e:
    if type(e) is FileNotFoundError:
        configsetup()
    else:
        print("Config could not be read")
        print("Make sure it is valid")
        print("Error was : " + str(e))
bot = commands.Bot(command_prefix=config['prefix'], description='''Amadeus Selfbot by Mattlau04''', self_bot=True)

@bot.event
async def on_ready():
    try:
        print("Welcome to Amadeus, " + bot.user.name + "!")
    except Exception:
        print("Welcome to Amadeus!")
    try:
        print("Prefix is " + str(config['prefix']))
    except Exception:
        pass

@bot.command()
async def reload(ctx):
    '''
    Reload Amadeus
    '''
    if ctx.message.author.id == bot.user.id:
        await ctx.send("`Reloading...`", delete_after=3)
        restart()

@bot.command()
async def ping(ctx):
    '''
    Pong! Get the bot latency with this command.
    '''

    latency = bot.latency
    await ctx.send("Pong! `" + str(int(latency * 100)) + "ms`")

@bot.command()
async def prefix(ctx, content:str):
    '''
    Changes Amadeus prefix
    '''
    newprefix = str(content)
    configstp = {}
    configstp["token"] = config["token"]
    configstp["prefix"] = newprefix
    with open('config.json', encoding='utf-8', mode="w") as n:
        dump(configstp, n, sort_keys=True, indent=4)
    await ctx.send("New prefix is `" + newprefix + "`!")
    restart()

@prefix.error
async def prefix_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument: `New prefix`", delete_after=5)
    else:
        print(error)

try:
    bot.run(token, bot=False)
except Exception as t:
        config["token"] = "NotSet"
        while config["token"] == "NotSet":
            config["token"] = input("Your token is invalid, please enter a valid one: ")
            if config["token"] == "":
                print("")
                print("You didn't enter anything :/")
                config["token"] = "NotSet"
        configstp = {}
        configstp["token"] = config["token"]
        configstp["prefix"] = prefix
        with open('config.json', encoding='utf-8', mode="w") as n:
            dump(configstp, n, sort_keys=True, indent=4)
        restart()
