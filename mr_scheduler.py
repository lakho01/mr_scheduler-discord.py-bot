import discord
import os

from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print('Bot is running as {0.user}'.format(client))

# This is the section where you put in your weekly assignments
# An example is :
# Week2 = ("Mathematics Sheet 12 due Friday")

Week0 = ("")
Week1 = ("")
Week2 = ("<Redacted>")
Week3 = ("<Redacted>")
Week4 = ("<Redacted>")
Week5 = (
    "<Redacted>")
Week6 = (
    "<Redacted>")
Week7 = (
    "<Redacted>")
Week8 = ("<Redacted>")
WeekAB = ("<Redacted>")
Week9 = ("<Redacted>")
Week10 = (
    "<Redacted>")
Week11 = ("<Redacted>")
Week12 = ("<Redacted>")

# End of section

# For example ("<@8932308402480230>") - include the < and >
owner = "<Enter your discord user id here>"
err_msg = "Send a DM to: " + str(owner)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == ("_help"):
        embedVar = discord.Embed(
            title="Mr Scheduler Help", description="To find out tasks in a week, type $$wk followed by a week number, for example -> $$wk2 ", color=0x00ff00)
        await message.channel.send(embed=embedVar)

    if message.content.startswith("$wk"):  # Change of prefix
        embedVar = discord.Embed(
            title="Prefix has been changed", description="Instead of $wk, it is now $$wk ", color=0x00ff00)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk0') or message.content == ('$$wk00'):
        embedVar = discord.Embed(
            title="Deadlines for Week 0", description="Week 0 runs from 31st Jan to 4th Feb", color=0x00ff00)
        embedVar.add_field(
            name="Tasks:", value="Currently no tasks for Week 0", inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk1') or message.content == ('$$wk01'):
        embedVar = discord.Embed(
            title="Deadlines for Week 1", description="Week 1 runs from 7 Feb to 11 Feb", color=0x00ff00)
        embedVar.add_field(
            name="Tasks:", value="Currently no tasks for Week 1", inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk2') or message.content == ('$$wk02'):
        embedVar = discord.Embed(
            title="Deadlines for Week 2", description="Week 2 runs from 14 Feb to 18 Feb", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week2, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk3') or message.content == ('$$wk03'):
        embedVar = discord.Embed(
            title="Deadlines for Week 3", description="Week 3 runs from 21 Feb to 25 Feb", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week3, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk4') or message.content == ('$$wk04'):
        embedVar = discord.Embed(
            title="Deadlines for Week 4", description="Week 4 runs from 28 Feb to 4 March", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week4, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk5') or message.content == ('$$wk05'):
        embedVar = discord.Embed(
            title="Deadlines for Week 5", description="Week 5 runs from 7 March to 11 March", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week5, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk6') or message.content == ('$$wk06'):
        embedVar = discord.Embed(
            title="Deadlines for Week 6", description="Week 6 runs from 14 March to 18 March", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week6, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk7') or message.content == ('$$wk07'):
        embedVar = discord.Embed(
            title="Deadlines for Week 7", description="Week 7 runs from 21 March to 25 March", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week7, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk8') or message.content == ('$$wk08'):
        embedVar = discord.Embed(
            title="Deadlines for Week 8", description="Week 8 runs from 28 March to 1 April", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week8, inline=False)
        embedVar.add_field(
            name="Upcoming April Break", value="There is one task due next week, type $wkab to find out", inline=False)
        embedVar.add_field(
            name="Caution:", value="Might get april fooled by someone", inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wkab'):
        embedVar = discord.Embed(
            title="Deadlines for Week - April Break", description="Week - April Break runs from 4 April to 7 April", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=WeekAB, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk9') or message.content == ('$$wk09'):
        embedVar = discord.Embed(
            title="Deadlines for Week 9", description="Week 9 runs from 25 April - 29 April", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week9, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk10'):
        embedVar = discord.Embed(
            title="Deadlines for Week 10", description="Week 10 runs from 2 May - 6 May", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week10, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk11'):
        embedVar = discord.Embed(
            title="Deadlines for Week 11", description="Week 11 runs from 9 May - 13 May", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week11, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('$$wk12'):
        embedVar = discord.Embed(
            title="Deadlines for Week 12", description="Week 12 runs from 16 May - 20 May", color=0x00ff00)
        embedVar.add_field(name="Tasks:", value=Week12, inline=False)
        embedVar.add_field(name="Do you see any incorrect data?",
                           value=err_msg, inline=False)
        await message.channel.send(embed=embedVar)
    if message.content == ('$$wk13'):
        embedVar = discord.Embed(
            title="That's all! Goodluck with your exams!", color=0x00ff00)
        embedVar.set_image(
            url="https://media4.giphy.com/media/ZhK8fC14hUxmo/giphy.gif?cid=ecf05e47draeno3afu9jru7nhvjrc5pi88vfkt5cbcua85y4&rid=giphy.gif&ct=g")  # Gif taken from GIPHY that wishes you luck
        await message.channel.send(embed=embedVar)

keep_alive()  # Calls the keep_alive() function from keep_running.py
# Method to get the token that is encrypted in this case
my_secret = os.environ['Token2']
client.run(my_secret)
