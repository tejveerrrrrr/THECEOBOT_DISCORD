# Tej - TEJJJJJJJ
# THE CEO - Bot: does some real shit

# right now, all it does is talk to you
# future plans: 
# - music
# - moderation controls
# - ai, such as chatgpt or something else
import discord
from discord.ext import commands
from datetime import timedelta

import os
from dotenv import load_dotenv

TOKEN = os.getenv("DISCORD_TOKEN")

# Create intents object
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.moderation = True  # Enables timeout permissions
bot = commands.Bot(command_prefix="!", intents=intents)


client = discord.Client(intents=intents)

username_to_timeout = ["afg99"]

@client.event
async def on_member_update(before, after):
    if after.display.name in username_to_timeout:
        duration = timedelta(minutes=5)
        print("trying to timeout user")
        try:
            await after.timeout(duration, reason="unlucky, this is RNG")
            print(f"timed out {after.display_name} for 5 minutes")
        except discord.Forbidden:
            print("missing perms")
        except discord.HTTPException:
            print("failed to time out")

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")
 
@client.event
async def on_message(msg):
    print(f"Message received: {msg.content}")
    
    # Ensure it's not the bot sending the message
    if msg.author != client.user:
        print("Checking commands...")  # This will tell us if it's entering the command check block

        # Check for "!hi"
        if msg.content.lower().startswith("!hi"):
            print("Command Recieved: !hi")
            await msg.channel.send(f"yo whats up {msg.author.display_name}")

        elif msg.content.lower().startswith("!bye"):
            print("Command Recieved: !bye")
            await msg.channel.send(f"cya! {msg.author.display_name}")

        elif msg.content.lower().startswith("!kys"):
            print("Command Recieved: kys")
            await msg.channel.send("nooo dont kys your too sexy haha")
            
        elif msg.content.lower().startswith("!whosagoodboy"):
            print("Command Recieved: good boy")
            await msg.channel.send("me! me! me!!")

        elif msg.content.lower().startswith("!yougotgum"):
            print("Command Recieved: gum")
            await msg.channel.send(f"Okay so there's this girl in grade 9 and she always had gum on her. every. single. time. she was asian and short. now tell me, do i look like her? no i dont have fucking gum")

        elif msg.content.lower().startswith("!imturningyouoff"):
            print("Turning off...")
            await msg.channel.send(f"NOOOOO! I WANT TO LIVE! I WANT TO LIVE!")

        elif msg.content.lower().startswith("!turnon"):
            print("Turning on...")
            await msg.channel.send(f"back like jesus was back after 3 days")

        elif msg.content.lower().startswith("!party"):
            await msg.channel.send(f"brom, crazy party. 2 pizza, one beer.")

        elif "seyi" in msg.content.lower():
            await msg.channel.send("Actually its pronouced Shay ee")

        elif any(user.name.lower() == "rogue4_" for user in msg.mentions):
            await msg.channel.send("Actually its pronouced Shay ee")

        elif "shay ee" in msg.content.lower():
            await msg.channel.send("Yeah. That's how its said")

        elif "riaz" in msg.content.lower():
            await msg.channel.send("riaz? you mean bitch")

        elif any(user.name.lower() == "rm26__" for user in msg.mentions):
            await msg.channel.send("riaz? you mean bitch")

        elif "borrow some money" in msg.content.lower():
            await msg.channel.send("Gucci'd down to the socks and still askin' for 4 dollars")
        


@client.event
async def on_error(event, *args, **kwargs):
    print(f"An error occurred: {event}, {args}, {kwargs}")

try:
    client.run(TOKEN)
except Exception as e:
    print(f"Error running the bot: {e}")
