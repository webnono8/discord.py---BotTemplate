""" Importations """
from discord import *


""" Class """
class test_def:
    """ Def pour Import """
    def commande(client, tree):
        @app_commands.command(description="Description de la commandes.") # Defini la fonction async def test 
        async def test(interaction : Interaction): # Creation de la commande Test avec definition de l'interaction
            await interaction.response.send_message("Test") # repond a l'interaction de la commande par test

        tree.add_command(test) # ajoute la commande au slash