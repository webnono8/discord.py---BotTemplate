###################################################################################################################################################################################
###################################################################################################################################################################################
############################################################################  say.py for Template  ################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################


""" Importations """
from discord import *


""" Class """
class say_def:
    """ Def pour Import """
    def commande(client, tree):
        @app_commands.default_permissions(administrator=True)
        @app_commands.command(description="C'est une commande pour envoyer un message.") # Defini la fonction async def test 
        async def say(interaction : Interaction, message : str): # Creation de la commande Test avec definition de l'interaction
            await interaction.channel.send(message)
            await interaction.response.send_message("Message bien envoyer!", ephemeral=True)
        tree.add_command(say)