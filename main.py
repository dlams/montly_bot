import discord
from adapters import get_discord_token
from service_layer.services import render

TOKEN = get_discord_token()


bot = discord.Bot()

@bot.slash_command()
async def daily_check(ctx, user):
    embed = render()
    await ctx.respond("오늘의 두부 상자를 요청하셨습니다.", embed=embed) # Send the embed with some text

bot.run(TOKEN)