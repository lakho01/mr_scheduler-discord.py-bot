from email.mime import image
from turtle import back, title
from discord.ext import commands
import discord
from discord import app_commands
import interactions
from datetime import date
from discord.ui import Button, View


bot = interactions.Client(
    token=""
)

#----------------------------Start of CWs------------------------------------------ 

Week1S = ("COMP23111 SWE1 Basic Git IndCwk1")
Week1F = ("")

Week2S = ("COMP21111 L&M Propositional Logic")
Week2F = ("")

Week3S = ("COMP21111 L&M Satisfiability \nCOMP23111 SWE1 Conflicts in Git IndCwk2")
Week3F = ("")

Week4S = ("COMP21111 L&M Propositional Formalisations \nCOMP26020 PLP Lab1 Matrix Multiplication in C \nCOMP22111 PM Lab1 ALU \nCOMP23111 DS Database Design")
Week4F = ("")

Week5S = ("COMP21111 L&M DPLL/Random Formulas \nCOMP26120 A&DS Recursive Complexity \nCOMP23311 SWE1 Fixing Bugs TeamCwk1")
Week5F = ("")

Week6S = ("COMP24011 AI Games")
Week6F = ("")

Week7S = ("COMP21111 L&M Randomized Algorithms/Tableaux \nCOMP26020 PLP Lab2 Library Management in C++")
Week7F = ("")

Week8S = ("COMP21111 L&M BDT/BDDs/OBDDs")
Week8F = ("")

Week9S = ("COMP21111 L&M QBF Basics \nCOMP26120 A&DS Spell Checking Data Structures \nCOMP22111 PM Lab3 FSM")
Week9F = ("")

Week10S = ("COMP21111 L&M QBF Algorithms \nCOMP23111 DS Advanced Databases \nCOMP23311 SWE1 Adding Features TeamCwk2")
Week10F = ("")

Week11S = ("COMP21111 L&M PLDF / State Transition Systems \nCOMP26020 PLP Haskell \nCOMP24011 AI SLAM")
Week11F = ("")

Week12S = ("COMP21111 L&M LTL \nCOMP22111 PM Control Implementation \nCOMP22111 PM Signal Using Charts")
Week12F = ("")
#----------------------------------------End of stupid section------------------------------------------
course_abb = "SWE1: Software Engineering 1 \nL&M: Logic & Modelling \nPLP: Programming Languages & Paradigms \nA&DS: Algorithms & Data Structures \nPM: Processor Microarchitecture \nDS: Database Systems \nAI: Introduction to AI"


Dates = {
    1 : "26 September - 30 September",
    2 : "03 October - 07 October",
    3 : "10 October - 14 October",
    4 : "17 October - 21 October",
    5 : "24 October - 28 October",
    6 : "31 October - 4 November",
    7 : "07 November - 11 November",
    8 : "14 November - 18 November",
    9 : "21 November - 25 November",
    10 : "28 November - 02 December",
    11 : "05 December - 09 December",
    12 : "12 December - 16 December"
}

Summatives = {
    1 : "No tasks",
    2 : "COMP21111 L&M Propositional Logic \nCOMP23111 SWE1 Basic Git IndCwk1",
    3 : "COMP21111 L&M Satisfiability",
    4 : "COMP21111 L&M Propositional Formalisations \nCOMP23111 SWE1 Conflicts in Git IndCwk2 \nCOMP26020 PLP Lab1 Matrix Multiplication in C \nCOMP22111 PM Lab1 ALU \nCOMP23111 DS Database Design",
    5 : "COMP21111 L&M DPLL/Random Formulas \nCOMP26120 A&DS Recursive Complexity \nCOMP23311 SWE1 Fixing Bugs TeamCwk1",
    6 : "COMP24011 AI Games",
    7 : "COMP21111 L&M Randomized Algorithms/Tableaux",
    8 : "COMP21111 L&M BDT/BDDs/OBDDs",
    9 : "COMP21111 L&M QBF Basics \nCOMP22111 PM Lab3 FSM",
    10 : "COMP21111 L&M QBF Algorithms \nCOMP23111 DS Implementation \nCOMP24011 AI Fuzzy Logic \nCOMP26020 PLP Lab2 C++",
    11 : "COMP21111 L&M PLDF / State Transition Systems \nCOMP26120 A&DS Spell Checking Data Structures \nCOMP23311 SWE1 Adding Features TeamCwk2",
    12 : "COMP21111 L&M LTL \nCOMP22111 PM Control Implementation \nCOMP22111 PM Signal Using Charts \nCOMP24011 AI SLAM"
}

Formatives = {
    1 : "No tasks",
    2 : "COMP26120 A&DS Analysing Algorithms",
    3 : "COMP26120 A&DS Introducing Complexity Analysis",
    4 : "COMP26120 A&DS Spellchecking 1",
    5 : "No tasks",
    6 : "No tasks",
    7 : "No tasks",
    8 : "COMP26120 A&DS Spellchecking 2",
    9 : "No tasks",
    10 : "No tasks",
    11 : "No tasks",
    12 : "COMP26120 A&DS Priority Queues"
}


#----------------------------End of CWs--------------------------------------

my_id = "<@467264405097283594>"
dan_id = "<@455501686023389186>"
hsdg_id = "<@325213623091986434>"
help_desc = "Note: The bot is currently being developed, any suggestions please DM: "
comb_ali_dan = my_id +"\n" + dan_id
data_link = "https://docs.google.com/spreadsheets/d/11XvSfBHq-kSYZquztFrkjaJJpn6OxDu1uPAkBn-Cie0/edit#gid=1202261217"

data_page = interactions.Button(
    style=interactions.ButtonStyle.LINK,
    label="Data From",
    url = data_link,
    disabled = False
)

@bot.command(
    name = "help",
    description = "View help"
)

async def help(ctx: interactions.CommandContext):
    embeds_help = interactions.Embed(
        title="Mr. Scheduler v2.0",
        description=help_desc+str(my_id)+" or "+str(dan_id),
        color=0x00ff00
        )
    embeds_help.add_field(name="Developed by", value=comb_ali_dan, inline=False)
    embeds_help.add_field(name="Tested by", value=hsdg_id, inline=False)
    embeds_help.add_field(name="Course Abbreviations", value=course_abb, inline=False)
    await ctx.send(embeds = embeds_help, components = data_page)

global WEEK_NUM


@bot.command(
    name="week_choose",
    description="Choose a week number",
    options = [
        interactions.Option(
            name="week_number",
            description="Choose a week number from 1 - 12",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
    ],
)
async def week_choose(ctx: interactions.CommandContext, week_number: int):
    # global msg
    if (week_number>12) or (week_number<1):
        await ctx.send(":x: Choose between 1 - 12")
    else:

        global WEEK_NUM
        WEEK_NUM = week_number
        embeds = interactions.Embed(
        title=f"Deadlines for Week {week_number}",
        description=Dates[week_number],
        color=0x00ff00
        )
        embeds.add_field(name="Summatives:", value=Summatives[week_number], inline=False)
        embeds.add_field(name="Formatives:", value=Formatives[week_number], inline=False)
        if (week_number == 6):
            embeds.title = (embeds.title+"\nReading Week")
            embeds.set_thumbnail(url = "https://i.pinimg.com/originals/66/8a/8c/668a8cccacc792924fa588b4adca8f68.gif")
        await ctx.send(embeds = embeds)




    @bot.component("next")
    async def button_response(ctx):
        global WEEK_NUM
        forward = WEEK_NUM
        WEEK_NUM += 1
        forward = forward + 1
        embeds1 = interactions.Embed(
        title=f"Deadlines for Week {forward}",
        description=Dates[forward],
        color=0x00ff00
        )
        embeds1.add_field(name="Summatives:", value=Summatives[forward], inline=False)
        if (forward == 6):
            embeds1.title = (embeds1.title+"\nReading Week")
            embeds1.set_thumbnail(url = "https://i.pinimg.com/originals/66/8a/8c/668a8cccacc792924fa588b4adca8f68.gif")
        await ctx.send(embeds = embeds1, ephemeral=False)

    

    @bot.component("back")
    async def button_response(ctx):
        # await msg.delete()
        backward = WEEK_NUM
        backward = backward - 1
        embeds0 = interactions.Embed(
        title=f"Deadlines for Week {backward}",
        description=Dates[backward],
        color=0x00ff00
        )
        embeds0.add_field(name="Summatives:", value=Summatives[backward], inline=False)
        if (backward == 6):
            embeds0.title = (embeds0.title+"\nReading Week")
            embeds0.set_thumbnail(url = "https://i.pinimg.com/originals/66/8a/8c/668a8cccacc792924fa588b4adca8f68.gif")
        await ctx.send(embeds = embeds0, ephemeral=False)


bot.start()

#---------------------------------------------End of code----------------------------------------------------
