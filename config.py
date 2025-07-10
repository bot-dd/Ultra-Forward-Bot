import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "26649585")
    API_HASH = environ.get("API_HASH", "588a3ea6fd01ae88bd2e10fed7d55b2c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Rahat:EGbbbvweNl6EFzf6@rahat.pizkp.mongodb.net/?retryWrites=true&w=majority&appName=Rahat")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Rahat")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7945551029').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002312610528'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/RMxBots") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
