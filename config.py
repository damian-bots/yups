from os import getenv
from dotenv import load_dotenv

#Necessary Variables 
API_ID = int(getenv("API_ID", 29400566))
API_HASH = getenv("API_HASH", "8fd30dc496aea7c14cf675f59b74ec6f")
BOT_TOKEN = "7043502393:AAHl5kbadb92YsrY-i4vpnVwCPi3QXCIxvU" #Put your bot token here
CHANNEL = getenv("CHANNEL", "about_tosuu") #Your public channel username without @ for force subscription.
MONGO = "mongodb+srv://tusar:tusar1@cluster0.guw5d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" #Put mongo db url here
#Optional Variables
OWNER_ID = int(getenv("OWNER_ID", 6848223695)) #Go to @ThunderrXbot and type /id and put that value here. 
FSUB = bool(getenv("FSUB", True)) #Set this True if you want to enable force subscription from users else set to False.
