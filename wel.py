import discord
from discord.ext import commands
import datetime
import keep_alive

intents = discord.Intents.all()



bot=commands.Bot(command_prefix="!??????",intents=intents)

@bot.event
async def on_member_join(member:discord.Member):
    if member.guild.id==916967677392744448:
        wchannel=bot.get_channel(916970240007626832)
        hu=member.guild.members
        ggi=bot.get_channel(916982932218974238)
        em=discord.Embed(title=f'------歡迎來到{member.guild.name}------',
                        description=f'{member.mention}\nღ第{len(hu)}個成員\nღ規則頻道傳送門：{ggi.mention}'
                        ,colour=discord.Color.random())
        em.set_author(name=member.name,icon_url=member.avatar_url)
        em.set_thumbnail(url=member.guild.icon_url)
        em.set_footer(text=(datetime.datetime.now()+datetime.timedelta(hours=8)).strftime('%Y/%m/%d %H:%M:%S'))
        await wchannel.send(embed=em)       

@bot.event
async def on_member_remove(member:discord.Member):
    if member.guild.id==916967677392744448:
        wchannel=bot.get_channel(916970472367882281)
        hu=member.guild.members
        em=discord.Embed(title=f'----{member.name}離開了{member.guild.name}我們歡送他----',description=f'我們歡送他QAQ\n剩餘成員數:{len(hu)}',colour=discord.Color.random())
        em.set_author(name=member.name,icon_url=member.avatar_url)
        em.set_footer(text=(datetime.datetime.now()+datetime.timedelta(hours=8)).strftime('%Y/%m/%d %H:%M:%S'))
        await wchannel.send(embed=em) 

       

if __name__ == '__main__':
	keep_alive.keep_alive()
	bot.run('OTE2OTkwNTk0OTEwNDE2ODk2.YayMCg.QeYVNp4qPmFb6kJnWSHCfddtMj8')        



  