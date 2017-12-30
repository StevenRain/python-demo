import time
import sched
import datetime
from threading import Timer
from apscheduler.schedulers.blocking import BlockingScheduler


def task1():
    """
    任务1
    :return:
    """
    current_time = datetime.datetime.now()
    current_time = datetime.datetime(current_time.date().__str__(), '%Y')
    print('Task-1 ' + current_time.__str__())


def task2():
    """
    任务2
    :return:
    """
    current_time = datetime.datetime.now()
    print('Task-2 ' + current_time.__str__())


# 第一种定时任务，不能自动重新装配
# task = sched.scheduler(time.time, time.sleep)
# task.enter(1, 0, task1)
# task.enter(2, 0, task2)
# task.run()


# 第二种方式，也不能自动重新装配
# Timer(1, task1).start()
# Timer(2, task2).start()


# 第三种方式, 可以自动装配
def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


task = BlockingScheduler()
# task.add_job(my_job, args=('steven'), trigger='interval', seconds=1)
task.add_job(my_job, 'cron', year=2017, month=12, day=30, hour=16, minute=17, second='*')
task.start()

