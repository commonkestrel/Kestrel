import time
import discord
from discord.ext import commands

global coordlist
coordlist = []

client = commands.Bot(command_prefix='\\')
client.remove_command('help')

@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="for \\\'s")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Logged in as {0.user}'.format(client))



@client.command()
async def summon(ctx):
    await ctx.send("YOU DARE SUMMON ME")


@client.command()
async def test(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'The Latency is {round(client.latency * 1000)} ms')
    time.sleep(3)
    await ctx.send(f'The Latency is {round(client.latency * 1000)} ms')
    time.sleep(3)
    await ctx.send(f'The Latency is {round(client.latency * 1000)} ms')

@client.command(pass_context=True)
async def dm(ctx):
    author = ctx.message.author
    await author.send(f'UwU hey sexy')
    await ctx.send('Successful')



@client.command()
async def purge(ctx):
        def check(msg):
            return msg.content and msg.channel == ctx.channel
        await ctx.send('How many messages')
        message = await client.wait_for("message", check=check)
        messageammount = message.content
        purgeammount = int(messageammount) + 3
        if int(messageammount) < 51 and int(messageammount) > 0:
            await ctx.channel.purge(limit=purgeammount)
            await ctx.send("Messages Cleared")
            time.sleep(3)
            await ctx.channel.purge(limit=1)
            print('Purged')
        else:
            await ctx.send('Invavlid number! Must be between 1-50')

@client.command()
async def reply(ctx):
        await ctx.reply('Fuck you')




@client.command(aliases=['uwu', 'UwU', 'roleplay'])
async def suck(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('\*purrs and sucks dick UwU\*')


        



@client.command(aliases =['xyz', 'coordinates', 'newcoord', 'coords', 'newxyz', 'newlocation', 'location', 'locationadd'])
async def coord(ctx):
        await ctx.send('Send X coordinate\n(X,y,z)')

        channel = ctx.channel

        def check(ctx):
            def inner(msg):
                return msg.author == ctx.author
                return msg.content and msg.channel == ctx.channel
            return inner

        messagex = await client.wait_for("message", check=check)
        Xcoord = messagex.content

        coordlist.append(Xcoord)

        await ctx.send('Send Y coordinate\n(x,Y,z)')

        messagey = await client.wait_for("message", check=check)
        Ycoord = messagey.content

        coordlist.append(Ycoord)

        await ctx.send('Send Z coordinate\n(x,y,Z)')

        messagez = await client.wait_for("message", check=check)
        Zcoord = messagez.content

        coordlist.append(Zcoord)

        await ctx.send('Location Name')

        messagel = await client.wait_for("message", check=check)
        location = messagel.content

        await ctx.send('Description \(Enter none if no description\)')

        messaged = await client.wait_for("message", check=check)
        description1 = messaged.content


        await ctx.channel.purge(limit=11)

        await ctx.send('Is this in the nether')
        while True:
            await ctx.channel.purge(limit=2)

            messagen = await client.wait_for("message", check=check)
            nethercheck = messagen.content

            Finalcoord = str(
                "(" + coordlist[0] + ", " + coordlist[1] + ", " + coordlist[2] + ")")

            print(coordlist)
            if nethercheck == 'no':
                embed = discord.Embed(
                    title=location,
                    colour=discord.Colour.blue()
                )

                embed.add_field(name='X coordinate', value=Xcoord, inline=True)
                embed.add_field(name='Y coordinate', value=Ycoord, inline=True)
                embed.add_field(name='Z coordinate', value=Zcoord, inline=True)
                embed.add_field(name='᲼᲼᲼᲼᲼᲼᲼᲼Nether Coordinates',
                                value=f'᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼\({round(int(Xcoord) / 8)}, {round(int(Zcoord) / 8)}\)', inline=False)
                if description1 == 'none':
                    print('no description for ' + location)

                else:
                    embed.set_footer(text=description1)

                await ctx.send(embed=embed)
            elif nethercheck == 'yes':
                embed = discord.Embed(
                    title=location,
                    colour=discord.Colour.red()
                )

                embed.add_field(name='X coordinate', value=Xcoord, inline=True)
                embed.add_field(name='Y coordinate', value=Ycoord, inline=True)
                embed.add_field(name='Z coordinate', value=Zcoord, inline=True)
                if description1 == 'none':
                    print('no description for ' + location)

                else:
                    embed.set_footer(text=f'In nether. {description1}')
            else:
                await ctx.send('Invalid answer. Must be yes or no')
        coordlist.clear()

@client.command()
async def testembed(ctx):
    embed = discord.Embed(
            title = 'Test title',
            description = 'Test description',
            colour = discord.Colour.blue()
        )

    embed.set_footer(text='test footer')
    embed.add_field(name='Field Name', value='Field Value', inline=True)
    await ctx.send(embed=embed)
        


client.run('ODY0OTgxNDM0OTgwNzYxNjcx.YO9WvA.UPzl-ZnUBm3pQhrfbBAkp45DDMU')
