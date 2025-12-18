import discord
from discord.ext import commands
from discord import app_commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

  	# cog 裡面的 decorator 改成這個
    @app_commands.command(name="clear", description="指定要刪除幾則訊息")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def delete_msg(self, interaction: discord.Interaction, amount: int):
       if amount < 1:
           await interaction.response.send_message("重新輸入數量", ephemeral=True)
           return

       await interaction.response.defer(ephemeral=True)
       deleted = await interaction.channel.purge(limit=amount)
       await interaction.followup.send(f"已刪除 {len(deleted)} 則訊息", ephemeral=True)

    
async def setup(bot):
  	await bot.add_cog(moderation(bot))