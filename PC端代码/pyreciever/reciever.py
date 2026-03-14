import requests
import time

url = "http://192.168.137.240:5000/value"

while True:
    try:
        r = requests.get(url,timeout = 1)
        data = r.json()
        print("AIN0 = ",data["ain0"])
    except Exception as e:
        print("Failed:",e)
    time.sleep(0.2)