import requests
import time
from threading import Timer


class Repeat(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def HealthCheck():
    try:
        response = requests.get('http://localhost:8080/')
        event = response.json()['status']
        log = f'logging event: {event}'
        print(log)
    except:
        print('[ * ] ERROR EXCEPTED . . .')
        time.sleep(60)
        


def exec():
        print("[ * ] EXECUTING . . . ")
        t = Repeat(1.0, lambda: HealthCheck())
        t.start()

exec()
