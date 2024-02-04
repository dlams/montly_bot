import discord

class InvalidUser(Exception):
    pass


def render():
    """
    """
#     # await ctx.respond("hello.")
    embed = discord.Embed(
        title=f"오늘의 두부 상자",
        description="""
        - - - - - - - -

 🟨ㅤ 🟨ㅤ 🟨ㅤ ⬜ㅤ 🟨ㅤ 📙ㅤ ⬜ㅤ 

 ⬜ㅤ ⬜ㅤ ⬜ㅤ ⬜ㅤ ⬜ㅤ ⬜ㅤ 🔖ㅤ 
        """,
        color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    )

    embed.set_footer(text="2/14") # footers can have icons too
    embed.set_author(name="한달이 - 두부 상자", icon_url="https://cdn.discordapp.com/avatars/1201900162730164376/024b4f0b4b36124e0ef2e0a4c87f0b1b.webp?size=100")
    # embed.set_thumbnail(url="https://altools.co.kr/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fimg_feature_alsee_1.60428533.png&w=3840&q=75")
    # embed.set_image(url="https://altools.co.kr/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fimg_feature_alsee_1.60428533.png&w=3840&q=75")
 
#     await ctx.respond("오늘의 두부 상자를 요청하셨습니다.", embed=embed) # Send the embed with some text

    return embed