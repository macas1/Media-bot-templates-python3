##DATA------------------------------------------------------------------------------------
#api reference: https://skpy.t.allofti.me/api.htm

##SETTINGS--------------------------------------------------------------------------------
username, password = ("emailAddress", "password") #The bot's account
admins = ["live:exampleName"] #Admin commands
users  = [] #The bot will not respond to accounter that are not in either admin or users

##INIT------------------------------------------------------------------------------------
from skpy import SkypeEventLoop, SkypeNewMessageEvent
from threading import Thread

class SkypePing(SkypeEventLoop):
    def __init__(self):
        super(SkypePing, self).__init__(username, password)
        for x in admins + users: #Send activated message to all admins and users
            self.contacts[x].chat.sendMsg("Bot Activated")
    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent):
            if event.msg.userId in admins+users: #Common commands
            
                if event.msg.content.lower() == "ping":
                    event.msg.chat.sendMsg("Pong")

            if event.msg.userId in admins: #Admin commands

                if event.msg.content.lower() == "checkAdmin":
                    event.msg.chat.sendMsg("You are one of my administrators.")




SkypePing().loop()
