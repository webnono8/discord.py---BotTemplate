from discord import *
import json

class ban_class:
    def commandes(client, tree):
        with open("data/client.json") as file:
            client_data = json.load(file)

        @app_commands.default_permissions(ban_members=True)
        @app_commands.describe(member="Membre à bannir.", raison="Raison du ban")
        @app_commands.command(description="Ban un membre.")
        async def ban(interaction : Interaction, member : Member, raison : str = "Aucune raison."):
            if member == interaction.user:
                await interaction.response.send_message("Vous ne pouvez pas vous ban.", ephemeral=True)
            else:
                embed = Embed(description=f"{member.mention} vient d'être ban par {interaction.user.mention}\n**Raison :** {raison}")
                embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)

                await member.ban(reason=raison)
                await interaction.response.send_message(embed=embed)
        
        tree.add_command(ban)