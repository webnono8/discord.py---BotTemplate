###################################################################################################################################################################################
###################################################################################################################################################################################
############################################################################  main.py for Template  ###############################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################


""" Importations """
from discord import *
import json


""" Client & Intents """
intents = Intents.default()
intents.message_content = True
intents.members = True

client = Client(intents=intents)
tree = app_commands.CommandTree(client)


""" Commandes """

# ---Say---

from commandes.say import say_def
say_def.commande(client, tree)

# ---Kick---

from commandes.kick import kick_class
kick_class.commande(client, tree)

# ---Ban---

from commandes.ban import ban_class
ban_class.commandes(client, tree)

# ---Unban---

from commandes.unban import unban_class
unban_class.commandes(client, tree)

# ---Welcome_Set---

from commandes.welcome_set import welcome_def
welcome_def.commande(client, tree)

# ---Server_Info---

from commandes.server_info import server_info_class
server_info_class.command(client, tree)

""" Events """

# ---Ready---

from event.ready import ready_def
ready_def.ready(client, tree)

# ---Welcome---

from event.welcome import welcome_def
welcome_def.welcome(client, tree)



""" Run """
with open('data/token.json', 'r') as file:
    token = json.load(file)
client.run(token)