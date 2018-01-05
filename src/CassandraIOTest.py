import requests
import threading
import time
import random


def task():
    while 1:
        pattern = "http://localhost:8450/api/v1/orderdata/me/orders/findByState?pageSize=100&currentPage=%d&access_token=%s"
        token = "2e8e8d14-4c2e-47a7-9cd2-8f84a73e229e"
        number = random.random()
        page = int(number * 5)
        url = pattern % (page, token)
        response = requests.get(url)
        print(threading.current_thread().getName())
        time.sleep(1)


threading.Thread(target=task).start()
threading.Thread(target=task).start()
threading.Thread(target=task).start()
threading.Thread(target=task).start()
threading.Thread(target=task).start()
threading.Thread(target=task).start()
threading.Thread(target=task).start()
threading.Thread(target=task).start()
threading.Thread(target=task).start()
threading.Thread(target=task).start()

