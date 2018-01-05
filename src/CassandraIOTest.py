from apscheduler.schedulers.blocking import BlockingScheduler
import requests

def task():
    pattern = "http://localhost:8450/api/v1/orderdata/me/orders/findByState?pageSize=5&currentPage=1&access_token=%s"
    token = "2e8e8d14-4c2e-47a7-9cd2-8f84a73e229e"
    url = pattern % token
    response = requests.get(url)
    print(response)


my_task = BlockingScheduler()
my_task.add_job(task, 'cron', second='*')
my_task.start()
