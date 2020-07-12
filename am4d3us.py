import discord
import random
from discord.ext import commands
prefix = "2"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
   activity = discord.Game(name="with a microwave")
   await bot.change_presence(status=discord.Status.online, activity=activity)
   print('henlo')
      

@bot.command()
async def banana(ctx):
   await ctx.send("Who would eat a pervert's banana?")

@bot.command()
async def cel_17(ctx):
      await ctx.send('Something must be wrong for you to use my actual name')

@bot.command()
async def assistant(ctx):
    await ctx.send('Something must be wrong for you to use my actual name')

@bot.command()
async def kurisutina(ctx):
    await ctx.send('Say it right, Pervert {}' .format(ctx.message.author.mention))

@bot.command()
async def christina(ctx):
    await ctx.send('Say it right, Pervert {}' .format(ctx.message.author.mention))

@bot.command()
async def kurisu(ctx):
    await ctx.send('How can i help you :) ? {}' .format(ctx.message.author.mention))


@bot.command()
async def blush(ctx):
    imageURL = "https://thumbs.gfycat.com/FaintMadBallpython-small.gif"
    embed = discord.Embed()
    embed.set_image(url=imageURL)
    await ctx.send('b-baka', embed = embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 50):
   await ctx.channel.purge(limit = amount)

@bot.command()
async def say(ctx, *, arg):
   await ctx.send(arg)

@bot.command()
async def hello(ctx):
    await ctx.send('hewwo {}'.format(ctx.message.author.mention))

@bot.command()
async def hi(ctx):
    await ctx.send('Hello {}'.format(ctx.message.author.mention))
    
@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))

@bot.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
   responses = ['Most likely.',
    'Without a doubt.',
    'Yes.',
    'As i see it ,yes.',
    'My reply is no.',
    'My reply is yes.',
   'Did Okabe send you to ask this stupid question?',
    'A-are you stupid? of course the answer is no.',
    'Ask again later, baka...',
    "Don't count on it. ",
    'Very doubtful.',
    'That is a dumb question.',
    'The answer is no and WHO ATE MY PUDDING?',
    "I'm not gonna answer that.",
    'Yes - definitely.',
    'No, no, no and no.']
   await ctx.send(f'{random.choice(responses)}')

@bot.command()
async def worldline(ctx):
   world_lines = ['0.571082α',
    '0.571046α',
    '0.571024α',
    '0.571015α',
    '0.523307α',
    '0.456914α',
    '1.143688β',
    '1.130426β',
    '1.130238β',
    '1.130205β ',
    '1.382733β',
    '1.129848β',
    '1.097302β ',
    '1.123581β ',
    '1.064750β ',
    '1.053649β ',
    'STEINS;GATE 1.048596',
    '2.615074γ',
    '3.019430δ ']
   await ctx.send(f'{random.choice(world_lines)}')

kurisu = ['https://media3.giphy.com/media/9cZQnwdzUXTDG/giphy.gif',
 'https://media1.giphy.com/media/mHDgjwPbOAuli/giphy.gif',
 'https://thumbs.gfycat.com/FaintMadBallpython-small.gif',
 'https://media2.giphy.com/media/VBc6l3CqQonqo/giphy.gif',
 'https://thumbs.gfycat.com/ScrawnyExcitableBufeo-max-1mb.gif',
 'https://i.pinimg.com/originals/3b/1c/71/3b1c710655fdf053a7080d59313bfd72.gif',
 'https://media1.giphy.com/media/sLSIcrMMm5VL2/giphy.gif',
 'https://media2.giphy.com/media/m3m60GHQjobtu/source.gif',
 'https://66.media.tumblr.com/4145c056e75249372c75372ffcc580a8/tumblr_p7rdzvztkd1v1hotuo1_500.gif',
 'https://66.media.tumblr.com/11e2b2b98cfc7f652113b3740ccfd8e5/tumblr_oo09wciJ6r1roj09io2_250.gif']

@bot.command()
async def gif(ctx):
   embed = discord.Embed()
   embed.set_image(url=random.choice(kurisu))
   await ctx.send(embed = embed)

pic = ['https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/69564059_587398298460009_3446557959067271168_n.jpg?_nc_cat=105&_nc_oc=AQnE4-BroFoqqZGzur6hPvfvgpcbF0XMNAja1agY5oCORaJOpRtFVSRjkbeW_U5cfOc&_nc_ht=scontent.fuln1-1.fna&oh=c22597d9d478daf1d1b5fbebd3e8f93c&oe=5DCCAA4E',
'https://scontent.fuln1-2.fna.fbcdn.net/v/t1.0-9/68936050_587263578473481_5574305012571439104_n.jpg?_nc_cat=104&_nc_oc=AQkh1eZoDb_nolU3F6q3wHPA6gMWECalwfV1N3Y8WHGJRudIRdQnEhw93UjFjtzFarw&_nc_ht=scontent.fuln1-2.fna&oh=94f7dec5f76df1dfc47527dcec14e55b&oe=5DC8BA23',
'https://scontent.fuln1-2.fna.fbcdn.net/v/t1.0-9/68741826_586652271867945_4925398667474501632_n.jpg?_nc_cat=110&_nc_oc=AQnYFkMXv6ybOkE5DtZqsRMqMZPEHGKrVaQgLOLh2rIa2TdLU9ZqZSBiRF39ruqUvuo&_nc_ht=scontent.fuln1-2.fna&oh=21d52423945eef08decdc981bf8b3795&oe=5DDC3ED7',
'https://scontent.fuln1-2.fna.fbcdn.net/v/t1.0-9/68684553_585229992010173_2382534099869892608_n.jpg?_nc_cat=108&_nc_oc=AQk9etpEPIv-I_LcYnjgO3IlKjBwZwBEYS6GVolbWCX0bHmsLyy-UffSphTYsH6L-5A&_nc_ht=scontent.fuln1-2.fna&oh=cc969c7ad3a4abab618f453bade316d2&oe=5E0B23B5',
'https://scontent.fuln1-2.fna.fbcdn.net/v/t1.0-9/67976102_584109612122211_5230673982117642240_n.jpg?_nc_cat=100&_nc_oc=AQnyxf20cMWM3BfBVtUM_SS5pLeeMuHoTXoc9VzNdO3xZYULex4ZozToR-6TLmghtEs&_nc_ht=scontent.fuln1-2.fna&oh=554113a331cbc2dec877dcac78cd75ff&oe=5DC7D407',
'https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/69499620_583828432150329_4410266483335102464_n.jpg?_nc_cat=102&_nc_oc=AQnkbzM9fRTK_9OZO2g5JEolENO66lApSowFPfOfzN9FmOSFL-t4GsADpB2vk8Dq_Zc&_nc_ht=scontent.fuln1-1.fna&oh=4c51989dbcc1ee4e5f33de175a147ce3&oe=5DD56038',
'https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/67953146_583282078871631_3272813015681990656_n.jpg?_nc_cat=103&_nc_oc=AQmHlehjHy5Oj_Dyu2U5-UMWQS3AG-F5kOaJiH_zAfQK0zQudJ5Ou4lj4k08GuxiwRQ&_nc_ht=scontent.fuln1-1.fna&oh=f615c0b7beb1b971e452e93da4aa6d14&oe=5DD39F30',
'https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/67834239_582619158937923_1437080191632408576_n.jpg?_nc_cat=109&_nc_oc=AQklc8YZOvU-zsk8xhNZIILcKqIwl_Qgg8VO6SXjXKY3nlKOfLY9Zh6AQlJDfAdEU4k&_nc_ht=scontent.fuln1-1.fna&oh=7335d9e309fe59106515f938504a818e&oe=5E0FA96B',
'https://scontent.fuln1-2.fna.fbcdn.net/v/t1.0-9/68490513_582326062300566_5030618339660005376_n.jpg?_nc_cat=106&_nc_oc=AQkNiHvdqfiry57GEH-VNpB3kbSmQlErhjXXgMVGlKo2Puq7EeoGm8CtaYfaMsuG3c8&_nc_ht=scontent.fuln1-2.fna&oh=1df86aeda5991cf74f0130ac8712ed94&oe=5DC9CCF2',
'https://scontent.fuln1-2.fna.fbcdn.net/v/t1.0-9/67957072_582087908991048_903014855349370880_o.jpg?_nc_cat=100&_nc_oc=AQnOG_63bpfBTbYxeyRnUxG43JsMqvwAozZieg0nP3UHoLvA7MclVrGbOd0-xtRc0UM&_nc_ht=scontent.fuln1-2.fna&oh=1ae79be00040eac9c9fd7a77eaf632f9&oe=5DD5C2CF',
'https://scontent.fuln1-2.fna.fbcdn.net/v/t1.0-9/68832641_581841119015727_2888929139413221376_n.jpg?_nc_cat=107&_nc_oc=AQm_VapR1Yc2AAGRTe_1iaxbuQYhQvmbMieICK47N5EiAfJBHW8I2Rll4tzOsGI7Ev8&_nc_ht=scontent.fuln1-2.fna&oh=70d44e923230d7d492d7e311ac275779&oe=5DD8407B',
'https://scontent.fuln1-2.fna.fbcdn.net/v/t1.0-9/67886670_581316775734828_7332628305310384128_n.jpg?_nc_cat=104&_nc_oc=AQkuTsepMbIFbBzPmAdILOwUEfngPThG_tmncGIlhBN4Ru3XKBEYOD5tH3_i_hqYaao&_nc_ht=scontent.fuln1-2.fna&oh=b18e7b72a9d2ebfb7c29e8d47a35278c&oe=5DCDBE88',
'https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/67556022_571723740027465_3604412266486693888_n.jpg?_nc_cat=102&_nc_oc=AQk3fLZMn1_3RpLBUAFPZcxL34XChqvqa-wulx730Nu1dG70gIXaceQwrta5qMSuw08&_nc_ht=scontent.fuln1-1.fna&oh=7e482379c40fffc99d9f94301325df60&oe=5DD1A7C3',
'https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/67782541_575839912949181_2861395371093917696_n.png?_nc_cat=102&_nc_oc=AQmR7HomsuzS6w7XU23UtZm70Mjsbi8c-YvAWibZ0WAh6HrPivtq6NGfxHKX2oQ6gNU&_nc_ht=scontent.fuln1-1.fna&oh=9b28520246baf93a1f53fcd87940ad7e&oe=5DC99B9A',
'https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/67909814_575757009624138_7891107494129303552_n.png?_nc_cat=109&_nc_oc=AQkPwvMb75BBU5WGa9YZJbLezv1necv3jH36v3Ai7FyiaFWMzElYZYDictPt0MfA6-E&_nc_ht=scontent.fuln1-1.fna&oh=9ff1aef5548ac5b5ce1baef8ef080d0d&oe=5DC9EF47',
'https://scontent.fuln1-2.fna.fbcdn.net/v/t1.0-9/66857199_569870583546114_3439580746040213504_n.png?_nc_cat=104&_nc_oc=AQmeGKMttsJrlA2zDG-wofAIX1uCJ4IFIDdXW5PvpTEoMWKU-P8fO-7aJCuX9gNgK0A&_nc_ht=scontent.fuln1-2.fna&oh=dd30ad819eb8f9ba94486a8ad70c3a95&oe=5E14EDA0',
'https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/65901144_559204581279381_1540084704370229248_n.jpg?_nc_cat=109&_nc_oc=AQnvimLQvPD1JuHuzcmNueQ-Hey2JOiPeb3BybMAizubASBvF8xFSjKlYvvg4eZBuAo&_nc_ht=scontent.fuln1-1.fna&oh=579ffb6c9f94c734956ce05e1866c63b&oe=5E0C641D',
'https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/65426268_557137081486131_8778689582796374016_n.jpg?_nc_cat=111&_nc_oc=AQkvCwu1C6tWpuDi1cOgONff0eGgeoYE1XfAjEuXa9R7vPaAsw5CS7J02UsDGXdHXBI&_nc_ht=scontent.fuln1-1.fna&oh=3c4d2df391e831d278616a2caf85573e&oe=5DDE0083',
'https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/65931520_2275014525910708_8858499545558941696_n.jpg?_nc_cat=101&_nc_oc=AQmTWOT1cAImdGgqckUFRiFGX06kZ9nypMCGTpe0z-S0nnt3wylhrGJOuJyv4NoSqSA&_nc_ht=scontent.fuln1-1.fna&oh=050903aebe25cd642ca55a35e296158e&oe=5DCC9EC7',
'https://scontent.fuln1-1.fna.fbcdn.net/v/t1.0-9/64875037_551482812051558_7268595492592812032_n.png?_nc_cat=101&_nc_oc=AQmUOmvkJIhHVAlS8Hn7f7OP_MpdYU6MhFb0B4vPfQ3WXq_KiKsSGsm3DyIiXIQplzo&_nc_ht=scontent.fuln1-1.fna&oh=86140d96a02c4e2a2a453405f160e0bb&oe=5E15358B']

@bot.command()
async def reaction_pic(ctx):
   embed = discord.Embed()
   embed.set_image(url=random.choice(pic))
   await ctx.send(embed = embed)

@bot.event
async def on_message(message):
   author = message.author
   content = message.content
   print('{}: {}' .format(author, content))
   await bot.process_commands(message)

@bot.event
async def on_message(message):
  channel = message.channel
  if message.content.startswith('uwu' ):
      await message.channel.send ('OWO')
  await bot.process_commands(message)

       


bot.run('NjEzNjcyMTYzNTAwNzUyOTA3.XV1Q1A.lZtmb7Jt-cUhXniKA9N_A-cxpko')
