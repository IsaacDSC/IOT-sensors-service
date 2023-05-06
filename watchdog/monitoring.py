import requests
import time
from threading import Timer
from dotenv import dotenv_values
from discord.discord_bot import DiscordAlert

environments = dotenv_values('.env')
alert = DiscordAlert()


class Repeat(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def HealthCheck():
    try:
        response = requests.get(environments['WHOAMI_URL'])
        if (response.status_code != 200):
            raise TypeError("TEST_ERROR")
        log = f'logging event: {response.json()}'
        print(log)
    except:
        print('[ * ] ERROR EXCEPTED . . .')
        alert.send_alert("[ * ] ERROR SERVICE IOT SENSOR . . .")
        time.sleep(20)
        exec()


def exec():
    print("[ * ] EXECUTING . . . ")
    t = Repeat(1.0, lambda: HealthCheck())
    t.start()


exec()
