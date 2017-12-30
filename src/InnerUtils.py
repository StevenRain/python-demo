from datetime import datetime, timedelta
import time

'''
时间操作
'''
# 时间加减
now = datetime.now()
now = now + timedelta(hours=1)
print(now)

# 时间戳
timestamp = now.timestamp() * 1000
print(timestamp)

timestampInSeconds = int(round(time.time()))
timestampInMilliSeconds = int(round(time.time() * 1000))
print(timestampInSeconds)
print(timestampInMilliSeconds)
