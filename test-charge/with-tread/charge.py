import os
import datetime
import time
import requests
from uuid import uuid4 as uuid
from multiprocessing.pool import ThreadPool as Pool

urls = []
counter_success_response = 0
quantity_request = 5000
time_init = time.time()
date_init = datetime.datetime.now().isoformat()

for index in range(quantity_request):
    urls.append('http://192.168.1.100/operation/sensor/analogic')
    counter_success_response += 1


# urls[2]('http://192.168.1.100/operation/sensor/analogic')
def send_request(U):
    URL = 'http://192.168.1.100/operation/sensor/analogic'
    # URL = 'http://localhost:8000/operation/sensor/analogic'
    body = {
        "sensor_name": f'sensor_{uuid()}',
        "tag": f'PT-100-{uuid()}',
        "value": 67.9,
        "unit": 'C'
    }
    resp = requests.post(URL, json=body)
    print(resp.json())
    


pool = Pool(processes=os.cpu_count())
pool.map(send_request, urls)

print("\n\nEND\n\n")
resume = dict(
    quantity_request=counter_success_response,
    time= round(((time.time()-time_init)/60),4),
    date=date_init
)
print(resume)
print(f'finished request -> {resume}')