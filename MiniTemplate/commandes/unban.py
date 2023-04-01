from discord import *
import json

class unban_class:
    def commandes(client, tree):
        with open("data/client.json") as file:
            client_data = json.load(file)

        @app_commands.default_permissions(ban_members=True)
        @app_commands.describe(member="Membre à unban.")
        @app_commands.command(description="Ban un membre.")
        async def unban(interaction : Interaction, member : str):

            guild = interaction.guild
            banned_users = [entry async for entry in guild.bans(limit=2000)]
            for user_entry in banned_users:
                user = user_entry.user
                if str(user) == member:
                    await guild.unban(user)
                    embed = Embed(description=f"{member} vient d'être unban par {interaction.user.mention}")
                    embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)    
                    await interaction.response.send_message(embed=embed)
                    return
            await interaction.response.send_message(f"Il semble que aucune personne bannie n'a comme nom : `{member}` !", ephemeral=True)
        
        tree.add_command(unban)