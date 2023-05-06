from discordwebhook import Discord
from dotenv import dotenv_values

enviroments = dotenv_values(".env")


class DiscordAlert:
    def __init__(self):
        TOKEN = enviroments['TOKEN_DISCORD']
        SECRET_TOKEN = enviroments['SECRET_TOKEN_DISCORD']
        URL = f'https://discord.com/api/webhooks/{TOKEN}/{SECRET_TOKEN}'
        self.discord = Discord(url=URL)

    def send_alert(self, message):
        try:
            return not not self.discord.post(content=message)
        except:
            return False
