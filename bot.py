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

@bot.command(name = "tictactoe", help = "Play a game of tic tac toe")
async def tictactoe(ctx):
    await ctx.send("`   1     2    3  ")
    await ctx.send("a |    |    |    |")
    await ctx.send("b |    |    |    |")
    await ctx.send("c |    |    |    |")

    gameOngoing = 1          #Bool to check if tictactoe game is ongoing
    while (gameOngoing):     #Continue the game if there is no winner and still valid moves
        msg = await bot.wait_for("message") 
        if msg.content == "1a":
            await ctx.send("`   1     2    3  ")
            await ctx.send("a | X |    |    |")
            await ctx.send("b |    |    |    |")
            await ctx.send("c |    |    |    |")
            gameOngoing = 0
        else:
            await ctx.send("Did not type 1a")

@bot.command(name = "q", help = "Display a quote from someone")
async def q(ctx, name: str):
    name = name.lower()
    nameFound = False                      # Bool flag for if name already exist in names.txt (i.e if we have quotes for this name)
    nameFile = open("names.txt")
    for line in nameFile:                  # Iterate through each line in the names.txt
        if (line == name + "\n"):          # If a line has the name of the person we are trying to get a quote from
            nameFound = True               # Set the bool flag to true for next if statement
            break
    nameFile.close                         # Close the name file since we no longer need to see its contents

    if (nameFound == False):           # If the name does not exists, there is no quote file for this name yet and we need to write that we are making a new file for it
        await ctx.send("There are no quotes for " + name)  # Tell the user we do not have this name stored therefore no quotes from them
    else:
        quoteFolder = "quotes/"            # Set variable for quotes folder directory to store all the quote text files in one folder for organization
        quoteFile = open(quoteFolder + name + ".txt")  # Open the specific quote file for the person we want a quote from
        quoteList = []                                 # Create an empty list to push all their quotes into
        for line in quoteFile:                         # Iterate thru each line of their quote file
            quoteList.append(line)                     # Push each line of quotes into the quote list
        await ctx.send(":mega: " + random.choice(quoteList))  # Choose a random quote from the list we just made and have the bot send it to the server

# ^^^^^^ COMMENTS ON THE EFFICENCY OF QUOTE SEARCHING THRU THE ABOVE METHOD ^^^^^^^
# Technically speaking iterating through all the lines and storing them into a list then randomly selecting one element has horrible run time and memory consumption
# but this is all just small text which is small in memory and the lists won't be very long given how many people will use the bot in my context, so this method is
# fine for that purpose. 
# If I was truly concerned about runtime, I would reserve the first line for storing how many lines are in the file as an int, then only read that line and generate 
# a random number between 1 and that number. I would then return the quote from the random line number generated. Going to that specific line though without iteration
# is not something I am sure is possible though with Pythons tools (I really haven't investigated this implementation at all). At the very least, you could iterate thru
# the list this way without storing each read line in a list like I do above which would at least reduce memory consumption (again like what a few kb though?)

@bot.command(name = "qa", help = "Add a new quote")
async def qa(ctx, *nameQuote):
    nameQuote = ' '.join(nameQuote)    # Combine all the words in the nameQuote tuple into one giant element separated by white spaces
    split = nameQuote.split(' ', 1)    # Split the string by white space, but only do once (so we have [name, quote])
    name = split[0].lower()            # Get first word of string and store as name to save quote under
    quote = split[1]                   # Store all of string minus first word as quote to save

    nameFile = open("names.txt", "r+") # Open names.txt to read names. r+ flag = open for reading and writing
    nameFound = False                  # Set boolean flag to know if name already exists and has a quotes file
    for line in nameFile:              # Iterate through each line in the names.txt
        if (line == name + "\n"):        # If any line already contains the name we are trying to add we do not need to make a new quote file and can instead edit the existing one
            nameFound = True
            break
    if (nameFound == False):           # If the name does not exists, there is no quote file for this name yet and we need to write that we are making a new file for it
        nameFile.write(name + "\n")    # Write the new name in the names.txt so we record that a quote file will exist for this name
        nameFile.close                 # Close the name file

    quoteFolder = "quotes/"            # Set variable for quotes folder directory to store all the quote text files in one folder for organization
    if (nameFound == False):                                  # If the name isn't found, no file exists yet, so the a+ flag needs to be used to make a new file and we don't need to worry about iterating through it since it has no quotes yet
        quoteFile = open(quoteFolder + name + ".txt", "a+")   # Open a new quote file titled "name".txt. The a+ flag means it is readable and writeable, and the file will be created if it doesn't exist
    else:                                                     # Otherwise if the new exists, we don't need to make the file but need to iterate thru it so see if quote exists so use r+ flag
        quoteFile = open(quoteFolder + name + ".txt", "r+")   # Open a new quote file titled "name".txt. The r+ flag means it is readable and writeable, but a+ opens at end of file which makes it
                                                              # impossible to iterate through file since we are already at the last line. Need to iterate to check if quote already exists
    quoteFound = False                 # Set boolean flag to check if we find the quote
    for line in quoteFile:             # Iterate through each line in the quote files
        if (line == (quote + "\n")):   # If the quote already exists
            quoteFound = True          # We found the quote
            await ctx.send("Quote already exists! I'm not adding this quote bro you already know I only have like 10 gb free on my HD.") #Tell user quote is not being added
            break                      # End iteration

    if (quoteFound == False):          # If the quote does not exist
        quoteFile.write(quote + "\n")  # Add the quote
        await ctx.send("Quote added for " + name + ": \"" + quote + "\"")  #Tell the user what quote was added and for whome
    
    quoteFile.close                    # Close the quote file

    # Do check to see if quote was added correctly
    # if added correctly print quote added for name with content quote
    # else if there was an error say quote was not added

@bot.command(name = "github", help = "Receive the github link for this bot to see my code and comments")
async def github(ctx):
    githubLink = "https://github.com/nsatch/Discord-Bot"
    await ctx.send(githubLink)

@bot.command(name = "shutdown", help = "Makes the bot go offline")
async def shutdown(ctx):
    bot.close()

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