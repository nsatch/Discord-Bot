# Import the commands module from discord.py to use easy functions
# to make a command bot
from discord.ext import commands
import random

# Set the prefix character to signal a command to the bot as '!'
bot = commands.Bot(command_prefix = '!')

# Define a new command for the bot
@bot.command(name = "idea", help = "Get a side project idea")
# async and await basically let this func run in the background and 
# lets the program do other things while it runs and comes back to it
# later. More details in async_await_exp.txt
async def idea(ctx):
    await ctx.send("Ideas are hard")
    await ctx.send("Worry not, I think you should...")

    topics = ['chat bot', 'cli', 'game', 'web bot', 'browser extention', 'api', 'web interface']
    areas = ['note taking', 'social life', 'physical fitness', 'mental health', 'pet care']
    lang = ['C++', 'Python', 'Scratch', 'JavaScript']

    # {} is an f-string which converts the value inside the {} to a string to be printed with the rest of the string
    idea = f'Create a new {random.choice(topics)} that helps with {random.choice(areas)} in {random.choice(lang)}! :slight_smile:'
    await ctx.send(idea)

# Calculator command that does addition, subtraction, multiplication, and division between two numbers
@bot.command(name = "calc", help = "Perform an operation between two numbers supporting +, -, *, /, ^. (Syntax is x (op) y)")
#async def calc(ctx, x, fn, y): -> Old function header which required types to be define like so underneats
    #x = float(x)            # Define x & y as floats
    #y = float(y)
async def calc(ctx, x: float, fn: str, y:float):
    
    # Different cases for the four different functions
    if fn == '+':
        await ctx.send(x + y)
    # Python uses "elif" instead of "else if"
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    elif fn == '**' or '^':
        await ctx.send(x ** y)
    else:
        await ctx.send("We only support five function operations")



# Use token to access and update the bot

# with statement in python assures proper acquistion and closure of the 
# desired data (so note no file.close used for BOT_TOKEN.txt)
# it is also a more compact way of writing the code (check https://www.geeksforgeeks.org/with-statement-in-python/
# for details)
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()  # Obtain token for bot to modify that bot
    print("Token file read")   # Print to console that the token was read successfully
    print("Press Ctrl + C to shut down the bot")
    bot.run(TOKEN)