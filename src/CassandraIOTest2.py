import requests
import time


while 1:
    url = "http://c6.wap.com/api/v1/orderdata/me/orders/findByTimeuuid?transactionTimeuuid=38902470-f050-11e7-b0e3-5716191582db&access_token=2e8e8d14-4c2e-47a7-9cd2-8f84a73e229e"
    # url = "http://localhost/api/v1/orderdata/me/orders/findByTimeuuid?transactionTimeuuid=38902470-f050-11e7-b0e3-5716191582db&access_token=2e8e8d14-4c2e-47a7-9cd2-8f84a73e229e"
    response = requests.get(url)
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(now + "  " + str(response.status_code))
    time.sleep(0.01)
